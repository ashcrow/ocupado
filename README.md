# ocupado
Plug-in based tool which checks a user data source against an authoritative source and alerts on any anomalies.

[![Build Status](https://api.travis-ci.org/ashcrow/ocupado.png)](https://travis-ci.org/ashcrow/ocupado/)

## Example Usage
```
$ ocupado -V conf/test.ini
- Plugins loaded: ['ocupado.plugin.test:Test']
- Plugins initialized: ['ocupado.plugin.test:Test']
- Getting users for plugin ocupado.plugin.test:Test
- Could not find user example in the authoritative plugin
- Notifying via ocupado.output.test:Test for: ['example']
$
```

## Available Plugins
* [LDAP](https://github.com/ashcrow/ocupado_plugin_ldap)
* [GoogleGroups](https://github.com/ashcrow/ocupado_plugin_google_groups)
* [GoogleGroupsFree](https://github.com/ashcrow/ocupado_plugin_google_groups_free)

## Available Outputs
* SMTP (built in)

## Configuration
While the configuration system has been built to allow for future extending a simple INI style
configuration is shipped and shown in examples.

### INI Sections
There are three required sections: plugin, output, and authoritative. Each uses the same
format and expects a list of ```module = class``` like so:

```ini
[plugin]
my.plugin.module = PluginClass
another.plugin.module = AnotherClass
```

Each ```module = class``` is configured with it's *own section* using the the module as the
section name. This section takes ```key = value``` pairs which will be passed to a plugin's
```__init__```. For instance, to configure ```my.plugin.module = PluginClass``` above:

```ini
[my.plugin.module]
username = user
domain = example.org
# ...
```

Note that the authoritative section specifies the single authoritative data source. There
is no support for multiple sources of truth.

Check out this [simple example](https://github.com/ashcrow/ocupado/blob/master/conf/test.ini) for
a complete config using the test plugins.

## Developing with Ocupado

### Testing
```ocupado``` uses [nose](http://nose.readthedocs.org/en/latest/) for unittesting. Do the following to run unittests locally:

```bash
python setup.py nosetests
```

You can also take a peak at the [travis file](https://github.com/ashcrow/ocupado/blob/master/.travis.yml#L9) if you'd like to mimick
the command used in CI.

### Writing Plugins
```ocupado``` provides multiple ways to modify and extend it's usage. However, the most useful way to
customize the tool is through plugins. Plugins are Python modules which define how to work with an external
datasource. The module must provide a class which subclasses [ocupado.plugin.Plugin](https://github.com/ashcrow/ocupado/blob/master/src/ocupado/plugin/__init__.py) and, of course, must be installed on the system for use.

For an example see the [test plugin](https://github.com/ashcrow/ocupado/blob/master/src/ocupado/plugin/test.py).

### Writing Outputs
Similar to Plugins, outputs provide a way to extend the functionality of ```ocupado``` by defining new ways for
the resulting output to be processed. Just like Plugins, Outputs are Python modules and must define how to
output results.  The module must provide a class which subclasses [ocupado.output.Output](https://github.com/ashcrow/ocupado/blob/master/src/ocupado/output/__init__.py) and, of course, must be installed on the system for use.

For an example see the [SMTP output](https://github.com/ashcrow/ocupado/blob/master/src/ocupado/output/smtp.py).
