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
        # Get or use a default subject and ensure no newlines are allowed
        subject = self._conf.get(
            'smtpsubject', 'Unmatched users').replace(
                '\n', '').replace(':', '')
        msg = (
            'From: %s\nSubject: %s\n\nThe following usernames '
            'could not be found: %s' % (
                self._conf['smtpfrom'], subject, usernames))
        if type(self._conf['smtpto']) != list:
            self._conf['smtpto'] = list(self._conf['smtpto'])

        server = smtplib.SMTP(self._conf['smtphost'])
        for to_addr in self._conf['smtpto']:
            server.sendmail(self._conf['smtpfrom'], to_addr, msg)
        server.quit()
