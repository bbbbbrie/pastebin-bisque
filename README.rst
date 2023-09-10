==============
✨ Overview ✨
==============

The Pastebin Bisque is a small Python utility that uses BeautifulSoup to scrape a user's `Pastebin`_ profile. All public pastes from that user are downloaded to disk. There is no rate-limiting protection built-in. Read about the `Pastebin Request Limits`_ if you anticipate generating a large number of requests. The file name provided by the Pastebin user will be prepended with the short URL that Pastebin provides. This allows a single directory with all pastes and no duplicates and makes the original URL fairly easy to reconstruct.

.. _Pastebin: https://pastebin.com/
.. _Pastebin Request Limits: https://pastebin.com/doc_scraping_api#2

TL;DR - Scrape all public Pastebin pastes from a user.

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

📦 Installation
===============

::

    pip install pastebin-bisque


📚 Documentation
================


https://pastebin-bisque.readthedocs.io/


💻 Development
==============

To run all the tests run::

    tox

Consider using this to run the tests in parallel:

    tox -p auto

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
