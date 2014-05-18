# Django navhelper

Django template tags to add active class on navigation menus

## Installation

From source

    python setup.py install

Using pip

    pip install django-navhelper

*settings.py*

Add `geelweb.django.navhelper` in our `INSTALLED_APPS`.

Ensure `django.core.context_processors.request` is in `TEMPLATE_CONTEXT_PROCESSORS`. Make sure you keep the components required by the features of Django you wish to use, in doubt keep the default values https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS.

*templates*

Load the tags adding in your templates

    {% load navactive %}

## Template tags

### navactive

Returns "active" if url name of the current request path is in the list of
view names

    <li class="{% navactive request "view_name another_view_name" %}">
        <a href="{% url "view_name" }">Menu Entry</a>
    </li>


### renavactive

Returns "active" if the pattern is found in the request path

    <li class="{% renavactive request "^/start_with_foo" %}">
        <a href="{% url "view_name" }">Menu Entry</a>
    </li>

## Options

You can customize some options using settings

*NAVHELPER_ACTIVE_CLASS*

Default: active

The class name for active entries

*NAVHELPER_NOT_ACTIVE_CLASS*

Default: '' (Empty string)

The class name for non-active entries

