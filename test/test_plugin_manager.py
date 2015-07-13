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
Tests for the PluginManager
"""

import unittest

from ocupado import PluginManager


class TestPluginManager(unittest.TestCase):

    def test_plugin_manager__init(self):
        pm = PluginManager()
        self.assertEquals(len(pm._plugins), 0)

    def test_plugin_manager__load_plugin(self):
        pm = PluginManager()
        pm._load_plugin('ocupado.plugin.test', 'Test')
        self.assertEquals(len(pm._plugins), 1)

    def test_plugin_manager_set_up_plugin(self):
        pm = PluginManager()
        pm._load_plugin('ocupado.plugin.test', 'Test')
        pm.set_up_plugin('ocupado.plugin.test:Test', {'key': 'val'})
        self.assertEquals(len(pm._instances), 1)

    def test_plugin_manager_set_up_plugins(self):
        pm = PluginManager()
        pm._load_plugin('ocupado.plugin.test', 'Test')
        pm.set_up_plugins({
            'ocupado.plugin.test': {
                'class': 'Test', 'kwargs': {'key': 'value'}}})
        self.assertEquals(len(pm._instances), 1)

    def test_plugin_manager_set_up_outputs(self):
        pm = PluginManager()
        pm._load_plugin('ocupado.output.test', 'Test')
        pm.set_up_outputs({
            'ocupado.output.test': {
                'class': 'Test', 'kwargs': {}}})
        self.assertEquals(len(pm._output_instances), 1)

    def test_plugin_manager_set_up_authoritative(self):
        pm = PluginManager()
        pm._load_plugin('ocupado.plugin.test', 'Test')
        pm.set_up_authoritative({
            'ocupado.plugin.test': {
                'class': 'Test', 'kwargs': {'key': 'value'}}})
        self.assertTrue(pm._authoritative_instance)
