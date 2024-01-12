# -*- coding: utf-8 -*-

import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

with open('requirements.txt') as file:
    requirements = [line.strip() for line in file.readlines() if not line.startswith('git+')]

setuptools.setup(
    name=' CRIMAC-preprocessing',
    packages=setuptools.find_packages(),
    install_requires=requirements,
)