# Simple Python Web Calculator

A single-file Flask app that serves a small calculator UI and keeps an in-memory history of saved calculations.

Quick start (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python simple_python_web_calculator.py
```

Open http://127.0.0.1:5000 in your browser. The calculator evaluates expressions in the browser (safe subset) and POSTs completed calculations to `/save` so the server can store a short history retrievable at `/history` (JSON).

Notes:
- This is a toy dev server — don't expose it to the public internet.
- History is in-memory and will be lost when the server stops.
 
 Project layout
 - `simple_python_web_calculator.py` — Flask app (server-side routes)
 - `templates/index.html` — UI (HTML/CSS/JS)
 - `requirements.txt` — Python dependencies
 - `.gitignore` — files to ignore when committing

When uploading to GitHub, commit the Python and templates files but do NOT commit the `venv/` folder; it's excluded by `.gitignore`.

Quick run helpers
- PowerShell: `run.ps1` — runs the app with the venv python if present.
- Windows cmd: `run.bat` — runs the app with the venv python if present.
- `fallback_server.py` — a pure-Python server (no Flask) that serves the UI and implements `/save` and `/history` for quick previews. Run with:

```powershell
python fallback_server.py
```

The fallback server listens on http://127.0.0.1:8000 by default.

## VS Code interpreter

If you're using VS Code, make sure the editor is using the project's virtual environment so run/debug actions use the same Python that has Flask installed.

Copy-paste these steps:

1. Open the Command Palette (Ctrl+Shift+P) and run "Python: Select Interpreter".
2. Choose the interpreter at:

```
D:\\New folder\\venv\\Scripts\\python.exe
```

3. Reload the window (Command Palette → "Developer: Reload Window") if the status bar doesn't update immediately.

After that, running the file (Run Python File / F5) will use the venv and should find Flask.

## PowerShell quick commands (copy-paste)

If you're on Windows PowerShell and want exact commands to create a venv, install dependencies and run the app, paste these lines into PowerShell (in the project folder):

```powershell
# create venv (only once)
python -m venv venv

# activate the venv for this PowerShell session
.\venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# run the app (dev server)
python simple_python_web_calculator.py

# open the app in your default browser (optional)
Start-Process http://127.0.0.1:5000
```

## Troubleshooting

- ModuleNotFoundError: No module named 'flask'
	- Reason: Flask isn't installed in the Python interpreter you're using. Ensure you activated the `venv` before running `pip install -r requirements.txt` and that VS Code is using the same interpreter.

- SyntaxError / unterminated triple-quoted string when running a temp runner (`tempCodeRunnerFile.python`)
	- Reason: Running a selection or temporary file can cut off the top/bottom of triple-quoted docstrings. Run the full file instead:

```powershell
# inside project folder - run the whole file, not a selection
python simple_python_web_calculator.py
```

That should avoid the invalid-escape and unterminated-string warnings you saw when running snippets.
