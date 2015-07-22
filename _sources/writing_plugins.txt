Writing Plugins
===============
``ocupado`` provides multiple ways to modify and extend it's usage. However, the most useful way to
customize the tool is through plugins. Plugins are Python modules which define how to work with an external
datasource. The module must provide a class which subclasses `ocupado.plugin.Plugin <https://github.com/ashcrow/ocupado/blob/master/src/ocupado/plugin/__init__.py>`_ and, of course, must be installed on the system for use.


Example
-------
Here is the `test plugin <https://github.com/ashcrow/ocupado/blob/master/src/ocupado/plugin/test.py>`_
which is, as it's name suggests, is used for testing.

Notice that:

* The plugin subclasses ``Plugin``.
* ``__init__(..)`` is capturing an arguments required.
* ``authenticate()``, ``logout()``, ``exists(userid)``, and ``get_all_usernames()`` are defined.

.. literalinclude:: ../src/ocupado/plugin/test.py
