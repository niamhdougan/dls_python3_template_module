import os
import pytest


@pytest.fixture
def setupcfg():
    import configparser

    conf = configparser.ConfigParser()
    conf.read("setup.cfg")

    return conf['metadata']


@pytest.fixture
def readme():
    readme_file = os.path.abspath("README.rst")
    with open(readme_file, 'r') as f:
        contents = f.read().replace('\n', ' ')
    return contents

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
        assert setupcfg['author'] != 'None',\
            "Please add an author."


def test_module_author_email_set(setupcfg):
    if setupcfg['author_email'] in setupcfg:
        assert setupcfg['author_email'] != 'None',\
            "Please add an author email."


# Docs
def test_docs_boilerplate_removed():
    pass


def test_docs_conf_general_info_changed():
    pass


# README
def test_changed_README(readme):
    if "dls_python3_template_module" in readme:
        assert False, "Please change the README to include information"\
            "about your module."
