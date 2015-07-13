# ocupado
Plug-in based tool which checks a user data source against an authoritative source and alerts on any anomalies.

[![Build Status](https://api.travis-ci.org/ashcrow/ocupado.png)](https://travis-ci.org/ashcrow/ocupado/)

## Example
```
$ ocupado -V conf/test.ini
- Plugins loaded: ['ocupado.plugin.test:Test']
- Plugins initialized: ['ocupado.plugin.test:Test']
- Getting users for plugin ocupado.plugin.test:Test
- Could not find user example in the authoritative plugin
- Notifying via ocupado.output.test:Test for: ['example']
$
```