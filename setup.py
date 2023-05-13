#!/usr/bin/env python

from distutils.core import setup
import os
os.system('pip install flask')
os.system('pip install flask_cors')
os.system('pip install asyncio')

setup(name='py_database',
      version='0.1',
      description='py_database with api',
      long_description='py_database with api for web',
      author='Geoloup Team',
      author_email='franckiebbb@gmail.com',
      packages=['py_database'],
)

