Starting mac-attrs
==================

Before starting mac-attrs for the first time, run the following commands from your shell.

.. code-block:: console

   [user@host mac-attrs]$ chmod +x ./get-started.sh
   [user@host mac-attrs]$ ./get-started.sh

To start mac-attrs, run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ gunicorn --bind=0.0.0.0:8080 --workers=2 "mac_attrs:make_app()"
