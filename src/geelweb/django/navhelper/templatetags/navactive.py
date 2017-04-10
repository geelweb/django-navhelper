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
    url_list = set(urls.split())

    resolved = resolve(request.path)
    resolved_urls = set()
    if resolved.url_name:
        resolved_urls.add(resolved.url_name)
    if resolved.namespaces:
        resolved_urls = resolved_urls.union(["{}:{}".format(namespace, resolved.url_name) for namespace in resolved.namespaces])
        resolved_urls = resolved_urls.union(["{}:".format(namespace) for namespace in resolved.namespaces])
    if getattr(resolved, 'app_name', None):
        resolved_urls = resolved_urls.union(["{}:{}".format(resolved.app_name, resolved.url_name), "{}:".format(resolved.app_name)])
    if getattr(resolved, 'app_names', []):
        resolved_urls = resolved_urls.union(["{}:{}".format(app_name, resolved.url_name) for app_name in resolved.app_names])
        resolved_urls = resolved_urls.union(["{}:".format(app_name) for app_name in resolved.app_names])
    if url_list and resolved_urls and bool(resolved_urls & url_list):
        return getattr(settings, "NAVHELPER_ACTIVE_CLASS", "active")
    return getattr(settings, "NAVHELPER_NOT_ACTIVE_CLASS", "")

