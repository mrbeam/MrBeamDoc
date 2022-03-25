# coding=utf-8

from setuptools import setup, find_packages

import versioneer

setup(name='MrBeamDoc',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description="""Provides documentation for Mr Beam Plugin""",
      author='Mr Beam',
      author_email='dev@mr-beam.org',
      url='https://github.com/mrbeam/MrBeamDoc',
      packages=find_packages(exclude=('test', '*.test', '*.test.*', 'test.*')),
      package_dir={'octoprint_mrbeamdoc': 'octoprint_mrbeamdoc'},
      package_data={'octoprint_mrbeamdoc': ['docs/*']},
      install_requires=['enum34==1.1.10']
      )
