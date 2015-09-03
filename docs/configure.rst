.. _configuration:

Configuration
=============
While the configuration system has been built to allow for future extending a simple INI style
configuration is shipped and shown in examples.

INI Sections
------------
There are three required sections:

* plugin: The user data sources.
* output: Where the resulting data flows out from.
* authoritative: A special user data source that acts as the source of truth.

Each uses the same format and expects a list of ``module = class`` like so:

.. code-block:: ini

   [plugin]
   my.plugin.module = PluginClass
   another.plugin.module = AnotherClass

Each ``module = class`` is configured with its *own section* using the the module as the
section name. This section takes ``key = value`` pairs which will be passed to a plugin's
``__init__``. For instance, to configure ``my.plugin.module = PluginClass`` above:


.. code-block:: ini

   [my.plugin.module]
   username = user
   domain = example.org
   # ...


.. note::
   
   The authoritative section specifies the single authoritative data source. There is no support for multiple sources of truth.

And there is also two optional sections:

* ignored_users: username as key (values ignored)

.. code-block:: ini

   [ignored_users]
   admin_account =
   ignorethisonetoo =
   # ...


* equate_users: username is an alias for another username

.. code-block:: ini

   [equate_users]
   thisguy = realuser
   # ...


INI Extras
----------

Python's ``ConfigParser`` doesn't support accepting lists. To get around this
the INI plugin accepts comma seperated items and parses them to a list.

.. code-block:: ini

   [ocupado.output.smtp]
   # ...
   smtpto = me@example.org,you@example.org
   # Parses to ['me@example.org', 'you@example.org']


INI Example
-----------

Check out this `simple example <https://github.com/ashcrow/ocupado/blob/master/conf/test.ini>`_ for
a complete config using the test plugins.

Next
----
Now it's time to :ref:`use ocupado <usage>`.
