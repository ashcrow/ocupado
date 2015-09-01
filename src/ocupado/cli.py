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
Command line interface for ocupado.
"""

import argparse
import platform

from ocupado import __version__, PluginManager
from ocupado.config.ini import INIConfig


def main():
    """
    Handler for the CLI interface.
    """
    if int(platform.python_version_tuple()[0]) == 2:
        parser = argparse.ArgumentParser(version=__version__)
    else:
        parser = argparse.ArgumentParser()

    parser.add_argument(
        'config', metavar='CONFIG', type=str,
        nargs=1, help='Path to the config file.')
    parser.add_argument(
        '-V', '--verbose', action='store_true',
        help='Enables verbose output.')

    args = parser.parse_args()

    conf = INIConfig(args.config[0])
    conf.load_ignored_users()
    conf.load_equate_users()

    # Load plugins for use
    plugin_manager = PluginManager()
    plugin_manager.set_up_authoritative(conf.authoritative)
    plugin_manager.set_up_outputs(conf.outputs)
    plugin_manager.load_dict(conf.plugins)

    if args.verbose:
        print('- Plugins loaded: %s' % plugin_manager.plugins.keys())
    plugin_manager.set_up_plugins(conf.plugins)
    if args.verbose:
        print('- Plugins initialized: %s' % plugin_manager.instances.keys())

    unmatched = []
    # Run through all the plugin instances looking for users
    for name in plugin_manager.instances:
        if args.verbose:
            print('- Authenticating for plugin %s' % name)
        plugin_manager.instances[name].authenticate()
        if args.verbose:
            print('- Getting users for plugin %s' % name)
        for username in plugin_manager.instances[name].get_all_usernames():
            real_username = conf.user_equate(username)
            if real_username != username and args.verbose:
                print('- Username %s equates to %s' % (
                    username, real_username))

            if (username not in conf.ignored_users and
                    real_username not in conf.ignored_users):
                exists, details = plugin_manager.authoritative_instance.exists(
                    real_username)
                if exists is False:
                    if args.verbose:
                        print(
                            '- Could not find user %s in the authoritative '
                            'plugin' % real_username)
                    unmatched.append(real_username)
            else:
                if args.verbose:
                    print(
                        '- User %s is in the ignored list.' % username)

        # Be nice citizens and logout
        if args.verbose:
            print('- Logging out of plugin %s' % name)
        plugin_manager.instances[name].logout()

    if unmatched:
        # Output the results through an output plugin
        for output_name in plugin_manager.output_instances:
            print('- Notifying via %s for: %s' % (output_name, unmatched))
            plugin_manager.output_instances[output_name].notify(unmatched)
    else:
        print('- No unmatched users.')


if __name__ == '__main__':
    try:
        main()
    except:
        import sys
        err = sys.exc_info()[1]
        sys.stdout.write('- Exiting due to error. (%s)\n' % err)
        raise SystemExit(1)
    raise SystemExit(0)
