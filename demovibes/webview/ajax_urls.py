from django.conf.urls.defaults import *
from demovibes.webview.models import *
from demovibes.webview import ajax_views

urlpatterns = patterns('',
    (r'^ping/(?P<event_id>\d+)/$',   'demovibes.webview.ajax_views.ping'),
    (r'^monitor/(?P<event_id>\d+)/$',   'demovibes.webview.ajax_views.monitor'),
    (r'^license/(?P<id>\d+)/$',   ajax_views.LicenseView()),
    url(r'^nowplaying/$',          'demovibes.webview.ajax_views.nowplaying', name="dv-ax-nowplaying"),
    url(r'^queue/$',               'demovibes.webview.ajax_views.queue', name="dv-ax-queue"),
    url(r'^history/$',             'demovibes.webview.ajax_views.history', name="dv-ax-history"),
    url(r'^smileys/$',             'demovibes.webview.ajax_views.smileys', name="dv-ax-smileys"),
    url(r'^songinfo/$',             'demovibes.webview.ajax_views.songinfo', name="dv-ax-songinfo"),
    url(r'^oneliner/$',            'demovibes.webview.ajax_views.oneliner', name="dv-ax-oneliner"),
    url(r'^tags/$',            'demovibes.webview.ajax_views.get_tags', name="dv-ax-taglist"),
    (r'a_queue_(?P<song_id>\d+)/$',        'demovibes.webview.ajax_views.songupdate'),
    (r'words/(?P<prefix>\w+)/$',        'demovibes.webview.ajax_views.words'),
    url(r'oneliner_submit/$',                'demovibes.webview.ajax_views.oneliner_submit', name = "dv-ax-oneliner_submit"),
)
