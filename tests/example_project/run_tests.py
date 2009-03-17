#!/usr/bin/env python

'''
simple shortcut for running nosetests via python
replacement for *.bat or *.sh wrappers
'''

import os, sys
from os.path import dirname, join, pardir


# django settings module
DJANGO_SETTINGS_MODULE = 'example_project.settings'
# pythonpath dirs
PYTHONPATH = [
    join(dirname(__file__), pardir, pardir),
    join(dirname(__file__), pardir),
]


# inject few paths to pythonpath
for p in PYTHONPATH:
    if p not in sys.path:
        sys.path.insert(0, p)

# django needs this env variable
os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE

# TODO: ugly hack to inject required plugins to nose.run
sys.argv.insert(1, '--with-selenium')
sys.argv.insert(1, '--with-cherrypyliveserver')
sys.argv.insert(1, '--with-django')


import nose

nose.run(
    defaultTest=dirname(__file__),
)

