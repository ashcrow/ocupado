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
Tests for the the SMTP Output.
"""

import unittest

import mock

from ocupado.output.smtp import SMTP


class TestOutputSMTP(unittest.TestCase):

    def test_output_smtp__init(self):
        # Without smtpsubject
        smtp = SMTP(
            smtphost='localhost',
            smtpfrom='noreply@example.com',
            smtpto=['admin@example.com'])
        self.assertEquals(smtp._conf, {
            'smtphost': 'localhost',
            'smtpfrom': 'noreply@example.com',
            'smtpto': ['admin@example.com']})

        # With smtpsubject
        smtp = SMTP(
            smtphost='localhost',
            smtpfrom='noreply@example.com',
            smtpto=['admin@example.com'],
            smtpsubject='My subject')
        self.assertEquals(smtp._conf, {
            'smtphost': 'localhost',
            'smtpfrom': 'noreply@example.com',
            'smtpto': ['admin@example.com'],
            'smtpsubject': 'My subject'})

    def test_output_smtp_notify(self):
        with mock.patch("smtplib.SMTP") as _smtp:
            smtp = SMTP(
                smtphost='localhost',
                smtpfrom='noreply@example.com',
                smtpto=['admin@example.com'])
            # No return is no error
            self.assertEquals(smtp.notify(['someone@example.org']), None)
            self.assertEquals(_smtp().sendmail.call_count, 1)
            self.assertEquals(
                _smtp().sendmail.call_args[0][2], (
                    "From: noreply@example.com\nSubject: Unmatched users\n\n"
                    "The following usernames could not be found: "
                    "['someone@example.org']"))
            self.assertEquals(_smtp().quit.call_count, 1)

    def test_output_smtp_notify_with_subject(self):
        with mock.patch("smtplib.SMTP") as _smtp:
            smtp = SMTP(
                smtphost='localhost',
                smtpfrom='noreply@example.com',
                smtpto=['admin@example.com'],
                smtpsubject='\n \nNewlines\n\n')
            # No return is no error
            self.assertEquals(smtp.notify(['someone@example.org']), None)
            self.assertEquals(_smtp().sendmail.call_count, 1)
            self.assertEquals(
                _smtp().sendmail.call_args[0][2], (
                    "From: noreply@example.com\nSubject:  Newlines\n\n"
                    "The following usernames could not be found: "
                    "['someone@example.org']"))
            self.assertEquals(_smtp().quit.call_count, 1)

    def test_output_smtp_notify_with_subject_colon(self):
        with mock.patch("smtplib.SMTP") as _smtp:
            smtp = SMTP(
                smtphost='localhost',
                smtpfrom='noreply@example.com',
                smtpto=['admin@example.com'],
                smtpsubject=':Colon:')
            # No return is no error
            self.assertEquals(smtp.notify(['someone@example.org']), None)
            self.assertEquals(_smtp().sendmail.call_count, 1)
            self.assertEquals(
                _smtp().sendmail.call_args[0][2], (
                    "From: noreply@example.com\nSubject: Colon\n\n"
                    "The following usernames could not be found: "
                    "['someone@example.org']"))
            self.assertEquals(_smtp().quit.call_count, 1)
