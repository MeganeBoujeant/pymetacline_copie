"""
The pymetacline package.

A set of tools written in Python to administrate the MetaCline database (for pedagogic purposes only).
"""

# -------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------

import sys
import re
from setuptools import setup

# -------------------------------------------------------------------------
# Informations about the project including trove classifiers
# -------------------------------------------------------------------------


author = 'M2 bioinfo, AMU'
email = 'some.address@univ-amu.fr'
description = 'A set of tools written in Python to administrate the MetaCline database (for pedagogic purposes only).'
license = 'MIT'
url = 'https://github.com/dputhier/pymetacline'
url_source = 'https://github.com/dputhier/pymetacline'
url_tracker = 'https://github.com/dputhier/pymetacline'
keywords = 'genomics bioinformatics'
python_requires = '>=3.5'
classifiers = ("License :: OSI Approved :: MIT License",
                   "Operating System :: MacOS",
                   "Operating System :: POSIX :: Linux",
                   "Environment :: Console",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",                   
                   "Intended Audience :: Science/Research",
                   "Natural Language :: English",
                   "Topic :: Scientific/Engineering :: Bio-Informatics",
                   "Operating System :: POSIX :: Linux",
                   "Operating System :: MacOS",
                   "Topic :: Documentation :: Sphinx"
                   )

# -------------------------------------------------------------------------
# Printing Python version
# -------------------------------------------------------------------------

sys.stderr.write('Python version : ' + str(sys.version_info) + '\n')
sys.stderr.write('Python path : ' + str(sys.prefix) + '\n')

# -------------------------------------------------------------------------
# Check pymetacline version
# -------------------------------------------------------------------------

version = open("pymetacline/version.py").readlines()[0]
version = version.split("=")[1]
version = re.sub("['\" \n\r]", "", version)
        
# ----------------------------------------------------------------------
# Description
# ----------------------------------------------------------------------

long_description = open('README.md', mode="r").read()

# ----------------------------------------------------------------------
# Declare the setup function
# ----------------------------------------------------------------------


setup(name="pymetacline",
      version=version,
      author_email=email,
      author=author,
      description=description,
      url=url,
      zip_safe=False,
      project_urls={
          'Source': url_source,
          'Tracker': url_tracker
      },
      python_requires=python_requires,
      keywords=keywords,
      packages=['pymetacline',
                'doc',
                'doc/source',
                'pymetacline/data',
                'pymetacline/data/fasta',
                'pymetacline/data/gtf'],
      package_data={'pymetacline/data': ['*.*'],
                    'pymetacline/data/fasta': ['*.*'],
                    'pymetacline/data/gtf': ['*.*'],
                    'docs': ['Makefile'],
                    'docs/source': ['*.*']},
      scripts=['scripts/compute_tx_len.py'],
      license='LICENSE',

      classifiers=classifiers,
      long_description=long_description,
      extras_require={
          'dev': ['sphinx',
                  'nose']},
      install_requires=['setuptools'])

sys.stderr.write("\n\nInstallation complete.\n\n")
