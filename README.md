# ✨ Overview ✨

The Pastebin Bisque is a small Python utility that uses BeautifulSoup to scrape a user's [Pastebin](https://pastebin.com/) profile. All public pastes from that user are downloaded to disk. Optionally, the pastes can be saved to a single `.zip` file.

There is no rate-limiting protection built-in. Read about the [Pastebin Request Limits](https://pastebin.com/doc_scraping_api#2) if you anticipate generating a large number of requests. The file name provided by the Pastebin user will be prepended with the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL fairly easy to reconstruct.

TL;DR - Scrape all public Pastebin pastes from a user.

Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

## 📦 Installation

    pip install pastebin-bisque

Learn more on [PyPI](https://pypi.org/project/pastebin-bisque/).

## ℹ️ Usage

    pastebin-bisque

Specify a username:

    pastebin-bisque --username catstestingcode

Zip the results:

    pastebin-bisque -z

Download all of the public pastes for the `catstestingcode` user and save them in a `.zip` file:

    pastebin-bisque --username catstestingcode -z

## 📚 Documentation

The documentation for `pastebin-bisque` is served via [Read the Docs](https://readthedocs.org) and is available at:

<https://pastebin-bisque.readthedocs.io/>

## 💻 Development

🙏 Thanks for your interest in contributing to the development (and documentation) of `pastebin-bisque`. See the notes on [contributing](CONTRIBUTING.md) to learn more.

### 🧪 Tests

This project uses [GitLab CI](https://docs.gitlab.com/ee/ci/), [tox](https://tox.wiki/en/4.11.3/) and [Test PyPI](https://packaging.python.org/en/latest/guides/using-testpypi/) for testing. See `tests/test_pastebin_bisque.py`.

#### 🏡 Local

To run all the tests run:

    tox

Consider using this to run the tests in parallel:

> tox -p auto

Note, to combine the coverage data from all the tox environments:

##### Windows 

```shell
set PYTEST_ADDOPTS=--cov-append
tox
```

##### Other Platforms

```shell
PYTEST_ADDOPTS=--cov-append tox
```

#### 💚 CI

See `.gitlab-ci.yml` for the tests that are performed via GitLab CI. You'll need to be a Maintainer to run the tests that interact with Test PyPI (or to release a new package to PyPI).
