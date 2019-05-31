# issh

[![PyPI version](https://badge.fury.io/py/issh.svg)](https://pypi.org/project/issh/)

Improved SSH launcher that provides a browsable
menu of SSH servers. Uses `~/.ssh/config`
to generate menu.

![Works in Windows, Mac, Linux](screenshots/screenshot1.png)

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

## Usage

Simply run `issh` from the command line to launch
the menu.

```bash
issh
```

Or invoke via Python:

```bash
python -m issh
```

To use the tool inside PYthon source code:

```python
from issh import ISSH

issh = ISSH()
issh.run()
```


## Troubleshooting

If you have permission errors with the `~/.ssh/config` file,
make sure the `.ssh/` directory has `700` permissions and
the `config` file has `600` permissions. Also ensure
the owner is correct.

## Author

NanoDano <nanodano@devdungeon.com>
