.. image:: https://travis-ci.com/critical-path/mac-attrs.svg?branch=master
   :target: https://travis-ci.com/critical-path/mac-attrs

.. image:: https://coveralls.io/repos/github/critical-path/mac-attrs/badge.svg?branch=master
   :target: https://coveralls.io/github/critical-path/mac-attrs?branch=master

.. image:: https://readthedocs.org/projects/mac-attrs/badge/?version=latest
   :target: https://mac-attrs.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Introduction
============

mac-attrs combines the functionality of `macaddress <https://github.com/critical-path/macaddress>`__ and `random-mac <https://github.com/critical-path/random-mac>`__ into a web app that evaluates the attributes of media access control (MAC) addresses.


Installing mac-attrs
====================

mac-attrs is available on GitHub at https://github.com/critical-path/mac-attrs.

If you do not have pip version 18.1 or higher, then run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --upgrade pip

To install mac-attrs with test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install --editable git+https://github.com/critical-path/mac-attrs.git#egg=mac-attrs[test]

To install it without test-related dependencies, run the following command from your shell.

.. code-block:: console

   [user@host ~]$ sudo pip install git+https://github.com/critical-path/mac-attrs.git

(If necessary, replace :code:`pip` with :code:`pip3`.)


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
* :code:`http://127.0.0.1:8080/mac-attrs.html`


Testing mac-attrs
=================

To conduct testing, run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ pytest --disable-warning --cov --cov-report=term-missing

