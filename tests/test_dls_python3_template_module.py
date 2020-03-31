import configparser
import pytest


class Setupcfg():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('setup.cfg')
        self.meta = self.conf['metadata']

    def test_module_name(self): 
        assert self.meta['name']!='dls_python3_template_module', \
            "Did you remember to change the module name in setup.cfg?"

    def test_module_description(self):
        assert self.meta['description']!=\
            'Tool for adding version from git to a python project without adding dependencies',\
            "Please write a description for your module."

    def test_module_url(self):
        assert self.meta['url']!='https://github.com/dls-controls/versiongit',\
            "Please add a URL for your module repo."

    def test_module_author(self):
        if self.meta['author'] in self.meta:
            assert self.meta['author']!= 'None',\
                "Please add an author or remove this line from setup.cfg"

    def test_module_author_email(self):
        if self.meta['author_email'] in self.meta:
            assert self.meta['author_email']!= 'None',\
                "Please add an author email or remove this line from setup.cfg"


# Docs

def test_docs_boilerplate_removed():
    pass

def test_docs_conf_general_info_changed():
    pass

# README

def test_changed_README():
    pass

