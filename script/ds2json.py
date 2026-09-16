#!/usr/bin/env python3
"""Generate the RhinoScriptSyntax API reference data from rhinoscriptsyntax docstrings.

Reads every module of the ``rhinoscript`` package in a checkout of
https://github.com/mcneel/rhinoscriptsyntax, parses the docstring of every
public function and writes ``data/rhinoscriptsyntax.json``.  The
``rhinoscriptsyntax`` Hugo shortcode (layouts/shortcodes/rhinoscriptsyntax.html)
renders that file at https://developer.rhino3d.com/api/RhinoScriptSyntax/.

The expected docstring layout is described in docstring.md in the
rhinoscriptsyntax repo::

    def AliasMacro(alias, macro=None):
        \"\"\"Returns or modifies the macro of a command alias.
        Parameters:
          alias (str): The name of an existing command alias.
          macro (str, optional): The new macro to run when the alias is executed.
        Returns:
          str: The existing macro if successful.
        Example:
          import rhinoscriptsyntax as rs
          print(rs.AliasMacro("Hello"))
        See Also:
          AddAlias
          AliasCount
        \"\"\"

Besides generating the JSON, the script lints every docstring against that
layout (missing or misspelled sections, parameters that do not match the
signature, "See Also" entries that do not exist, examples that do not parse as
Python 3, ...) and can write the findings to a Markdown report.

Usage::

    python script/ds2json.py --source path/to/rhinoscriptsyntax
    python script/ds2json.py --source path/to/rhinoscriptsyntax --report report.md
    python script/ds2json.py --source path/to/rhinoscriptsyntax --check --strict
    RHINOSCRIPTSYNTAX_DIR=path/to/rhinoscriptsyntax python script/ds2json.py

Requires Python 3.9 or newer and nothing outside the standard library.
"""
from __future__ import annotations

import argparse
import ast
import inspect
import json
import os
import re
import subprocess
import sys
import textwrap
import warnings
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "data" / "rhinoscriptsyntax.json"
SOURCE_ENV_VAR = "RHINOSCRIPTSYNTAX_DIR"
PACKAGE_SUBDIR = Path("Scripts") / "rhinoscript"

PARAMETERS = "Parameters:"
RETURNS = "Returns:"
EXAMPLE = "Example:"
SEE_ALSO = "See Also:"
SECTION_ORDER = (PARAMETERS, RETURNS, EXAMPLE, SEE_ALSO)

# A line consisting of one of these (case-insensitively) almost certainly was
# meant to be a section header.  It is reported so it does not silently end up
# as text inside the previous section.
SUSPECT_HEADERS = frozenset(
    {header.lower() for header in SECTION_ORDER}
    | {
        "parameter:", "params:", "param:", "args:", "arguments:",
        "return:", "yields:",
        "examples:", "sample:", "samples:", "usage:",
        "seealso:", "also see:", "related:",
    }
)

# "name (type): description" or "name: description"; several names may share
# one line ("x, y (number): ...").
PARAM_LINE = re.compile(r"^([A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)*)\s*[(:]")


@dataclass
class Finding:
    """One problem found in one docstring."""

    code: str
    module: str
    function: str
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.code}: {self.module}.{self.function} ({self.module}.py:{self.line}): {self.message}"


@dataclass
class FunctionDoc:
    """The parsed documentation of one public rhinoscriptsyntax function."""

    module: str
    name: str
    line: int
    signature: str
    description: str = ""
    parameters: str = ""
    returns: str = ""
    example: str = ""
    see_also: List[str] = field(default_factory=list)

    def to_dict(self, name_to_module: Dict[str, str]) -> dict:
        """The JSON shape consumed by layouts/shortcodes/rhinoscriptsyntax.html."""
        return {
            "ModuleName": self.module,
            "Name": self.name,
            "Signature": self.signature,
            "Description": self.description,
            "HasArguments": bool(self.parameters),
            "ArgumentDesc": self.parameters,
            "Returns": self.returns,
            "ExampleString": self.example,
            "SeeAlso": [
                {"ModuleName": name_to_module[target], "FunctionName": target}
                for target in self.see_also
                if target in name_to_module
            ],
        }


# --------------------------------------------------------------------------- #
# Docstring parsing
# --------------------------------------------------------------------------- #

def is_public(name: str) -> bool:
    """rhinoscriptsyntax API functions are CapitalCase; helpers are lower_case."""
    return name[:1].isupper()


def split_sections(docstring: str) -> Tuple[List[str], Dict[str, List[str]], List[Tuple[str, str]]]:
    """Split a raw docstring into description lines and per-section lines.

    Returns ``(description_lines, {header: lines}, [(code, message), ...])``.
    A header is a line whose stripped text is exactly one of SECTION_ORDER.
    """
    lines = inspect.cleandoc(docstring).splitlines()
    description: List[str] = []
    sections: Dict[str, List[str]] = {}
    order: List[str] = []
    problems: List[Tuple[str, str]] = []
    current: Optional[str] = None

    for line in lines:
        stripped = line.strip()
        if stripped in SECTION_ORDER:
            if stripped in sections:
                problems.append(("duplicate-section", f"'{stripped}' appears more than once"))
            else:
                sections[stripped] = []
                order.append(stripped)
            current = stripped
            continue
        if stripped.lower() in SUSPECT_HEADERS:
            problems.append((
                "unknown-section",
                f"'{stripped}' looks like a section header; expected one of "
                + ", ".join(f"'{h}'" for h in SECTION_ORDER),
            ))
        (sections[current] if current else description).append(line)

    expected = [header for header in SECTION_ORDER if header in sections]
    if order != expected:
        problems.append(("section-order", f"sections appear as {order}, expected {expected}"))
    return description, sections, problems


def block_text(lines: Sequence[str]) -> str:
    """Dedent a section body and strip surrounding whitespace."""
    return textwrap.dedent("\n".join(line.rstrip() for line in lines)).strip()


def description_text(lines: Sequence[str]) -> str:
    """The description's first line follows the opening quotes, so it carries
    no indentation of its own; dedent the continuation lines separately."""
    cleaned = [line.rstrip() for line in lines]
    while cleaned and not cleaned[0].strip():
        cleaned.pop(0)
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()
    if not cleaned:
        return ""
    first, rest = cleaned[0].strip(), cleaned[1:]
    if not rest:
        return first
    return f"{first}\n{textwrap.dedent(chr(10).join(rest))}".strip()


def see_also_names(lines: Sequence[str]) -> List[str]:
    """One function name per line by convention; commas are tolerated."""
    names: List[str] = []
    for line in lines:
        names.extend(name for name in re.split(r"[,\s]+", line.strip()) if name)
    return names


def signature_parameters(node: ast.FunctionDef) -> List[str]:
    args = node.args
    names = [arg.arg for arg in (*args.posonlyargs, *args.args)]
    if args.vararg:
        names.append(args.vararg.arg)
    names.extend(arg.arg for arg in args.kwonlyargs)
    if args.kwarg:
        names.append(args.kwarg.arg)
    return names


def documented_parameters(parameters: str) -> List[str]:
    """Parameter names from a dedented 'Parameters:' body.  Continuation lines
    are indented, so only lines starting at column 0 are considered."""
    names: List[str] = []
    for line in parameters.splitlines():
        if not line or line[0].isspace():
            continue
        match = PARAM_LINE.match(line)
        if match:
            names.extend(name.strip() for name in match.group(1).split(","))
    return names


STRING_LITERAL = re.compile(r"^[rRuUbB]{0,2}(\"\"\"|\'\'\'|\"|\')(.*)\1$", re.DOTALL)


def raw_docstring(node: ast.FunctionDef, source: str) -> Optional[str]:
    """The function's docstring exactly as typed in the source file.

    ``ast.get_docstring`` returns the *evaluated* string, in which ``"C:\\\\Users"``
    has already become ``"C:\\Users"``.  The examples are meant to be copied into
    a script, so they must keep their escapes; the generator has therefore
    always published the source text rather than ``__doc__``.
    """
    if not node.body:
        return None
    first = node.body[0]
    if not (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)):
        return None
    segment = ast.get_source_segment(source, first.value)
    match = STRING_LITERAL.match(segment) if segment else None
    return match.group(2) if match else first.value.value


def parses_as_python(code: str) -> Optional[str]:
    """None if ``code`` parses as Python 3, otherwise a short error message."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ast.parse(code)
    except SyntaxError as exc:
        return f"line {exc.lineno}: {exc.msg}"
    return None


def parse_module(path: Path) -> Tuple[List[FunctionDoc], List[Finding]]:
    """Parse one rhinoscript module.  Raises SyntaxError if it is not valid Python 3."""
    module = path.stem
    source = path.read_text(encoding="utf-8")
    findings: List[Finding] = []

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        tree = ast.parse(source, filename=str(path))
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]

    def enclosing_function(line: int) -> str:
        for node in functions:
            if node.lineno <= line <= (node.end_lineno or node.lineno):
                return node.name
        return "<module>"

    for warning in caught:
        # e.g. "\s" inside a docstring, which Python will eventually reject.
        if issubclass(warning.category, SyntaxWarning):
            line = warning.lineno or 0
            findings.append(Finding("syntax-warning", module, enclosing_function(line), line, str(warning.message)))

    docs: List[FunctionDoc] = []
    for node in functions:
        if not is_public(node.name):
            continue
        doc = FunctionDoc(module, node.name, node.lineno, f"{node.name}({ast.unparse(node.args)})")
        docs.append(doc)

        def problem(code: str, message: str, _node: ast.FunctionDef = node) -> None:
            findings.append(Finding(code, module, _node.name, _node.lineno, message))

        raw = raw_docstring(node, source)
        if raw is None:
            problem("no-docstring", "public function has no docstring")
            continue

        description, sections, problems = split_sections(raw)
        for code, message in problems:
            problem(code, message)

        doc.description = description_text(description)
        doc.parameters = block_text(sections.get(PARAMETERS, []))
        doc.returns = block_text(sections.get(RETURNS, []))
        doc.example = block_text(sections.get(EXAMPLE, []))
        doc.see_also = see_also_names(sections.get(SEE_ALSO, []))

        if not doc.description:
            problem("empty-description", "docstring has no description")

        expected_params = signature_parameters(node)
        if PARAMETERS in sections:
            documented = documented_parameters(doc.parameters)
            missing = [p for p in expected_params if p not in documented]
            extra = [p for p in documented if p not in expected_params]
            if missing or extra:
                details = []
                if missing:
                    details.append("not documented: " + ", ".join(missing))
                if extra:
                    details.append("documented but not in the signature: " + ", ".join(extra))
                problem("parameter-mismatch", "; ".join(details))
        elif expected_params:
            problem("missing-section", f"no '{PARAMETERS}' section, but the function takes {', '.join(expected_params)}")

        for header in (RETURNS, EXAMPLE, SEE_ALSO):
            if header not in sections:
                problem("missing-section", f"no '{header}' section")
        if RETURNS in sections and not doc.returns:
            problem("empty-section", f"'{RETURNS}' section is empty")
        if EXAMPLE in sections and not doc.example:
            problem("empty-section", f"'{EXAMPLE}' section is empty")

        if doc.example:
            error = parses_as_python(doc.example)
            if error:
                problem("example-syntax-error", f"example does not parse as Python 3 ({error})")

    return docs, findings


# --------------------------------------------------------------------------- #
# Package level
# --------------------------------------------------------------------------- #

def resolve_package_dir(source: Path) -> Path:
    """Accept the repo root, its Scripts folder or the rhinoscript package itself."""
    for candidate in (source, source / PACKAGE_SUBDIR, source / "rhinoscript"):
        if (candidate / "application.py").is_file() and (candidate / "curve.py").is_file():
            return candidate
    raise SystemExit(
        f"error: {source} does not look like a rhinoscriptsyntax checkout "
        f"(expected to find {PACKAGE_SUBDIR / 'application.py'})"
    )


def module_paths(package_dir: Path) -> List[Path]:
    return sorted(path for path in package_dir.glob("*.py") if not path.name.startswith("_"))


def collect(package_dir: Path) -> Tuple[List[FunctionDoc], Dict[str, str], List[Finding]]:
    docs: List[FunctionDoc] = []
    findings: List[Finding] = []
    for path in module_paths(package_dir):
        module_docs, module_findings = parse_module(path)
        docs.extend(module_docs)
        findings.extend(module_findings)

    name_to_module: Dict[str, str] = {}
    for doc in docs:
        if doc.name in name_to_module:
            findings.append(Finding(
                "duplicate-function", doc.module, doc.name, doc.line,
                f"also defined in {name_to_module[doc.name]}.py; 'See Also' links resolve to that one",
            ))
        else:
            name_to_module[doc.name] = doc.module

    for doc in docs:
        for target in doc.see_also:
            if target not in name_to_module:
                findings.append(Finding(
                    "see-also-unresolved", doc.module, doc.name, doc.line,
                    f"'{SEE_ALSO}' entry '{target}' is not a public rhinoscriptsyntax function; dropped from the output",
                ))

    findings.sort(key=lambda f: (f.code, f.module, f.line, f.function))
    return docs, name_to_module, findings


def build_json(docs: Sequence[FunctionDoc], name_to_module: Dict[str, str]) -> list:
    """Modules sorted by name; functions in source order."""
    by_module: Dict[str, List[FunctionDoc]] = defaultdict(list)
    for doc in docs:
        by_module[doc.module].append(doc)
    return [
        {"ModuleName": module, "functions": [doc.to_dict(name_to_module) for doc in by_module[module]]}
        for module in sorted(by_module)
    ]


def describe_git_checkout(path: Path) -> Optional[str]:
    """'abc1234 (rhino-8.x)' for the checkout containing ``path``, if it is one."""
    def git(*args: str) -> str:
        return subprocess.run(
            ["git", "-C", str(path), *args], capture_output=True, text=True, check=True
        ).stdout.strip()

    try:
        sha = git("rev-parse", "--short", "HEAD")
        branch = git("rev-parse", "--abbrev-ref", "HEAD")
    except (OSError, subprocess.CalledProcessError):
        return None
    return sha if branch == "HEAD" else f"{sha} ({branch})"


def write_report(path: Path, package_dir: Path, source_desc: Optional[str],
                 docs: Sequence[FunctionDoc], findings: Sequence[Finding]) -> None:
    counts = Counter(finding.code for finding in findings)
    modules = {doc.module for doc in docs}
    lines = [
        "# RhinoScriptSyntax docstring report",
        "",
        f"- Source: `{package_dir}`" + (f" at `{source_desc}`" if source_desc else ""),
        f"- Modules: {len(modules)}",
        f"- Public functions: {len(docs)}",
        f"- Findings: {len(findings)}",
        "",
    ]
    if findings:
        lines += ["| Finding | Count |", "|---|---:|"]
        lines += [f"| `{code}` | {count} |" for code, count in sorted(counts.items())]
        lines.append("")
        for code in sorted(counts):
            lines += [f"## {code} ({counts[code]})", ""]
            lines += [
                f"- `{f.module}.{f.function}` ({f.module}.py:{f.line}): {f.message}"
                for f in findings if f.code == code
            ]
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Command line
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate data/rhinoscriptsyntax.json from the rhinoscriptsyntax docstrings.",
        epilog=f"The source can also be given through the {SOURCE_ENV_VAR} environment variable.",
    )
    parser.add_argument(
        "--source", type=Path, default=os.environ.get(SOURCE_ENV_VAR),
        help="path to a rhinoscriptsyntax checkout (the repo root, or its Scripts/rhinoscript folder)",
    )
    parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"where to write the JSON (default: {DEFAULT_OUTPUT.relative_to(REPO_ROOT)})",
    )
    parser.add_argument("--report", type=Path, help="write a Markdown report of the docstring findings to this file")
    parser.add_argument("--check", action="store_true", help="parse and lint only; do not write the JSON")
    parser.add_argument("--strict", action="store_true", help="exit with status 2 if there is any docstring finding")
    parser.add_argument("--quiet", action="store_true", help="do not print individual findings")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.source is None:
        parser.error(f"--source is required (or set {SOURCE_ENV_VAR})")

    package_dir = resolve_package_dir(args.source.resolve())
    source_desc = describe_git_checkout(package_dir)
    try:
        docs, name_to_module, findings = collect(package_dir)
    except SyntaxError as exc:
        print(f"error: {exc.filename}:{exc.lineno}: not valid Python 3: {exc.msg}", file=sys.stderr)
        return 1
    if not docs:
        print(f"error: no public functions found in {package_dir}", file=sys.stderr)
        return 1

    modules = len({doc.module for doc in docs})
    where = f"{package_dir}" + (f" at {source_desc}" if source_desc else "")
    print(f"rhinoscriptsyntax: {modules} modules, {len(docs)} public functions ({where})")

    if not args.check:
        text = json.dumps(build_json(docs, name_to_module), indent=2, ensure_ascii=False) + "\n"
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        print(f"wrote {args.output} ({len(text.encode('utf-8')) / 1024:.0f} KiB)")

    if args.report:
        write_report(args.report, package_dir, source_desc, docs, findings)
        print(f"wrote {args.report}")

    if findings:
        counts = Counter(finding.code for finding in findings)
        summary = ", ".join(f"{code} {count}" for code, count in sorted(counts.items()))
        print(f"{len(findings)} docstring findings: {summary}", file=sys.stderr)
        if not args.quiet:
            for finding in findings:
                print(f"  {finding}", file=sys.stderr)
    else:
        print("no docstring findings")

    return 2 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
