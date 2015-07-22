.. _usage:

Usage
=====

Once :ref:`installation <installation>` and :ref:`configuration <configuration>` are finished you should be able to run
``ocupado`` on the command line.

.. code-block:: shell

   $ ocupado --help
   usage: ocupado [-h] [-v] [-V] CONFIG
   
   positional arguments:
     CONFIG         Path to the config file.
   
   optional arguments:
     -h, --help     show this help message and exit
     -v, --version  show program's version number and exit
     -V, --verbose  Enables verbose output.
   $

The following shows running ``ocupado`` with the ``conf/test.ini`` file and
verbose output enabled:

.. code-block:: shell

   $ ocupado -V conf/test.ini
   - Plugins loaded: ['ocupado.plugin.test:Test']
   - Plugins initialized: ['ocupado.plugin.test:Test']
   - Getting users for plugin ocupado.plugin.test:Test
   - Could not find user example in the authoritative plugin
   - Notifying via ocupado.output.test:Test for: ['example']
   $
