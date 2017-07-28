# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='colorharmonies',
      version='0.1',
      description='Library to generate all your color harmonies with simplicity',
      url='https://github.com/baptistemanteau/colorharmonies',
      author='Baptiste Manteau',
      author_email='baptiste.manteau@allegorithmic.com',
      license='MIT',
      packages=['colorharmonies'],
      python_requires='>=3',
      install_requires=[
          'colorsys',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)