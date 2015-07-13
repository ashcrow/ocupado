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

        :location: Location of the configuration provider.
        """
        self._location = location

    def reload(self):
        """
        Reloads the configuration files contents.
        """
        raise NotImplementedError('reload(location) must be implemented')

    def __getitem__(self, name):
        """
        Enables getting of items with d[k] format.

        :name: The name of the section to get.
        """
        raise NotImplementedError(
            '__getitem__(name) must be implemented')

    def list_plugins(self):
        """
        Gets all plugin configurations.
        """
        raise NotImplementedError('list_plugins() must be implemented')

    def list_outputs(self):
        """
        Gets all output configurations.
        """
        raise NotImplementedError('list_outputs() must be implemented')

    def get_authoritative(self):
        """
        Return the authoritative plugin.
        """
        raise NotImplementedError('get_authoritative() must be implemented')

    # Read-only properties
    plugins = property(lambda s: s.list_plugins())
    outputs = property(lambda s: s.list_outputs())
    authoritative = property(lambda s: s.get_authoritative())
