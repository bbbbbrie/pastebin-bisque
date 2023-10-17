#!/usr/bin/env python
import re
from pathlib import Path

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


setup(
    name="pastebin-bisque",
    version="1.0.0",
    license="LGPL-3.0-or-later",
    description="Scrape all public Pastebin pastes from a user.",
    long_description="{}\n{}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.rst")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    long_description_content_type="text/x-rst",
    author="Brie Carranza",
    author_email="hi@brie.ninja",
    url="https://github.com/bbbbbrie/pastebin-bisque",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[path.stem for path in Path("src").glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    project_urls={
        "📝 Documentation": "https://pastebin-bisque.readthedocs.io/",
        "🚀 Changelog": "https://pastebin-bisque.readthedocs.io/en/latest/changelog.html",
        "💡 Issue Tracker": "https://github.com/bbbbbrie/pastebin-bisque/issues",
    },
    keywords=["pastebin", "osint", "security", "research", "scraping"],
    python_requires=">=3.7",
    install_requires=[
        "loguru==0.7.1",
        "beautifulsoup4==4.12.2",
        "certifi==2023.7.22",
        "chardet==5.2.0",
        "charset-normalizer==3.2.0",
        "Click==8.1.7",
        "idna==3.4",
        "pathvalidate==3.1.0",
        "requests==2.31.0",
        "six==1.16.0",
        "soupsieve==2.5",
        "urllib3==2.0.7",
    ],
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=="2.6"": ["argparse"],
    },
    entry_points={
        "console_scripts": [
            "pastebin-bisque = pastebin_bisque.cli:main",
        ]
    },
)
