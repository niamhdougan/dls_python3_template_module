import os
import pytest


@pytest.fixture
def readme():
    readme_file = os.path.abspath("README.rst")
    with open(readme_file, 'r') as f:
        contents = f.read().replace('\n', ' ')
    return contents


@pytest.fixture
def setupcfg():
    import configparser

    conf = configparser.ConfigParser()
    conf.read("setup.cfg")

    return conf['metadata']


@pytest.fixture
def doc_confpy():
    from docs import conf

    return conf.project, conf.copyright, conf.author


@pytest.fixture
def doc_index():
    indexrst = os.path.abspath("docs/index.rst")
    with open(indexrst, 'r') as f:
        contents = f.read().replace('\n', ' ')
    return contents


@pytest.fixture
def doc_api():
    apirst = os.path.abspath("docs/reference/api.rst")
    with open(apirst, 'r') as f:
        contents = f.read().replace('\n', ' ')
    return contents


# README
def test_changed_README(readme):
    if "dls_python3_template_module" in readme:
        assert False, "Please change the README to include information "\
            "about your module."


# setup.cfg
def test_module_name(setupcfg):
    assert setupcfg['name'] != 'dls_python3_template_module', \
        "Did you remember to change the module name in setup.cfg?"


def test_module_description(setupcfg):
    assert setupcfg['description'] != \
        'Python3 template including some recommended code styling',\
        "Please write a description for your module."


def test_module_url(setupcfg):
    assert setupcfg['url'] != \
        'https://github.com/niamhdougan/dls_python3_template_module',\
        "Please add a URL for your module repo."


def test_module_author_set(setupcfg):
    if setupcfg['author'] in setupcfg:
        assert setupcfg['author'] != 'Author',\
            "Please add an author."


def test_module_author_email_set(setupcfg):
    if setupcfg['author_email'] in setupcfg:
        assert setupcfg['author_email'] != 'author@diamond.ac.uk',\
            "Please add an author email."


# Docs
def test_docs_index_changed(doc_index):
    assert "dls_python3_template_module" not in doc_index, \
        "Change the documentation in docs/index.rst"


def test_docs_ref_api_changed(doc_api):
    assert "dls_python3_template_module" not in doc_api, \
        "Change the module name in docs/reference/api.rst"


def test_docs_conf_project_changed(doc_confpy):
    if "dls_python3_template_module" in doc_confpy:
        assert False, "Please change the project name in docs/conf.py"


def test_docs_conf_correct_year(doc_confpy):
    import datetime
    thisyear = datetime.datetime.now().year
    if str(thisyear) not in str(doc_confpy):
        assert False, "Please state the correct year in docs/conf.py"


def test_docs_conf_author_changed(doc_confpy):
    if "author" in doc_confpy:
        assert False, "Please change the author in docs/conf.py"
