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
Simple INI configuration backend.
"""

from ocupado.config import _Config

try:
    import configparser
except ImportError:
    # python 2.x support
    import ConfigParser as configparser


class INIConfig(_Config):
    """
    Parent class for all Configuration backends.
    """

    def __init__(self, location):
        """
        Creates an INIConfig instance.

        :param str location: Location of the ini file.
        """
        _Config.__init__(self, location)
        self._cp = configparser.ConfigParser()
        self.reload()

    def reload(self):
        """
        Reloads the configuration files contents.
        """
        self._cp.read(self._location)

    def __getitem__(self, name):
        """
        Enables getting of items with d[k] format.

        :param str name: The name of the section to get.
        :return str: The item at d[k]
        :raises KeyError: If the item does not exist.
        """
        try:
            return self._cp.items(name)
        except configparser.NoSectionError:
            raise KeyError(name)

    def _list(self, type):
        """
        Shared code for listing items.

        :param str type: The section to list.
        :return dict: Dictionary describing a section of the config.
        """
        kind = {}
        for mod, cls in self._cp.items(type):
            kind[mod] = {'class': cls, 'kwargs': {}}
            for k, v in self._cp.items(mod):
                if ',' in v:
                    v = v.split(',')
                kind[mod]['kwargs'][k] = v
            return kind

    def list_plugins(self):
        """
        Gets all plugin configurations.

        :return dict: Dictionary of the plugins.
        """
        return self._list('plugin')

    def list_outputs(self):
        """
        Gets all output configurations.

        :return: Dictionary of the outputs.
        :rtype: dict
        """
        return self._list('output')

    def get_authoritative(self):
        """
        Return the authoritative plugin.

        :return dict: Dictionary of the authoritative plugin.
        """
        result = {}
        module_name, class_name = self._cp.items('authoritative')[0]
        result[module_name] = {'class': class_name, 'kwargs': {}}
        for k, v in self._cp.items('authoritative_kwargs'):
            if ',' in v:
                v = v.split(',')
            result[module_name]['kwargs'][k] = v
        return result

    def load_ignored_users(self):
        """
        Loads ignored users from an ini config.
        """
        if self._cp.has_section('ignored_users'):
            for userid, _ in self._cp.items('ignored_users'):
                self.ignore_user(userid)

    def load_equate_users(self):
        """
        Loads equate users from a config.
        """
        if self._cp.has_section('equate_users'):
            for userid, realid in self._cp.items('equate_users'):
                self._user_equate_mapping[userid] = realid
