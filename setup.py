#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.1'


def get_requirements(env):
    with open('requirements_%s.txt' % env) as file:
        return [x for x in file.read().split('\n') if not x.startswith('#')]


install_requires = get_requirements('base')
dev_requires = get_requirements('dev')

setup(
    name='PyREST',
    version=version,
    description="""Rest server for FroxyProject project""",
    long_description="""Rest server for FroxyProject project""",
    author='0ddlyoko',
    author_email='0ddlyokoOfficial@gmail.com',
    url='https://github.com/FroxyProject/PyREST',
    install_requires=install_requires,
    extras_require={"dev": dev_requires},
    license='MIT',
    packages=[
        'pyrest'
    ],
    include_package_data=True,
    keywords='PyREST',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django CMS :: 3.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
