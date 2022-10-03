from setuptools import setup
import pathlib
import re

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

version = ''
with open('dipshit/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(
    name="dipshit",
    version=version,
    description="a shitty brainfuck inspired esolang, implemented in python.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="anytarseir67",
    url="https://github.com/anytarseir67/dipshit",
    license="GPLv3",
    packages=["dipshit"],
    include_package_data=True,
    entry_points={
        "console_scripts": ["dipshit=dipshit.__main__:main"],
    },
    extras_require={
        'docs': [
            'sphinx',
            'sphinxcontrib_trio',
            'sphinxcontrib-websupport',
            'typing-extensions',
            'myst_parser'
        ],
    },
)
