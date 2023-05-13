#!/usr/bin/env python

from distutils.core import setup

setup(name='py_database',
      version='0.1',
      description='py_database with api',
      long_description='py_database with api for web',
      author='Geoloup Team',
      author_email='franckiebbb@gmail.com',
      packages=['py_database'],
)

import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()
setup(name="py_database", install_requires=install_requires)