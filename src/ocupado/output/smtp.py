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
SMTP output backend.
"""

import smtplib

from ocupado.output import Output


class SMTP(Output):
    """
    SMTP output backend.
    """

    def notify(self, usernames):
        """
        Implements notification for non matching users.

        :param list usernames: list of usernames which do not match.
        """
        msg = "The following usernames could not be found: %s" % usernames
        server = smtplib.SMTP(self._conf['smtphost'])
        server.sendmail(self._conf['smtpfrom'], self._conf['smtpto'], msg)
        server.quit()
