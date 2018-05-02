#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click',
    'bs4',
    'lxml',
    'unicodecsv',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='hx_util',
    version='0.1.0',
    description="batch tools for edx course exporws",
    long_description=readme,
    author="Colin Fredericks",
    author_email='colin_fredericks@harvard.edu',
    url='https://github.com/Colin_Fredericks/hx_util',
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': [
            'hx_util=hx_util.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='hx_util hx edx course_export',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
