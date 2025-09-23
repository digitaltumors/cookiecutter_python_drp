Welcome to {{ cookiecutter.project_name }}'s documentation!
================================================================

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}


{% if is_open_source %}
|a| |b| |c|

.. |a| image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. |b| image:: https://app.travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://app.travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. |c| image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Source code: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
{% endif %}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   modules
   developer
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
