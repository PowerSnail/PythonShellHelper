import typing as T
from pathlib import Path
import re

class Globals:
    cwd = Path(".").absolute()

def cd(p: str):
    Globals.cwd.joinpath(p).absolute()

def pwd() -> Path:
    return Globals.cwd

def ls(p: str = ".") -> T.List[Path]:
    path = Globals.cwd.joinpath(p)
    return [p for p in path.iterdir()]

def batch_rename(regex, name_template):
    r = re.compile(regex)
    for p in ls():
        match = r.match(p.name)
        if match is None:
            continue
        groups = match.groups()
        new_name = name_template.format(*groups)
        p.rename(p.parent.joinpath(new_name))  # TODO: name conflict
    