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
Pluggable CLI tool that checks external accounts with an internal source
"""

__version__ = '0.0.1'


class PluginManager:
    """
    PluginLoader is in charge of loading a all types of plugins for use.
    """

    def __init__(self):
        """
        Creates an instance of the PluginManager.
        """
        self._plugins = {}
        self._instances = {}
        self._authoritative = tuple()
        self._authoritative_instance = None
        self._output_plugins = {}
        self._output_instances = {}

    def _load_plugin(self, module_name, class_name):
        """
        Loads a plugin.

        :module_name: The name of the module. Example: some.name.like.this
        :class_name: The name of the class. Example: MyPlugin
        """
        mod = __import__(
            module_name, fromlist=['True'], globals=globals(), locals=locals())
        cls = getattr(mod, class_name)
        self._plugins[module_name + ':' + class_name] = cls

    def set_up_plugin(self, plugin_name, kwargs):
        """
        Sets up a specific plugin for use.

        :plugin_name: The full name of the plugin to set up
        :kwargs: The keyword arguments to pass to the plugin
        """
        self._instances[plugin_name] = self._plugins[plugin_name](**kwargs)

    def set_up_plugins(self, dct):
        """
        Sets up a plugins for use.

        :dct: Dictionary describing plugins as returned by _Config
        """
        for module_name, conf in dct.items():
            plugin_name = module_name + ':' + conf['class']
            self.set_up_plugin(plugin_name, conf['kwargs'])

    def load_dict(self, dct):
        """
        Loads plugins from a list.

        :plugin: list of plugins with (mod, cls)
        """
        for module_name, conf in dct.items():
            self._load_plugin(module_name, conf['class'])

    def set_up_authoritative(self, dct):
        """
        Sets up a specific authoritative plugin for use.

        :plugin_name: The full name of the plugin to set up
        :kwargs: The keyword arguments to pass to the plugin
        """
        for module_name, conf in dct.items():
            mod = __import__(
                module_name, fromlist=['True'],
                globals=globals(), locals=locals())
            cls = getattr(mod, conf['class'])
            self._authoritative = (module_name + ':' + conf['class'],  cls)
        self._authoritative_instance = self._authoritative[1](**conf['kwargs'])

    def set_up_outputs(self, dct):
        """
        Sets up a specific output plugins for use.
        """
        for module_name, conf in dct.items():
            mod = __import__(
                module_name, fromlist=['True'],
                globals=globals(), locals=locals())
            cls = getattr(mod, conf['class'])
            plugin_name = module_name + ':' + conf['class']
            self._output_plugins[plugin_name] = cls
            self._output_instances[plugin_name] = cls(**conf['kwargs'])

    # Read-only properties
    plugins = property(lambda s: s._plugins)
    instances = property(lambda s: s._instances)
    authoritative = property(lambda s: s._authoritative)
    authoritative_instance = property(lambda s: s._authoritative_instance)
    outputs = property(lambda s: s._outputs)
    output_instances = property(lambda s: s._output_instances)
