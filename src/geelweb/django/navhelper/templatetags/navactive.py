from django.template import Library
from django.core.urlresolvers import resolve
from django.conf import settings
import re

register = Library()

@register.simple_tag
def renavactive(request, pattern):
    """
    {% renavactive request "^/a_regex" %}
    """
    if re.search(pattern, request.path):
        return getattr(settings, "NAVHELPER_ACTIVE_CLASS", "active")
    return getattr(settings, "NAVHELPER_NOT_ACTIVE_CLASS", "")

@register.simple_tag
def navactive(request, urls):
    """
    {% navactive request "view_name another_view_name" %}
    """
    url_name = resolve(request.path).url_name
    if url_name in urls.split():
        return getattr(settings, "NAVHELPER_ACTIVE_CLASS", "active")
    return getattr(settings, "NAVHELPER_NOT_ACTIVE_CLASS", "")

