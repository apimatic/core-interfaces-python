
import sys
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='apimatic-core-interfaces',
    version='0.1.5',
    description='An abstract layer of the functionalities provided by apimatic-core-library, requests-client-adapter '
                'and APIMatic SDKs.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='APIMatic',
    author_email='support@apimatic.io',
    license='MIT',
    url='https://github.com/apimatic/core-interfaces-python',
    packages=find_packages(),
)
