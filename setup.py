#!/usr/bin/env python3
#
# Setup script for standalone libgpiod Python bindings.
#
# SPDX-License-Identifier: LGPL-2.1-or-later
# Copyright (C) 2020 Allen Wild <allenwild93@gmail.com>

import sys
if sys.version_info < (3,):
    sys.exit('Error: this module requires Python 3')

from setuptools import Extension, setup

GPIOD_VERSION = '1.4.1'

gpiod_extension = Extension(
    'gpiod',
    [
        # gpiod Python module
        'gpiod/gpiodmodule.c',
        # libgpiod C API
        'gpiod/core.c',
        #'gpiod/ctxless.c', # not needed by python bindings
        'gpiod/helpers.c',
        'gpiod/iter.c',
        'gpiod/misc.c',
    ],
    include_dirs=['gpiod'],
    define_macros=[('_GNU_SOURCE', None), ('GPIOD_VERSION_STR', '"%s"'%GPIOD_VERSION)],
)

setup(
    name='gpiod',
    ext_modules=[gpiod_extension],

    version=GPIOD_VERSION,
    description='libgpiod Python bindings',
    author='Bartosz Golaszewski',
    author_email='bartekgola@gmail.com',
    maintainer='Allen Wild',
    maintainer_email='allenwild93@gmail.com',

    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux',
    ]
)
