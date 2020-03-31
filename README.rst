dls_python3_template_module
===========================

|build_status| |coverage| |pypi_version| |readthedocs|

This template contains recommended features for Python3 modules 
including versiongit - a tool for managing versioning, as well 
as various code styling checks.

When pushing your repo, this module will perform the following 
checks on your code, tests and documentation:

- flake8_ for style checks
- flake8-black_ for code formatting
- flake8-isort_ for import ordering
- mypy_ for static type checking

In order to disable these features, you will need to remove the
appropriate items from the list of [dev-packages] in the Pipfile, 
as well as the corresponding sections in setup.cfg.
.. Note::
    To remove all checks, delete the [isort] and [flake8]
    sections as well as the --flake8 and --mypy flags from the
    pytest section.


Deploying to pypi
-----------------

You will need to add the following to the end of the module's .travis.yml file.

.. code-block:: yaml

    deploy:
      provider: pypi
      username: {username}
      password:
        secure: {secure_password}
      # Only deploy if something else in the matrix hasn't already done the sdist/wheel
      skip_existing: true
      on:
        tags: true
      # opt in to dpl v2
      edge: true

For instructions on how to create a secure key, 
There is a script that will automatically append this entire deploy
section to your .travis.yml, including generating a secure
password for your repository.  


.. |build_status| image:: https://travis-ci.org/dls-controls/versiongit.svg?branch=master
    :target: https://travis-ci.org/dls-controls/versiongit
    :alt: Build Status

.. |coverage| image:: https://coveralls.io/repos/github/dls-controls/versiongit/badge.svg?branch=master
    :target: https://coveralls.io/github/dls-controls/versiongit
    :alt: Test coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/versiongit.svg
    :target: https://pypi.python.org/pypi/versiongit
    :alt: Latest PyPI version

.. |readthedocs| image:: https://readthedocs.org/projects/versiongit/badge/?version=latest
    :target: http://versiongit.readthedocs.org
    :alt: Documentation

.. _LICENSE:
    https://github.com/niamhdougan/dls_python3_template_module/blob/master/LICENSE
