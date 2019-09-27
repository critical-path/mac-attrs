Testing mac-attrs
=================

To conduct testing, run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ pytest --disable-warnings --cov --cov-report=term-missing

If pytest raises an :code:`INTERNALERROR`, then run the following command from your shell.

.. code-block:: console

   [user@host random-mac]$ sudo $(which pytest) --disable-warnings --cov --cov-report=term-missing
