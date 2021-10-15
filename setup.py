"""
Setup for making overall package
"""
__author__ = 'Tommy Godfrey'
__copyright__ = 'Copyright 2019 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    _long_description = readme_file.read()

setup(
    name='ceda-directory_tree',
    version='1.0.0',
    description='Python package to create a virtual tree data structure to represent a directory tree to be used for efficient search',
    author='Tommy Godfrey',
    author_email='tommy.godfrey@stfc.ac.uk',
    url='https://github.com/cedadev/ceda-directory-tree',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    license='BSD - See LICENSE file for details',
    packages=find_packages(),
    include_package_data = True,
    python_requires='>=3',
    install_requires='anytree',
    extras_require={
        'docs':[
            'sphinx',
            'sphinx-rtd-theme',
            'sphinxcontrib-programoutput'
        ]
    },
    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            'directory-tree-speed-test=directory_tree.examples.speed_test:main'
        ]
    }
)
