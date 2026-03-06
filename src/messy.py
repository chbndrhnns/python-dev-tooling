"""Messy demo module — intentionally terrible Python to exercise ruff ALL rules.

Run:  uv run ruff check src/messy.py
Fix:  uv run ruff check --fix src/messy.py
Fmt:  uv run ruff format src/messy.py

Each section is labelled with the ruff rule categories it triggers.
"""

# ── F: Pyflakes ───────────────────────────────────────────────────────────────
import os          # F401 — imported but unused (after we shadow it below)
import sys
import os          # F811 — redefinition of unused 'os' from import
import math, json  # E401 — multiple imports on one line
from os.path import (join, exists, dirname, basename)  # F401 — some unused

# ── I: isort — imports out of order ──────────────────────────────────────────
import datetime
import collections
import re

# ── UP: pyupgrade — old-style Python patterns ────────────────────────────────
from typing import Dict, List, Optional, Tuple, Union   # UP035 — use built-ins

# ── E/W: pycodestyle ─────────────────────────────────────────────────────────
x=1+2           # E225 — missing whitespace around operator
y = [1,2,3]     # E231 — missing whitespace after ','
z = {  'a': 1  }  # E201/E202 — whitespace inside braces


# ── N: pep8-naming ────────────────────────────────────────────────────────────
class bad_class_name:          # N801 — class name should be CapWords
    """A badly named class."""

    WRONG_constant = 42        # N803 — constant should be UPPER_CASE (if meant as one)
    # N815 — mixedCase variable in class scope
    myMixedCaseAttr = "oops"

    def BadMethodName(self):   # N802 — method name should be lowercase
        """Bad method name."""
        return self.myMixedCaseAttr

    def __init__(Self):        # N803 — argument 'Self' should be lowercase 'self'
        """Init."""
        Self.value = 0


# ── B: flake8-bugbear ─────────────────────────────────────────────────────────
def mutable_default(items: list = []) -> list:  # B006 — mutable default argument
    """Append and return."""
    items.append(1)
    return items


def loop_variable_closure() -> list:
    """B023 — loop variable used in lambda inside loop."""
    funcs = []
    for i in range(5):
        funcs.append(lambda: i)  # B023 — captures loop var by reference
    return funcs


def broad_exception() -> None:
    """B001/BLE001 — blind except clause."""
    try:
        result = 1 / 0
    except:             # E722/BLE001 — bare except
        pass
    try:
        result = 1 / 0  # noqa: F841
    except Exception:   # BLE001 — too broad
        pass


# ── C4: flake8-comprehensions ─────────────────────────────────────────────────
def comprehension_smells() -> None:
    """Unnecessary use of list/dict/set calls."""
    _ = list([1, 2, 3])             # C411 — unnecessary list()
    _ = dict({"a": 1})              # C418 — unnecessary dict()
    _ = set([x for x in range(5)])  # C401 — set() around a list comprehension → use set comprehension
    _ = list(x for x in range(5))   # C400 — generator inside list() → use list comprehension
    _ = [i for i in [1, 2, 3] if i]  # fine, but next one isn't:
    _ = dict([(k, k * 2) for k in range(5)])  # C416 — unnecessary dict comprehension


# ── SIM: flake8-simplify ──────────────────────────────────────────────────────
def simplify_me(flag: bool, value: Optional[int]) -> str:  # UP007 → int | None
    """Could be simplified."""
    # SIM108 — ternary instead of if/else
    if flag:
        result = "yes"
    else:
        result = "no"

    # SIM102 — nested if → single if with and
    if flag:
        if value is not None:
            print("both true")

    # SIM105 — use contextlib.suppress instead of try/except/pass
    try:
        int("not a number")
    except ValueError:
        pass

    # SIM118 — use `key in dict` instead of `key in dict.keys()`
    d = {"a": 1}
    if "a" in d.keys():  # SIM118
        print("found")

    return result  # noqa: F821 — result might be unbound (it's not, but demo)


# ── RET: flake8-return ────────────────────────────────────────────────────────
def return_mess(x: int) -> Optional[int]:  # UP007
    """Return statement issues."""
    if x > 0:
        return x
    else:              # RET505 — superfluous else after return
        return None    # RET501 — explicit return None unnecessary


def early_return_candidate(items: List[int]) -> bool:  # UP006
    """RET504 — unnecessary assignment before return."""
    found = False
    for item in items:
        if item > 10:
            found = True
            break
    return found


# ── TRY: tryceratops ─────────────────────────────────────────────────────────
def exception_antipatterns(path: str) -> str:
    """Various try/except smells."""
    # TRY003 — long message in raise
    try:
        with open(path) as f:  # noqa: PTH123 — PTH flagged separately
            return f.read()
    except FileNotFoundError:
        raise ValueError(  # TRY003 — long inline message; TRY200 — use raise..from
            f"Could not open the file at {path!r} — are you sure it exists?"
        )

    # TRY301 — abstract raise to an inner function
    try:
        data = json.loads("{bad}")
    except json.JSONDecodeError as exc:
        raise RuntimeError("parse failed") from exc  # fine, but below is not:

    # EM101 — string literal in exception
    raise ValueError("something went wrong")  # EM101


# ── PTH: flake8-use-pathlib ───────────────────────────────────────────────────
def old_path_style(directory: str) -> list:
    """PTH — replace os.path calls with pathlib."""
    files = []
    for name in os.listdir(directory):          # PTH208
        full = os.path.join(directory, name)    # PTH118
        if os.path.isfile(full):                # PTH113
            files.append(os.path.abspath(full)) # PTH100
    return files


# ── PERF: Perflint — performance anti-patterns ───────────────────────────────
def perf_issues() -> None:
    """Slow patterns ruff can flag."""
    # PERF401 — manual list accumulation instead of list comprehension
    result = []
    for i in range(100):
        result.append(i * 2)  # PERF401

    # PERF203 — try/except in a loop
    values = ["1", "2", "bad", "4"]
    parsed = []
    for v in values:
        try:                   # PERF203
            parsed.append(int(v))
        except ValueError:
            parsed.append(0)


# ── G: flake8-logging-format ─────────────────────────────────────────────────
import logging

logger = logging.getLogger(__name__)


def logging_smells(user: str, count: int) -> None:
    """Bad logging patterns."""
    # G001/G002 — use % formatting or lazy %, not f-string/str.format
    logger.info(f"User {user} logged in")             # G004 — f-string in logging
    logger.warning("Count is: " + str(count))         # G003 — string concat in logging
    logger.debug("Items: %s" % count)                 # G002 — % operator in log call
    logger.error("Something broke: {}".format(user))  # G001 — .format() in log call


# ── ERA: eradicate — commented-out code ──────────────────────────────────────
# result = some_old_function(x, y)   # ERA001
# if debug_mode:                     # ERA001
#     print("DEBUG:", result)        # ERA001


# ── DTZ: flake8-datetimez ────────────────────────────────────────────────────
def naive_datetime() -> None:
    """DTZ — always use timezone-aware datetimes."""
    now = datetime.datetime.now()          # DTZ005 — missing tz=
    today = datetime.date.today()          # DTZ011
    utcnow = datetime.datetime.utcnow()    # DTZ003 — deprecated, use now(UTC)
    _ = now, today, utcnow


# ── FLY: flynt — f-string conversion ─────────────────────────────────────────
def old_string_formatting(name: str, age: int) -> str:
    """FLY001 — .format() calls that should be f-strings."""
    return "Hello, {}! You are {} years old.".format(name, age)  # FLY001


# ── UP: pyupgrade — more old patterns ────────────────────────────────────────
def type_annotation_old_style(
    items: Dict[str, List[int]],          # UP006/UP035 — use dict/list
    mapping: Optional[Dict[str, Union[int, str]]] = None,  # UP007/UP035
) -> Tuple[int, ...]:                     # UP006/UP035 — use tuple
    """Old-style type hints."""
    _ = items, mapping
    return (1, 2, 3)


# ── ARG: unused arguments ─────────────────────────────────────────────────────
def unused_args(keep: int, throw_away: str, also_unused: float) -> int:
    """ARG001 — unused function arguments."""
    return keep * 2


# ── FBT: flake8-boolean-trap ─────────────────────────────────────────────────
def boolean_trap(data: list, reverse: bool, unique: bool, sort: bool) -> list:  # FBT001/FBT002
    """FBT — boolean positional arguments are a trap."""
    if sort:
        data = sorted(data, reverse=reverse)
    if unique:
        data = list(set(data))
    return data


# ── C90: mccabe complexity ────────────────────────────────────────────────────
def overly_complex(a, b, c, d, e, f, g, h):  # PLR0913 — too many args; C901 complexity
    """This function has cyclomatic complexity > 10."""
    result = 0
    if a:
        if b:
            if c:
                result += 1
            elif d:
                result += 2
            else:
                result += 3
        elif e:
            if f:
                result -= 1
            else:
                result -= 2
        else:
            result += 10
    elif g:
        if h:
            result *= 2
        else:
            result //= 2
    else:
        result = -1
    return result


# ── TODO comments (TD) ────────────────────────────────────────────────────────
# TODO: refactor this entire module once the team agrees on style  # TD001


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("violations detected above — run `uv run ruff check src/messy.py` to see them all")
    print(sys.version)
