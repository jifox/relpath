from pathlib import Path
import sys

sys.path.append(str(Path(Path(__file__).parent).parent))

import pytest
import os
from relpath import relative_path


def test_relative_path():
    testdir = str(Path(__file__).parent) + os.sep
    testdata = [
        {
            "bas": str(Path(testdir).joinpath("dir1", "dir2")),
            "rel": str(Path(testdir).joinpath("dir4", "test.txt")),
            "res": str(Path("..").joinpath("..", "dir4", "test.txt")),
        },
        {
            "bas": testdir,
            "rel": str(Path(testdir).joinpath("dir4", "test.txt")),
            "res": str(Path("dir4").joinpath("test.txt")),
        },
        {
            "bas": str(Path(testdir).joinpath("dir1", "non-existing-filename")),
            "rel": str(Path(testdir).joinpath("dir4", "test.txt")),
            "res": str(Path("..").joinpath("dir4", "test.txt")),
        },
        {
            "bas": "/home",
            "rel": "/",
            "res": "../",
        },
    ]

    for dat in testdata:
        print("")
        print("bas:", dat.get("bas"))
        print("rel:", dat.get("rel"))
        print("res:", dat.get("res"))
        res = relative_path(dat.get("bas"), dat.get("rel"))
        assert str(res) == str(dat.get("res"))
