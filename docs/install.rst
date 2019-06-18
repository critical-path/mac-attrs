Installing mac-attrs
====================

mac-attrs is available on GitHub at https://github.com/critical-path/mac-attrs.  (A version that runs inside of a Docker container is available at https://github.com/critical-path/mac-attrs-docker.)

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install mac-attrs with test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/mac-attrs.git
   [user@host ~]$ cd mac-attrs
   [user@host mac-attrs]$ sudo pip install --editable .[test]

To install it without test-related dependencies, run the following commands from your shell.

.. code-block:: console

   [user@host ~]$ git clone git@github.com:critical-path/mac-attrs.git
   [user@host ~]$ cd mac-attrs
   [user@host mac-attrs]$ sudo pip install .

(If necessary, replace :code:`pip` with :code:`pip3`.)
