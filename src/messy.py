"""Messy demo module — intentionally terrible Python to exercise ruff ALL rules.

Run:  uv run ruff check src/messy.py
Fix:  uv run ruff check --fix src/messy.py
Fmt:  uv run ruff format src/messy.py

Each section is labelled with the ruff rule categories it triggers.
"""

import os
import sys
import os
import math, json
from os.path import (join, exists, dirname, basename)

import datetime
import collections
import re

from typing import Dict, List, Optional, Tuple, Union

x=1+2           
y = [1,2,3]     
z = {  'a': 1  }


class bad_class_name:          
    """A badly named class."""

    WRONG_constant = 42        
    myMixedCaseAttr = "oops"

    def BadMethodName(self):   
        """Bad method name."""
        return self.myMixedCaseAttr

    def __init__(Self):        
        """Init."""
        Self.value = 0


def mutable_default(items: list = []) -> list:
    """Append and return."""
    items.append(1)
    return items


def loop_variable_closure() -> list:
    funcs = []
    for i in range(5):
        funcs.append(lambda: i) 
    return funcs


def broad_exception() -> None:
    try:
        result = 1 / 0
    except:           
        pass
    try:
        result = 1 / 0  
    except Exception: 
        pass


def comprehension_smells() -> None:
    """Unnecessary use of list/dict/set calls."""
    _ = list([1, 2, 3])             
    _ = dict({"a": 1})              
    _ = set([x for x in range(5)])  
    _ = list(x for x in range(5))   
    _ = [i for i in [1, 2, 3] if i]  # fine, but next one isn't:
    _ = dict([(k, k * 2) for k in range(5)])


def simplify_me(flag: bool, value: Optional[int]) -> str:
    """Could be simplified."""
    if flag:
        result = "yes"
    else:
        result = "no"

    if flag:
        if value is not None:
            print("both true")

    try:
        int("not a number")
    except ValueError:
        pass

    d = {"a": 1}
    if "a" in d.keys():
        print("found")

    return result


def return_mess(x: int) -> Optional[int]:
    """Return statement issues."""
    if x > 0:
        return x
    else:              
        return None    


def early_return_candidate(items: List[int]) -> bool:  # UP006
    found = False
    for item in items:
        if item > 10:
            found = True
            break
    return found


def exception_antipatterns(path: str) -> str:
    """Various try/except smells."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise ValueError( 
            f"Could not open the file at {path!r} — are you sure it exists?"
        )

    try:
        data = json.loads("{bad}")
    except json.JSONDecodeError as exc:
        raise RuntimeError("parse failed") from exc  # fine, but below is not:

    raise ValueError("something went wrong")


def old_path_style(directory: str) -> list:
    """PTH — replace os.path calls with pathlib."""
    files = []
    for name in os.listdir(directory):          
        full = os.path.join(directory, name)    
        if os.path.isfile(full):                
            files.append(os.path.abspath(full)) 
    return files


def perf_issues() -> None:
    """Slow patterns ruff can flag."""
    result = []
    for i in range(100):
        result.append(i * 2)


    values = ["1", "2", "bad", "4"]
    parsed = []
    for v in values:
        try:                  
            parsed.append(int(v))
        except ValueError:
            parsed.append(0)


import logging

logger = logging.getLogger(__name__)


def logging_smells(user: str, count: int) -> None:
    """Bad logging patterns."""
    logger.info(f"User {user} logged in")             
    logger.warning("Count is: " + str(count))         
    logger.debug("Items: %s" % count)                 
    logger.error("Something broke: {}".format(user))  


# result = some_old_function(x, y)  
# if debug_mode:                    
#     print("DEBUG:", result)       


def naive_datetime() -> None:
    """DTZ — always use timezone-aware datetimes."""
    now = datetime.datetime.now()          
    today = datetime.date.today()          
    utcnow = datetime.datetime.utcnow()    
    _ = now, today, utcnow


def old_string_formatting(name: str, age: int) -> str:
    return "Hello, {}! You are {} years old.".format(name, age)


def type_annotation_old_style(
    items: Dict[str, List[int]],    
    mapping: Optional[Dict[str, Union[int, str]]] = None, 
) -> Tuple[int, ...]:                   
    """Old-style type hints."""
    _ = items, mapping
    return (1, 2, 3)


def unused_args(keep: int, throw_away: str, also_unused: float) -> int:
    return keep * 2


def boolean_trap(data: list, reverse: bool, unique: bool, sort: bool) -> list:
    if sort:
        data = sorted(data, reverse=reverse)
    if unique:
        data = list(set(data))
    return data


# ── C90: mccabe complexity ────────────────────────────────────────────────────
def overly_complex(a, b, c, d, e, f, g, h):
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
