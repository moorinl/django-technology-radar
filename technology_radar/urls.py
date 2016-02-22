from django.conf.urls import url

from technology_radar import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^radars/(?P<radar>[\w-]+)/$', views.radar_detail,
        name='radar-detail'),
    url(r'^radars/(?P<radar>[\w-]+)/download/$', views.radar_detail_download,
        name='radar-detail-download'),
    url(r'^radars/(?P<radar>[\w-]+)/(?P<area>[\w-]+)/$', views.area_detail,
        name='area-detail'),
    url(r'^radars/(?P<radar>[\w-]+)/(?P<area>[\w-]+)/(?P<blip>[\w-]+)/$',
        views.blip_detail, name='blip-detail'),
    url(r'^api/$', views.RootView.as_view(), name='api-root'),
    url(r'^api/areas/$', views.AreaListView.as_view(), name='api-area-list'),
    url(r'^api/statuses/$', views.StatusListView.as_view(),
        name='api-status-list'),
    url(r'^api/radars/$', views.RadarListView.as_view(),
        name='api-radar-list'),
    url(r'^api/radars/(?P<pk>[0-9]+)/$', views.RadarDetailView.as_view(),
        name='api-radar-detail'),
    url(r'^api/blips/$', views.BlipListView.as_view(),
        name='api-blip-list'),
    url(r'^api/blips/(?P<pk>[0-9]+)/$', views.BlipDetailView.as_view(),
        name='api-blip-detail'),
]
