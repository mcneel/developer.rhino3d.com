#!/usr/bin/env python3
"""Unit tests for script/ds2json.py.  Run with ``python script/test_ds2json.py``."""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ds2json  # noqa: E402

APPLICATION_PY = r'''
import Rhino

def AliasMacro(alias, macro=None):
    """Returns or modifies the macro of a command alias.
    Second line of the description.
    Parameters:
      alias (str): The name of an existing command alias.
      macro (str, optional): The new macro. If omitted,
        the current macro is returned.
    Returns:
      str: the macro
      None: on error
    Example:
      import rhinoscriptsyntax as rs
      print(rs.AliasMacro("C:\\path"))
    See Also:
      AddAlias
      NoSuchFunction
    """
    return None


def AddAlias(alias, macro):
    """Add new command alias.
    Parameters:
      alias (str): name
      macro (str): macro
    Returns:
      bool: success
    Example:
      import rhinoscriptsyntax as rs
      rs.AddAlias("a", "b")
    See Also:
      AliasMacro
    """


def _helper():
    """Not part of the API."""


def lowercase():
    """Not part of the API either."""


def Broken(x, y=1):
    """Description only.
    Params:
      x (number): under a misspelled header
    Returns:
    Example:
      if x: for y in z: print(y)
    """


def NoDoc():
    return 1
'''

CURVE_PY = '''
def AddLine(start, end, tolerance=0.0):
    """Adds a line.
    Parameters:
      start (point): start
      end (point): end
    Returns:
      guid: identifier
    Example:
      import rhinoscriptsyntax as rs
      rs.AddLine((0,0,0), (1,1,1))
    See Also:
      AliasMacro, AddAlias
    """
'''


class TempPackage(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.package = self.root / "Scripts" / "rhinoscript"
        self.package.mkdir(parents=True)
        (self.package / "application.py").write_text(APPLICATION_PY, encoding="utf-8")
        (self.package / "curve.py").write_text(CURVE_PY, encoding="utf-8")
        (self.package / "__init__.py").write_text("", encoding="utf-8")
        self.docs, self.name_to_module, self.findings = ds2json.collect(self.package)
        self.by_name = {doc.name: doc for doc in self.docs}

    def tearDown(self):
        self._tmp.cleanup()

    def codes(self, function):
        return sorted(f.code for f in self.findings if f.function == function)


class ParsingTests(TempPackage):
    def test_only_public_functions_are_collected(self):
        self.assertEqual(sorted(self.by_name), ["AddAlias", "AddLine", "AliasMacro", "Broken", "NoDoc"])

    def test_signature_is_normalised_from_the_ast(self):
        self.assertEqual(self.by_name["AliasMacro"].signature, "AliasMacro(alias, macro=None)")
        self.assertEqual(self.by_name["AddLine"].signature, "AddLine(start, end, tolerance=0.0)")

    def test_description_keeps_continuation_lines(self):
        self.assertEqual(
            self.by_name["AliasMacro"].description,
            "Returns or modifies the macro of a command alias.\nSecond line of the description.",
        )

    def test_sections_are_dedented_but_keep_relative_indentation(self):
        doc = self.by_name["AliasMacro"]
        self.assertEqual(
            doc.parameters,
            "alias (str): The name of an existing command alias.\n"
            "macro (str, optional): The new macro. If omitted,\n"
            "  the current macro is returned.",
        )
        self.assertEqual(doc.returns, "str: the macro\nNone: on error")

    def test_example_is_the_source_text_not_the_evaluated_string(self):
        # "C:\\path" in the file must stay "C:\\path" so the example remains valid Python.
        self.assertIn('print(rs.AliasMacro("C:\\\\path"))', self.by_name["AliasMacro"].example)

    def test_see_also_accepts_one_per_line_and_comma_separated(self):
        self.assertEqual(self.by_name["AliasMacro"].see_also, ["AddAlias", "NoSuchFunction"])
        self.assertEqual(self.by_name["AddLine"].see_also, ["AliasMacro", "AddAlias"])

    def test_missing_docstring_still_yields_an_entry(self):
        self.assertEqual(self.by_name["NoDoc"].signature, "NoDoc()")
        self.assertEqual(self.by_name["NoDoc"].description, "")


class FindingTests(TempPackage):
    def test_well_formed_docstring_has_no_findings(self):
        self.assertEqual(self.codes("AddAlias"), [])

    def test_unresolved_see_also_is_reported(self):
        self.assertEqual(self.codes("AliasMacro"), ["see-also-unresolved"])

    def test_parameter_mismatch_is_reported(self):
        self.assertEqual(self.codes("AddLine"), ["parameter-mismatch"])
        message = next(f.message for f in self.findings if f.function == "AddLine")
        self.assertIn("tolerance", message)

    def test_broken_docstring_reports_each_problem(self):
        self.assertEqual(
            self.codes("Broken"),
            ["empty-section", "example-syntax-error", "missing-section", "missing-section", "unknown-section"],
        )

    def test_missing_docstring_is_reported(self):
        self.assertEqual(self.codes("NoDoc"), ["no-docstring"])


class OutputTests(TempPackage):
    @staticmethod
    def run_main(*args):
        """Run ds2json.main without its console output cluttering the test run."""
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return ds2json.main(list(args))

    def test_json_shape_matches_the_hugo_shortcode(self):
        data = ds2json.build_json(self.docs, self.name_to_module)
        self.assertEqual([m["ModuleName"] for m in data], ["application", "curve"])
        entry = data[0]["functions"][0]
        self.assertEqual(
            list(entry),
            ["ModuleName", "Name", "Signature", "Description", "HasArguments",
             "ArgumentDesc", "Returns", "ExampleString", "SeeAlso"],
        )
        self.assertEqual(entry["Name"], "AliasMacro")
        self.assertTrue(entry["HasArguments"])
        # unresolved entries are dropped; resolved ones carry their module
        self.assertEqual(entry["SeeAlso"], [{"ModuleName": "application", "FunctionName": "AddAlias"}])
        curve = data[1]["functions"][0]
        self.assertEqual(
            curve["SeeAlso"],
            [{"ModuleName": "application", "FunctionName": "AliasMacro"},
             {"ModuleName": "application", "FunctionName": "AddAlias"}],
        )
        self.assertFalse(data[0]["functions"][-1]["HasArguments"])

    def test_resolve_package_dir_accepts_root_scripts_or_package(self):
        for candidate in (self.root, self.root / "Scripts", self.package):
            self.assertEqual(ds2json.resolve_package_dir(candidate), self.package)
        with self.assertRaises(SystemExit):
            ds2json.resolve_package_dir(self.root / "nowhere")

    def test_main_writes_json_and_report(self):
        output = self.root / "out" / "rhinoscriptsyntax.json"
        report = self.root / "report.md"
        code = self.run_main("--source", str(self.root), "--output", str(output), "--report", str(report))
        self.assertEqual(code, 0)
        data = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(len(data), 2)
        self.assertIn("# RhinoScriptSyntax docstring report", report.read_text(encoding="utf-8"))
        self.assertIn("`application.Broken`", report.read_text(encoding="utf-8"))

    def test_check_does_not_write_and_strict_fails_on_findings(self):
        output = self.root / "never.json"
        code = self.run_main("--source", str(self.root), "--output", str(output), "--check", "--strict")
        self.assertEqual(code, 2)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
