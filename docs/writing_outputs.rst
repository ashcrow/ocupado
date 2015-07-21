Writing Outputs
===============
Similar to Plugins, outputs provide a way to extend the functionality of ``ocupado`` by defining new ways for
the resulting output to be processed. Just like Plugins, Outputs are Python modules and must define how to
output results.  The module must provide a class which subclasses `ocupado.output.Output <https://github.com/ashcrow/ocupado/blob/master/src/ocupado/output/__init__.py>`_ and, of course, must be installed on the system for use.


Example
-------
The following example is the `SMTP output <https://github.com/ashcrow/ocupado/blob/master/src/ocupado/output/smtp.py>`_
which comes bundled along with ``ocupado``.

Notice that:

* The output subclasses ``Output``.
* ``notify(users)`` is defined.

.. literalinclude:: ../src/ocupado/output/smtp.py
