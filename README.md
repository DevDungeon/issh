# issh

[![PyPI version](https://badge.fury.io/py/issh.svg)](https://pypi.org/project/issh/)

Improved SSH launcher that provides a browsable
menu of SSH servers. Uses `~/.ssh/config`
to generate menu.

![Screenshot](screenshots/screenshot1.png)

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

If uses Windows, also install `windows-curses` (included in setup.py).

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

If you have permission errors with the `~/.ssh/config` file,
make sure the `.ssh/` directory has `700` permissions and
the `config` file has `644` permissions. Also ensure
the owner is correct.

## Author

NanoDano <nanodano@devdungeon.com>
