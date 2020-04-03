Contributing
============

Contributions and issues are most welcome! All issues and pull requests are
handled through github on the `dls_controls repository`_. Also, please check for
any existing issues before filing a new one. If you have a great idea but it
involves big changes, please file a ticket before making a pull request! We
want to make sure you don't spend your time coding something that might not fit
the scope of the project.

.. _temporary_personal_repository: https://github.com/niamhdougan/dls_python3_template_module/issues

Running the tests
-----------------

To get the source source code and run the unit tests, run::

    $ git clone git://github.com/niamhdougan/dls_python3_template_module.git
    $ cd dls_python3_template_module
    $ pipenv install --dev
    $ pipenv run tests

While 100% code coverage does not make a library bug-free, it significantly
reduces the number of easily caught bugs! Please make sure coverage remains the
same or is improved by a pull request!

Code Styling
------------

The code in this repository conforms to standards set by the following tools:

- flake8_ for style checks
- flake8-black_ for code formatting
- flake8-isort_ for import ordering
- mypy_ for static type checking (for Python3.6+)

.. _flake8: http://flake8.pycqa.org/en/latest/
.. _flake8-isort: https://github.com/gforcada/flake8-isort
.. _flake8-black: https://github.com/peterjc/flake8-black
.. _mypy: https://github.com/python/mypy

These tests will be run on code when running ``pipenv run tests`` and also
automatically at check in. Please read the tool documentation for details
on how to fix the errors it reports.

In order to disable these features, you will need to remove the
appropriate items from the list of [dev-packages] in the Pipfile,
as well as the corresponding sections and pytest flags in setup.cfg.

Documentation
-------------

Documentation is contained in the ``docs`` directory and extracted from
docstrings of the API.

Docs follow the underlining convention::

    Headling 1 (page title)
    =======================

    Heading 2
    ---------

    Heading 3
    ~~~~~~~~~


You can build the docs from the project directory by running::

    $ pipenv run docs
    $ firefox build/html/index.html

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

Release Checklist
-----------------

Before a new release, please go through the following checklist:

* Add a release note in CHANGELOG.rst
* Git tag the version with message from CHANGELOG
* Push to github and travis will make a release on pypi
