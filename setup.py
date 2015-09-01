#!/usr/bin/env python
# Copyright (C) 2015 SEE AUTHORS FILE
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
Build script.
'''

import os.path

from setuptools import setup, find_packages


setup(
    name='ocupado',
    version='0.0.3',
    description=('Pluggable CLI tool that checks external accounts'
                 ' with an internal source'),
    author='See AUTHORS',
    author_email='stevem@gnulinux.net',
    url='https://github.com/ashcrow/ocupado',
    license='AGPLv3',
    zip_safe=False,
    package_dir={
        'ocupado': os.path.join('src', 'ocupado')
    },
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'ocupado = ocupado.cli:main',
        ]
    },
    classifiers=[
        ('License :: OSI Approved :: GNU Affero General Public '
         'License v3 or later (AGPLv3+)'),
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
    ],
)
