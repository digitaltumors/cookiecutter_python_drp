import re
import sys
import requests


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)



    #Exit to cancel project
    sys.exit(1)

prodpypi_url = 'https://pypi.org/pypi/' + module_name + '/json'

resp = requests.get(prodpypi_url, timeout=30)

if resp.status_code == 200:
    print('ERROR: The project slug ' + module_name +
          ' already exists on Production Pypi (' + prodpypi_url +
          ') Please use a different name')
    sys.exit(2)

testpypi_url = 'https://test.pypi.org/pypi/' + module_name + '/json'
resp = requests.get(testpypi_url, timeout=30)

if resp.status_code == 200:
    print('ERROR: The project slug ' + module_name +
          ' already exists on Test Pypi (' + testpypi_url +
          ') Please use a different name')
    sys.exit(3)

