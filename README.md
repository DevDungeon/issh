# issh

[![PyPI version](https://badge.fury.io/py/issh.svg)](https://badge.fury.io/py/issh)

Improved SSH launcher that provides a browsable
menu of SSH servers. Uses `~/.ssh/config`
to generate menu.

## Install

Install from pypi.org using:

```bash
python -m pip install issh
```

Install from source by running this from
the root of the source code directory:

```bash
python setup.py install
```

If uses Windows, also install `windows-curses`.

```bash
python -m pip install windows-curses
```

## Usage

Simply run `issh` from the command line to launch
the menu.

```bash
issh
# or
python -m issh
```

## Author

NanoDano <nanodano@devdungeon.com>
