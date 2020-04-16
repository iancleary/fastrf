from setuptools import setup
from setuptools import find_packages
from distutils import util

setup(name='fastrf',
      version='0.0.0',
      description='FastRF application, create link budgets, track compliance, fast to use, ready for use',
      author='Ian Cleary',
      package_data={'': ['Readme.md']},
      include_package_data=True,
      license="MIT",
      packages=find_packages(),
      install_requires=[],
      )
