import os
from pathlib import Path
from typing import Union


def relative_path(base_path:Union[str,Path], relative_path:Union[str,Path]) -> str:
    """Returns the relative path from base path to relative_path
    even when relative_path is not a subdirectory of base_path.

    Args:
        base_path (str|Path): Base for relative path
        relative_path (str|Path): File or Directory that the relative path points to.

    Returns:
        str: relative path to access 'relative_path' from 'base_path'
    """
    base = Path(base_path).absolute()
    rel = Path(relative_path).absolute()

    if not base.is_dir():
        base = base.parent

    common = ""
    idx = 0
    while (idx < min(len(base.parts), len(rel.parts))) and (
          str(base.parts[idx]) == str(rel.parts[idx])
    ):
        if len(common) > 0 and (common[-1] != os.sep):
            common += os.sep
        common += base.parts[idx]
        idx += 1

    diff_len = len(base.parts) - len(Path(common).parts)
    res = ""
    for dummy in range(0, diff_len):
        res += ".." + os.sep
    ofs = 0
    if str(rel) == str(common):
        return res
    if len(res) > 0 and res[-1] == os.sep and str(rel)[len(str(common))] == os.sep:
        ofs = 1
    elif len(res) == 0:
        ofs = 1
    res += str(rel)[len(str(common))+ofs :]
    return res
