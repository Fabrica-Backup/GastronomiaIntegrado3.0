from django.conf.urls import url

from .views import CreateAulaReceita, ListAulaReceita, EditAulaReceita, DeleteAulaReceita



urlpatterns = [
    url(r'^create/$', CreateAulaReceita.as_view(), name='create'),
    url(r'^list/$', ListAulaReceita.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditAulaReceita.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteAulaReceita.as_view(), name='delete'),
]