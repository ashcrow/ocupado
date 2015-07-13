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
Plugins for ocupado.
"""


class Plugin:
    """
    Parent class for all plugins.
    """

    def __init__(self, **kwargs):
        """
        Creates an instance of a Plugin.
        """
        pass

    def authenticate(self, **kwargs):
        """
        Defines how to authenticate via a Plugin.

        :kwargs: Keyword arguments to use with authenticatation.
        """
        raise NotImplementedError('authenticate(**kwargs) must be implemented')

    def logout(self):
        """
        Defines how to logout via a Plugin.
        """
        raise NotImplementedError('logout() must be implemented')

    def exists(self, userid):
        """
        Checks for the existance of a user.

        :userid: The userid to check.
        """
        raise NotImplementedError('exists(userid) must be implemented')

    def get_all_usernames(self):
        """
        Returns **all** user names.
        """
        raise NotImplementedError('get_all_users() must be implemented')

    # Read-only properties
    users = property(lambda s: s.get_all_usernames())
