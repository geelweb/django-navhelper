from django.conf.urls import patterns, url

urlpatterns = patterns('tests.views',
    url(r'^main-page/$', 'page', name='p1'),
    url(r'^main-page/sub-section/$', 'page', name='p1-s1'),
    url(r'^second-page/$', 'page', name='p1'),
    )
