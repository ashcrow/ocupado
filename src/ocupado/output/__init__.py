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
Output backends
"""


class Output:
    """
    Parent class for all Output backends.
    """

    def __init__(self, **kwargs):
        """
        Creates an instance of _Output.

        :param dict kwargs: All keyword arguments for use in notify()
        """
        self._conf = kwargs

    def notify(self, usernames):
        """
        Implements notification for non matching users.

        :param list usernames: list of usernames which do not match.
        """
        raise NotImplementedError("notify(usernames) must be implemented")
