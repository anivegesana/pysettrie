#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, Extension
from Cython.Build import cythonize

if os.name == 'nt':
    # Windows compile time arguments
    extra_compile_args = ["/std:c++17"]
else:
    # Mac/Linux GCC compile time arguments
    extra_compile_args = ["-std=c++17", "-g", "-O3", "-fPIC"]

setup(
    name='pysettrie',
    url='https://github.com/mmihaltz/pysettrie',
    version='0.1.3',
    author='Márton Miháltz ',
    description='Efficient storage and querying of sets of sets using the trie data structure',
    packages=['settrie'],
    install_requires=['sortedcontainers'],
    ext_modules = cythonize(Extension("settrie", sources=["settrie/settrie.pyx"], extra_compile_args=extra_compile_args), language_level=3),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'],
)
