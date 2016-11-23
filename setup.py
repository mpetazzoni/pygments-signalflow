#!/usr/bin/env python

# Copyright (C) 2016 Maxime Petazzoni <maxime.petazzoni@bulix.org>

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

with open('README.rst') as f:
    readme = f.read()

setup(
    name='pygments-signalflow',
    version='0.4',
    author='Maxime Petazzoni',
    author_email='maxime.petazzoni@bulix.org',
    description='Pygments lexer for SignalFlow',
    long_description=readme,
    license='Apache Software License v2',
    url='https://github.com/mpetazzoni/pygments-signalflow',
    zip_safe=True,
    packages=find_packages(),
    install_requires=requirements,
    entry_points="""
    [pygments.lexers]
    signalflow = pygments_signalflow:SignalFlowLexer
    """,
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
