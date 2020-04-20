dls_python3_template_module
===========================

|build_status| |coverage| |pypi_version| |readthedocs|

This is a template module for Python3 projects, containing recommended features
for code styling checks and versioning.

In order to disable these features, you will need to remove the
appropriate items from the list of [dev-packages] in the Pipfile,
as well as the corresponding sections and pytest flags in setup.cfg.

Changes to make:

- Write a README
- Write tests
- Write docs

Tests
-----

There are a set of tests in this template that are designed to fail if boilerplate
text hasn't been removed and some general information variables about this module
have not been changed.

Deploying to Pypi
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

For instructions on how to create a secure key, see this confluence page:
https://confluence.diamond.ac.uk/display/CNTRLS/Deploying+to+PyPi+using+Travis

Alternatively, there is a script that will automatically append this entire
deploy section to your .travis.yml, including generating a secure password
for your repository.


Documentation
-------------

Full documentation is available at http://dls_python3_template_module.readthedocs.io

Source Code
-----------

Available from http://github.com/dls-controls/dls_python3_template_module

Installation
------------

To start using this template::

    git clone https://github.com/dls-controls/dls_python3_template_module

Contributing
------------

See `CONTRIBUTING`_

License
-------
APACHE License. (see `LICENSE`_)


.. |build_status| image:: https://travis-ci.com/dls-controls/dls_python3_template_module.svg?branch=master
    :target: https://travis-ci.com/dls-controls/dls_python3_template_module
    :alt: Build Status

.. |coverage| image:: https://coveralls.io/repos/github/dls-controls/dls_python3_template_module/badge.svg?branch=master
    :target: https://coveralls.io/github/dls-controls/dls_python3_template_module?branch=master
    :alt: Test Coverage

.. |pypi_version| image:: https://badge.fury.io/py/dls_python3_template_module.svg
    :target: https://badge.fury.io/py/dls_python3_template_module
    :alt: Latest PyPI version

.. |readthedocs| image:: https://readthedocs.org/projects/dls_python3_template_module/badge/?version=latest
    :target: http://dls_python3_template_module.readthedocs.io
    :alt: Documentation

.. _CONTRIBUTING:
    https://github.com/dls-controls/dls_python3_template_module/blob/master/CONTRIBUTING.rst

.. _LICENSE:
    https://github.com/dls-controls/dls_python3_template_module/blob/master/LICENSE
