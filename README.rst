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

Ensure ``django.core.context_processors.request`` is in
``TEMPLATE_CONTEXT_PROCESSORS``. Make sure you keep the components
required by the features of Django you wish to use, in doubt keep the
`default values`_.

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

.. _default values: https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS

.. |Build status| image:: https://travis-ci.org/geelweb/django-navhelper.svg?branch=master

Run test suite
--------------

To run the test suite, first, create and activate a virtual environment. Then install some requirements and run the tests:

.. code-block:: text

        pip install Django==4.2
        python runtests.py
