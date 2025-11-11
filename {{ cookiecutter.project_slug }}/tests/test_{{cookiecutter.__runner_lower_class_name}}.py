#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""
import os
import tempfile
import shutil
import aixport.constants
from {{ cookiecutter.project_slug }}.exceptions import {{ cookiecutter.__error_class_name }}

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}
from {{ cookiecutter.project_slug }}.runner import {{ cookiecutter.__runner_class_name }}
{%- if cookiecutter.use_pytest == 'y' %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- else %}


class Test{{ cookiecutter.__runner_class_name|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = {{ cookiecutter.__runner_class_name }}({'outdir': 'foo',
                                                        'skip_logging': True,
                                                        'mode': aixport.constants.TRAIN_MODE})

        self.assertIsNotNone(myobj)

    def test_run_predict(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = {{cookiecutter.__runner_class_name}}({'outdir': os.path.join(temp_dir, 'foo'),
                                                         'skip_logging': True,
                                                         'mode': aixport.constants.PREDICT_MODE})
            self.assertEqual(0, myobj.run())
        finally:
            shutil.rmtree(temp_dir)

    def test_run_test(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = {{cookiecutter.__runner_class_name}}({'outdir': os.path.join(temp_dir, 'foo'),
                                                         'skip_logging': True,
                                                         'mode': aixport.constants.TEST_MODE})
            self.assertEqual(0, myobj.run())
        finally:
            shutil.rmtree(temp_dir)

    def test_run_train(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = {{cookiecutter.__runner_class_name}}({'outdir': os.path.join(temp_dir, 'foo'),
                                                         'skip_logging': True,
                                                         'mode': aixport.constants.TRAIN_MODE})
            self.assertEqual(0, myobj.run())
        finally:
            shutil.rmtree(temp_dir)

    def test_run_optimizetrain(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = {{cookiecutter.__runner_class_name}}({'outdir': os.path.join(temp_dir, 'foo'),
                                                         'skip_logging': True,
                                                         'mode': aixport.constants.OPTIMIZETRAIN_MODE})
            self.assertEqual(0, myobj.run())
        finally:
            shutil.rmtree(temp_dir)

    def test_run_invalidmode(self):
        """ Tests run()"""
        temp_dir = tempfile.mkdtemp()
        try:
            myobj = {{cookiecutter.__runner_class_name}}({'outdir': os.path.join(temp_dir, 'foo'),
                                                         'skip_logging': True,
                                                         'mode': 'invalid'})
            myobj.run()
            self.fail('Expected exception')
        except {{ cookiecutter.__error_class_name }} as e:
            self.assertTrue('Unsupported mode: ' in str(e))
        finally:
            shutil.rmtree(temp_dir)

{%- endif %}
