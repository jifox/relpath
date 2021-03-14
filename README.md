# [relpath](https://github.com/jifox/relpath.git) - relative path module

![Python package](https://github.com/jifox/relpath/actions/workflows/python-package.yml/badge.svg)  [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

This module `relpath` eliminates the weakness of pathlib.Path
that a Valuen error no relative path will be returned if the
directory is not a subdirectory of the base Path.

## Installation

```bash
pip install relpath
```

## Example for error:

```python
from pathlib import Path

base="/home"
rel="/"

# Error when using Path
Path(rel).relative_to(base)

Exception has occurred: ValueError
'/' does not start with '/home'
```

## Example using relpath module:

```python
from relpath import relative_path

base="/home"
rel="/"

print(relative_path(base, rel))
../
```

## Support

If you find any problems with relpath module, please report them to GitHub, and I will respond when possible. Code contributions are always welcome, and ideas for new modules, or additions to existing modules, are also appreciated.
