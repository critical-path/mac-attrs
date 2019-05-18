Using mac-attrs
===============

Before using mac-attrs for the first time, run the following commands from your shell.

.. code-block:: console

   [user@host mac-attrs]$ chmod +x ./get-started.sh
   [user@host mac-attrs]$ ./get-started.sh

Then, start the web server by running the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ gunicorn --bind 127.0.0.1:8080 "mac_attrs:make_app()"

Finally, point your browser to any of the following URLs to begin evaluating MAC addresses.

* :code:`http://127.0.0.1:8080/`
* :code:`http://127.0.0.1:8080/index`
* :code:`http://127.0.0.1:8080/index.html`
* :code:`http://127.0.0.1:8080/mac-attrs`
