from setuptools import setup

setup(
    name='issh',
    version='1.0.0',
    description='Improved SSH: TUI menu for connecting to SSH config hosts',
    long_description=open('README.md').read(),
    url='https://github.com/DevDungeon/issh',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    modules=['issh'],
    scripts=[
        'bin/issh',
        'bin/issh.bat',
    ],
    zip_safe=False,
    install_requires=[
        'windows-curses',
    ],
)
