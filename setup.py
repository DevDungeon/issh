from setuptools import setup
from sys import platform

scripts = ['bin/issh']
requirements = []

if platform == "win32":
    requirements.append('windows-curses')
    scripts.append('bin/issh.bat')

setup(
    name='issh',
    version='1.1.1',
    description='Improved SSH: TUI menu for connecting to SSH config hosts',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/DevDungeon/issh',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    py_modules=['issh'],
    scripts=scripts,
    zip_safe=False,
    install_requires=[
        requirements,
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
