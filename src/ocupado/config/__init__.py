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
Configuration backends.
"""


class _Config:
    """
    Parent class for all Configuration backends.
    """

    def __init__(self, location):
        """
        Creates an instance of _Config.

        :param str location: Location of the configuration provider.
        """
        self._location = location
        self._ignored_users = []

    def reload(self):
        """
        Reloads the configuration files contents.
        """
        raise NotImplementedError('reload(location) must be implemented')

    def __getitem__(self, name):
        """
        Enables getting of items with d[k] format.

        :param str name: The name of the section to get.
        :return str: The item at d[k]
        :raises KeyError: If the item does not exist.
        """
        raise NotImplementedError(
            '__getitem__(name) must be implemented')

    def list_plugins(self):
        """
        Gets all plugin configurations.

        :return dict: Dictionary of the plugins.
        """
        raise NotImplementedError('list_plugins() must be implemented')

    def list_outputs(self):
        """
        Gets all output configurations.

        :return dict: Dictionary of the outputs.
        """
        raise NotImplementedError('list_outputs() must be implemented')

    def get_authoritative(self):
        """
        Return the authoritative plugin.

        :return dict: Dictionary of the authoritative plugin.
        """
        raise NotImplementedError('get_authoritative() must be implemented')

    def load_ignored_users(self):
        """
        Loads ignored users from a config.
        """
        raise NotImplementedError('load_ignored_users() must be implemented')

    def ignore_user(self, userid):
        """
        Adds a username to the list to ignore.

        :param str userid: A username to ignore
        """
        self._ignored_users.append(userid)

    # Read-only properties
    #: Property listing all ignored users
    ignored_users = property(lambda s: s._ignored_users)
    #: Property showing all plugins.
    plugins = property(lambda s: s.list_plugins())
    #: Property showing all outputs.
    outputs = property(lambda s: s.list_outputs())
    #: Property showing the authoritative plugin.
    authoritative = property(lambda s: s.get_authoritative())
