# -*- coding: utf-8 -*-

from django.template import Context, Template
from django.test import TestCase, RequestFactory

class NavhelperTemplateTagTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_navactive(self):
        self._navactive_common('active', '')

        with self.settings(NAVHELPER_ACTIVE_CLASS='my-active-class',
                NAVHELPER_NOT_ACTIVE_CLASS='my-not-active-class'):
            self._navactive_common('my-active-class', 'my-not-active-class')

    def test_renavactive(self):
        self._renavactive_common('active', '')

        with self.settings(NAVHELPER_ACTIVE_CLASS='my-active-class',
                NAVHELPER_NOT_ACTIVE_CLASS='my-not-active-class'):
            self._renavactive_common('my-active-class', 'my-not-active-class')

    def _navactive_common(self, active, not_active):
        request = self.factory.get('/main-page/')

        out = Template(
                "{% load navactive %}"
                "{% navactive request 'p1' %}"
            ).render(Context({"request": request}))
        self.assertEqual(out, active)

        out = Template(
                "{% load navactive %}"
                "{% navactive request 'p1-s1' %}"
            ).render(Context({"request": request}))
        self.assertEqual(out, not_active)

        out = Template(
                "{% load navactive %}"
                "{% navactive request 'p1 p1-s1' %}"
            ).render(Context({"request": request}))
        self.assertEqual(out, active)

        out = Template(
                "{% load navactive %}"
                "{% navactive request 'p2' %}"
            ).render(Context({"request": request}))
        self.assertEqual(out, not_active)

    def _renavactive_common(self, active, not_active):
        t1 = "{% load navactive %}{% renavactive request '^/main-page' %}"

        request = self.factory.get('/main-page/')
        out = Template(t1).render(Context({"request": request}))
        self.assertEqual(out, active)

        request = self.factory.get('/main-page/sub-section/')
        out = Template(t1).render(Context({"request": request}))
        self.assertEqual(out, active)

        request = self.factory.get('/second-page/')
        out = Template(t1).render(Context({"request": request}))
        self.assertEqual(out, not_active)
