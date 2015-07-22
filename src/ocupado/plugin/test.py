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
A simple test plugin.
"""

from ocupado.plugin import Plugin


class Test(Plugin):
    """
    A simple test plugin for testing.
    """

    def __init__(self, key):
        """
        Creates an instance of a Plugin.

        :param str key: A dummy input used for testing.
        """
        pass

    def authenticate(self):
        """
        Defines how to authenticate via the Test plugin.
        """
        pass

    def logout(self):
        """
        Defines how to logout via the Test plugin.
        """
        pass

    def exists(self, userid):
        """
        Checks for the existance of a user.

        :param str userid: The userid to check.
        :return: Boolean and extra information
        :rtype: tuple(bool, dict)
        """
        if userid in self.get_all_usernames():
            return True, {"exists": True, "details": {"username": userid}}
        return False, {'exists': False, 'details': {'username': userid}}

    def get_all_usernames(self):
        """
        Returns *all* user names.

        :return: A list of all users known to the backend.
        :rtype: list
        """
        return ['test', 'example']
