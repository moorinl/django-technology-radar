from django.conf.urls import url

from technology_radar import views


urlpatterns = [
    url(r'^$', views.ApiRootView.as_view(), name='api-root'),
    url(r'^radars/$', views.RadarListView.as_view(), name='radar-list'),
]
