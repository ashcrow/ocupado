.. _installation:

Installing
==========

pip
---
`pip <https://pip.pypa.io/en/stable/>`_ makes installing Python source and their dependencies a breeze and is the
recommended way of installing ``ocupado``.

.. code-block:: shell

   $ pip install https://github.com/ashcrow/ocupado


Traditional
-----------
The traditional way to install Python code is via the ``setup.py`` command that comes with the source code.

.. note::

   You will need to resolve dependencies manually upon installation.

.. code-block:: bash

   $ ./setup.py install


Adding Plugins
==============
On it's own ``ocupado`` doesn't do much more than provide a framework for user data sources.
Installing plugins allows for integration with external data sources. Using either the
above ``pip`` or ``traditional`` method of installtion should work for the following plugins:

.. include:: plugins.rst


Next
----
The next step is to make a :ref:`configuration <configuration>`.
