# encoding: utf-8

from setuptools import find_packages, setup


setup(name='search_counter',
      description='A toolkit for matching term frequency with keyword search volume',
      author='Derek Hawkins',
      author_email='derekhawkinsmail@gmail.com',
      version='0.0.1',
      license='MIT',
      packages=find_packages(),
      keywords='data analysis keyword research google seo',
      install_requires=[
          'pandas>=0.25.1',
          'nltk>=3.4.5',
          're>=2.2.1'
      ],
      test_suite='tests'
      )
