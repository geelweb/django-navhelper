# Django navhelper

## Installation

From source

    python setup.py install

Using pip

    pip install django-navhelper

Ensure "django.core.context_processors.request" is in
"TEMPLATE_CONTEXT_PROCESSORS.

Add "geelweb.django.navhelper" in our INSTALLED_APPS.

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

*NAVHELPER_ACTIVE_CLASS*

Default active class is "active", you can update it adding in your
settings.py file the following piece of code

    NAVHELPER_ACTIVE_CLASS = "your_active_class"

*NAVHELPER_NOT_ACTIVE_CLASS*

By default the navactive and renavactive tags return an empty string for
non-active entries. Change it using the following option

   NAVHELPER_NOT_ACTIVE_CLASS = "your_not_active_class"
