Django navhelper
================

|Build status|

Django template tags to add active class on navigation menus

Prerequisites
-------------

-  Django 4.2
-  Python 3.10

Installation
------------

From sources

.. code-block:: text

    python setup.py install

From PyPi

.. code-block:: text

    pip install django-navhelper==1.0

Configure your Django installation
----------------------------------

Add ``geelweb.django.navhelper`` in your ``INSTALLED_APPS``.

Template tags
-------------

navactive
~~~~~~~~~

Returns "active" if url name of the current request path is in the list
of view names

.. code-block:: html

    {% load navactive %}
    <li class="{% navactive request "view_name app_name:another_view_name namespace:" %}">
        <a href="{% url "view_name" }">Menu Entry</a>
    </li>

renavactive
~~~~~~~~~~~

Returns "active" if the pattern is found in the request path

.. code-block:: html

    {% load navactive %}
    <li class="{% renavactive request "^/start_with_foo" %}">
        <a href="{% url "view_name" }">Menu Entry</a>
    </li>

Settings
--------

You can customize some options using settings

**NAVHELPER\_ACTIVE\_CLASS**

Default: 'active'

The class name for active entries

**NAVHELPER\_NOT\_ACTIVE\_CLASS**

Default: '' (Empty string)

The class name for non-active entries


Run test suite
--------------

To run the test suite, first, create and activate a virtual environment. Then install some requirements and run the tests:

.. code-block:: text

        pip install Django==4.2
        python runtests.py

.. |Build status| image:: https://github.com/geelweb/django-navhelper/actions/workflows/testsuite.yml/badge.svg
