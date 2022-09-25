from distutils.core import setup

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'django_case_insensitive_field',         # How you named your package folder (MyLib)
  version = '1.0.7',      # Start with a small number and increase it with every change you make
  license='MIT',
  py_modules=["django_case_insensitive_field"],             # Name of the python package       # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Django Case Insensitive Field is used to make Django Model Field case insensitive - by default Django can't do this.",
  author = 'iamoracle',                   # Type in your name
  author_email = 'officialbilas@gmail.com',      # Type in your E-Mail
  long_description=long_description,      # Long description read from the the readme file
  long_description_content_type="text/markdown",
  url = 'https://github.com/iamoracle/django_case_insensitive_field',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/iamoracle/django_case_insensitive_field/archive/refs/tags/v1.0.7.tar.gz',    # I explain this later on
  keywords = ['Django', 'Case Insensitive', 'Field', 'How to make Django Field', 'make django case insensitive'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
