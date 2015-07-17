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

Check out this [simple example](https://github.com/ashcrow/ocupado/blob/master/conf/test.ini) for
a complete config using the test plugins.
