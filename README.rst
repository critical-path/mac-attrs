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


Starting mac-attrs
==================

Before starting mac-attrs for the first time, run the following commands from your shell.

.. code-block:: console

   [user@host mac-attrs]$ chmod +x ./get-started.sh
   [user@host mac-attrs]$ ./get-started.sh

To start mac-attrs, run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ gunicorn --bind=0.0.0.0:8080 --workers=2 "mac_attrs:make_app()"


Using mac-attrs
===============

Using mac-attrs is easy!

1. Point your browser to any of the following URLs.

* :code:`http://localhost:8080/`
* :code:`http://localhost:8080/home`
* :code:`http://localhost:8080/home.html`
* :code:`http://localhost:8080/index`
* :code:`http://localhost:8080/index.html`
* :code:`http://localhost:8080/mac-attrs`
* :code:`http://localhost:8080/mac-attrs.html`

2. Type a MAC address.

3. Click on the :code:`submit` button.

4. View the results.


Testing mac-attrs
=================

To conduct testing, run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ pytest --disable-warnings --cov --cov-report=term-missing

If pytest raises an :code:`INTERNALERROR`, then run the following command from your shell.

.. code-block:: console

   [user@host mac-attrs]$ sudo $(which pytest) --disable-warnings --cov --cov-report=term-missing
