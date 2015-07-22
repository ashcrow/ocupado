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
"""
Tests for the the INI Config.
"""

import unittest

from ocupado.config.ini import INIConfig


class TestINIConfig(unittest.TestCase):

    def test_ini_config__init(self):
        cfg = INIConfig('conf/test.ini')
        self.assertEquals(cfg._location, 'conf/test.ini')

    def test_ini_config__getitem(self):
        cfg = INIConfig('conf/test.ini')
        self.assertEquals(cfg['plugin'], [('ocupado.plugin.test', 'Test', )])
        self.assertRaises(KeyError, cfg.__getitem__, 'DoesNotExist')

    def test_ini_config_list_plugins(self):
        cfg = INIConfig('conf/test.ini')
        self.assertEquals(
            cfg.list_plugins(),
            {'ocupado.plugin.test': {
                'class': 'Test', 'kwargs': {'key': 'value'}}})

    def test_ini_config_list_outputs(self):
        cfg = INIConfig('conf/test.ini')
        self.assertEquals(
            cfg.list_outputs(),
            {'ocupado.output.test': {
                'class': 'Test',
                'kwargs': {'key': 'value'}}})

    def test_ini_config_get_authoritative(self):
        cfg = INIConfig('conf/test.ini')
        self.assertEquals(
            cfg.get_authoritative(),
            {'ocupado.plugin.test': {
                'class': 'Test',
                'kwargs': {'key': 'value'}}})

    def test_ini_config_load_ignored_users(self):
        cfg = INIConfig('conf/test.ini')
        self.assertIsNone(cfg.load_ignored_users())
        self.assertEquals(cfg.ignored_users, ['ignoreme'])

    def test_ini_config_load_ignored_users_with_no_section(self):
        cfg = INIConfig('conf/test.ini')
        cfg._cp.remove_section('ignored_users')
        self.assertIsNone(cfg.load_ignored_users())
        self.assertEquals(cfg.ignored_users, [])
