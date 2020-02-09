from setuptools import setup
from sys import platform

requirements = []
if platform == "win32":
    requirements.append('windows-curses')

setup(
    name='issh',
    version='1.3.1',
    description='Improved SSH: TUI menu for connecting to SSH config hosts',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    url='https://github.com/DevDungeon/issh',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    py_modules=['issh'],
    entry_points={
        'console_scripts': [
            'issh = issh:main',
        ],
    }
    ,
    zip_safe=False,
    install_requires=[
        requirements,
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
