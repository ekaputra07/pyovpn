#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  PyOvpn - Simple Python Open VPN Client
#  Copyright (C) 2012 Eka Putra - ekaputra@balitechy.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name = "PyOvpn",
    version = "0.2.1",
    url = 'https://github.com/ekaputra07/pyovpn',
    description = 'Simple Python Open VPN Client.',
    license = 'GNU/GPL',
    author = 'Eka Putra',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    install_requires = ['pexpect', 'pyqt4'],
    data_files = [
                ('/usr/share/pixmaps', ['data/pyovpn.svg']),
                ('/usr/share/applications', ['data/pyovpn.desktop'])
                ],
    include_package_data = True,
    zip_safe = False,
    scripts=['bin/pyovpn'],
)

