#!/usr/bin/env python

from setuptools import setup

setup(name='jdlangtranslator',
      version='1.0',
      description='jdLangTranslator',
      author='JakobDev',
      author_email='jakobdev@gmx.de',
      url='https://gitlab.com/JakobDev/jdLangTranslator',
      include_package_data=True,
      packages=['src'],
      entry_points={
          'console_scripts': ['jdLangTranslator = src.jdLangTranslator:main']
          },
     )
