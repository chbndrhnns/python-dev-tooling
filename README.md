# ruff + uv Playground 🚀

A GitHub Codespaces-ready environment to explore [**ruff**](https://docs.astral.sh/ruff/) (linter + formatter) and [**uv**](https://docs.astral.sh/uv/) (Python package manager) — both from [Astral](https://astral.sh).

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/chbndrhnns/python-dev-tooling)

---

## 🏁 Getting started

Open this repo in a Codespace and everything is pre-configured. Once the container is ready:

```bash
# Install dependencies
make install

# or manually:
uv sync
```

---

## 🔧 uv cheat sheet

```bash
# Add a dependency
uv add httpx

# Add a dev-only dependency
uv add --dev pytest

# Remove a dependency
uv remove httpx

# Run a command in the venv
uv run python src/example.py

# Show installed packages
uv pip list

# Upgrade all packages
uv lock --upgrade && uv sync
```

---

## 🧹 ruff cheat sheet

```bash
# Lint the project
uv run ruff check src/ tests/

# Auto-fix lint issues
uv run ruff check --fix src/ tests/

# Format code (like Black)
uv run ruff format src/ tests/

# Check formatting without writing
uv run ruff format --check src/ tests/

# Show all active rules
uv run ruff rule --all
```

---

## 🛠 Makefile shortcuts

| Command        | Description                        |
|----------------|------------------------------------|
| `make install` | `uv sync --all-extras`             |
| `make lint`    | `ruff check`                       |
| `make fix`     | `ruff check --fix`                 |
| `make format`  | `ruff format`                      |
| `make test`    | `pytest` via uv                    |
| `make ci`      | lint + format-check + test         |

---

## 📁 Project structure

```
.
├── .devcontainer/
│   └── devcontainer.json   # Codespaces config (uv, ruff, VS Code extensions)
├── src/
│   ├── example.py          # Clean file — passes all rules (reference)
│   └── messy_code.py       # Deliberately bad file — demonstrates ~20 rule categories
├── tests/
│   └── test_example.py     # pytest tests
├── pyproject.toml          # Project + ruff + uv config (single source of truth)
├── Makefile                # Convenience shortcuts
└── README.md
```

---

## 🧨 The messy file

`src/messy_code.py` is a **showcase of intentional violations** — one section per rule family. Use it to:

1. **See every violation**: `uv run ruff check src/messy_code.py`
2. **Auto-fix what can be fixed**: `uv run ruff check --fix src/messy_code.py`
3. **Format the aftermath**: `uv run ruff format src/messy_code.py`

Rule families covered include: `F` (Pyflakes), `E/W` (pycodestyle), `I` (isort), `UP` (pyupgrade), `B` (bugbear), `C4/C90` (comprehensions/complexity), `ANN` (annotations), `ARG` (unused args), `DTZ` (timezones), `EM` (errmsg), `ERA` (commented code), `FBT` (boolean traps), `FURB` (refurb), `G` (logging), `N` (naming), `PERF` (performance), `PTH` (pathlib), `RET` (return), `RUF` (ruff-specific), `S` (security), `SIM` (simplify), `SLF` (private access), `T10/T20` (debugger/print), `TRY` (exceptions), `YTT` (sys.version), and more.

---

## ⚙️ Configured rule categories

All ruff settings live in `pyproject.toml` under `[tool.ruff]`. The playground enables **every stable rule category** except:

| Excluded | Reason |
|---|---|
| `COM812`, `COM819` | Conflict with `ruff format` (trailing commas) |
| `ISC001` | Conflicts with `ruff format` (implicit string concat) |
| `Q000–Q003` | Conflict with `ruff format` (quote style) |
| `W191` | Conflicts with `ruff format` (tab indentation) |
| `AIR`, `DJ`, `FAST`, `PD`, `NPY` | Framework-specific (Airflow, Django, FastAPI, pandas, NumPy) |
| `D` (pydocstyle) | Full docstring enforcement disabled for playground ergonomics |

Browse all available rules at <https://docs.astral.sh/ruff/rules/>.
