from unicodedata import name
from setuptools import setup

setup(
  name="dev_aberto_gui",
  version=0.1,
  packages=['dev_aberto'],
  install_requires=[
    'requests'
  ],
  scripts=['scripts/hello.py']
)