..  _contributing:

=======================================
💻 Contributing to `pastebin-bisque` 💻
=======================================

👋 Hello, world.  Contributions to `pastebin-bisque` are very welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

🐛 Bug Reports
==============

When reporting a bug please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

📚 Documentation Improvements
=============================

Documentation updates are welcome. That includes docstrings and links to blog posts or articles. Open `an issue <https://github.com/bbbbbrie/pastebin-bisque/issues>`_ to start discussing your ideas.

To make the changes directly, you'll want to run `pip install -r docs/requirements.txt` to set up the development dependencies for the docs. To build your changes into HTML that you can preview, do something like:

    sphinx-build   docs  /tmp/thedocs

You can then browse to `/tmp/thedocs` to view your changes in a browser.

💡 Feature Requests and Feedback
================================

The best way to send feedback is to file `an issue <https://github.com/bbbbbrie/pastebin-bisque/issues>`_.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

💻 Development
==============

To set up `pastebin-bisque` for local development:

1. Fork `pastebin-bisque <https://github.com/bbbbbrie/pastebin-bisque>`_
   (look for the "Fork" button).
2. Clone your fork locally

3. Install the development tools with one of these commands::

    pip install  bump2version check-manifest docutils isort pre-commit pygments readme-renderer
    python -I -m pip install check-manifest docutils isort pre-commit pygments readme-renderer

4. Set up the development tools with::

    pre-commit install

   This will ensure that `pre-commit run --all-files` runs as a pre-commit `hook <https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`_ using the `pre-commit <https://pre-commit.com/>`_ framework.

5. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

6. To do a quick test of your changes::

    python setup.py install
    rm $(which pastebin-bisque) && python setup.py install # subsequent runs

7. When you're done making changes run all the checks and docs builder with one command::

    tox

8. Commit your changes and push your branch to GitHub::

    git add .
    git commit -m "A brief description of a specific changes"
    git push origin name-of-your-bugfix-or-feature

9.  Submit a pull request through the GitHub website.

Releasing new versions
----------------------

Pushing a new patch version::

  pre-commit run --all-files &&  \
  git commit -am"✨ Add it all" && \
  bump2version patch && \
  git push --tags

Replace `patch` with `minor` or `major` as appropriate.

ℹ️ Pull Request Guidelines
--------------------------

If you need some code review or feedback while you're developing the code just make the pull request and ask `Brie <https://infosec.exchange/@brie>`_ to take a look.

To make it easier for your work to be reviewed and merged, you should:

1. Make sure that tests are passing (run ``tox``).
2. Update documentation as appropriate.
3. Add a note to ``CHANGELOG.rst`` describing the changes.
4. Add yourself to ``AUTHORS.rst``.

Don't let the perfect be the enemy of the good. Go ahead and `git commit` and `git push` so we can 🤝 get started.

💡 Tips
-------

To run a subset of tests::

    tox -e envname -- pytest -k test_myfeature

To run all the test environments in *parallel*::

    tox -p auto

For quick development::

   rm $(which pastebin-bisque) && python setup.py install && pastebin-bisque

Installing the current version from TestPyPI::

   pip install -i https://test.pypi.org/simple/ pastebin-bisque==$(grep ^current_version .bumpversion.cfg | cut -d"=" -f2 | cut -d" " -f2)  --extra-index-url https://pypi.org/simple

The `--extra-index-url https://pypi.org/simple` is important because the dependencies on TestPyPI are out-of-date or not present.

🔖 Bookmarks
------------

- `pip install <https://pip.pypa.io/en/stable/cli/pip_install/>`_

The source files for the `docs <https://pastebin-bisque.readthedocs.io/>`_ for `pastebin-bisque` are in `reStructured Text (RST) <https://docutils.sourceforge.io/rst.html>`_.

- `rst Cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_
- `Restructured Text (reST) and Sphinx CheatSheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
