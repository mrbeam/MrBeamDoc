# coding=utf-8
from distutils.core import setup

import versioneer

exec (open('octoprint_mrbeamdoc/__version.py').read())

setup(name='MrBeamDoc',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description="""Provides documentation for Mr Beam Plugin""",
      author='Mr Beam',
      author_email='dev@mr-beam.org',
      url='https://github.com/mrbeam/MrBeamDoc',
      packages=['octoprint_mrbeamdoc'],
      package_dir={'octoprint_mrbeamdoc': 'octoprint_mrbeamdoc'},
      package_data={'octoprint_mrbeamdoc': ['docs/*']},
      install_requires=['enum34==1.1.10']
      )
