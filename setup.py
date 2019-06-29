#!/usr/bin/env python

from setuptools import setup

setup(name='jslangtranslator',
      version='1.0',
      description='jdLangTranslator',
      author='JakobDev',
      author_email='jakobdev@gmx.de',
      url='https://gitlab.com/JakobDev/jdLangTranslator',
      py_modules=['jdLangTranslator'],
      entry_points={
          'console_scripts': ['jdLangTranslator = jdLangTranslator:main']
          },
      data_files=[
          ('translation', ['translation/de_DE.lang', 'translation/en_GB.lang']),
          ],
     )
