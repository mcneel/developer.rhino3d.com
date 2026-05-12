---
description: Run every C#/Python sample on a Rhino/Eto doc page through the Rhino MCP, fixing bugs as we go
---

# Verify Rhino doc samples

Run every runnable code sample on the doc page at `$ARGUMENTS` through Rhino — Python via `mcp__rhino__run_python`, C# via `mcp__rhino__run_csharp` — and have the user visually confirm each one. The goal is catching bugs static review misses (empty grids, off-screen dialogs, scrambled scroll, wrong bindings).

If no path is given in `$ARGUMENTS`, ask the user which page.

## Setup

1. Use TodoWrite to track each sample.
2. Read the page and inventory every fenced code block. Map tab ids (`py1`, `cs5`, etc.) to what each sample demonstrates.
3. Skip:
   - Fences marked ` no-compile`
   - Empty fences
   - Samples the prose says don't run in the script editor (e.g. `LocalizeAndRestore`)
   - Pages that look orphaned (grep for inbound links first if uncertain)
4. The user verifies visually — don't try to assert correctness from stdout. After each run, give a one-line "you should see X" and ask "Look right?".

## Auto-close wrapper

Modal dialogs (`ShowModal` / `ShowSemiModal`) block the script. Wrap with a UITimer that closes the dialog after a few seconds.

Python:
```py
timer = ef.UITimer()
timer.Interval = 4
def _close(s, e):
    timer.Stop()
    dialog.Close()
timer.Elapsed += _close
timer.Start()
```

C#:
```cs
var timer = new UITimer { Interval = 4 };
timer.Elapsed += (s, e) => { timer.Stop(); dialog.Close(); };
timer.Start();
```

Place the wrapper immediately before the `ShowModal` / `ShowSemiModal` call. For samples that need scrolling or interaction to see the bug (e.g. broken-on-purpose CustomCell), bump the interval to 15s.

Non-modal forms (`form.Show(...)`) return immediately. Don't try to auto-close — the timer reference can be GC'd before it fires. Tell the user `close manually` in the status message.

Samples that prompt for input (`MessageBox.Show`, `RhinoGet.*`, `OpenFileDialog`, etc.) can't be auto-closed. Either run and warn the user about needed interaction, or skip them and note that the doc fix landed but wasn't exercised.

## Known bug patterns

If a sample errors or shows wrong behaviour, check these before diagnosing from scratch — they recur across the eto docs:

**Python:**
- Rows built from bare Python lists: `items.Add([0, "Zero"])` — Python `list` doesn't satisfy the `IList` interface `TextBoxCell(int)`/`CheckBoxCell(int)`/`ComboBoxCell(int)` need for indexing. Wrap each row: `items.Add(List[object]([0, "Zero"]))` (requires `from System.Collections.Generic import List`).
- Trailing comma: `gridView.DataStore = items,` turns `items` into a 1-tuple.
- C# syntax leaks: `var x = ...;`, trailing `;`, `true`/`false`/`null`.
- Missing `ef.` / `ed.` prefix on enums (`Orientation.Vertical`, `Size(8,8)`, `DialogResult.Cancel`).
- `RhinoDoc.<Event> -= handler` on first call — pythonnet throws if the handler isn't already subscribed. Wrap each `-=` in `try/except`.
- `EtoExtensions.WindowsFromDocument[T](doc)[0]` — returns an `IEnumerable[T]` which isn't subscriptable in Python. Use `next(iter(...), None)` or `list(...)[0]`.
- `TextBoxCell("Text")` binding to a Python object — case-sensitive, must match the attribute name exactly.
- `ObservableCollection[type(MyClass)]()` — `type(MyClass)` is `type`, not the class. Use `ObservableCollection[object]()`.

**C#:**
- `dialog.Show(parent)` — `Dialog` has no `Show`, only `ShowModal` / `ShowModalAsync`. (Use `Form` if you need a non-modal window, or change to `ShowModal`.)
- Missing semicolon after a collection initializer assigned to a variable.

## Per-sample loop

For each runnable sample:

1. TodoWrite: mark in_progress.
2. Apply the auto-close wrapper if it's a modal dialog.
3. Run via the appropriate MCP tool.
4. If stdout shows an error or exception:
   - Diagnose
   - Fix the source code in the doc with Edit
   - Re-run
5. Print one sentence telling the user what they should see, then ask "Look right?" (or similar).
6. Wait for user confirmation. "next" / "yep" / "great" → proceed. Anything else → dig in.
7. TodoWrite: mark completed.

## Wrap-up

At the end, summarise:
- What was run and confirmed working
- What bugs were fixed (file, sample id, one-line description)
- What was skipped and why

Don't commit anything — leave fixes as working-tree changes for the user to review.
