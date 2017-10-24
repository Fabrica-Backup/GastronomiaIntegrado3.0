from django.conf.urls import url

from .views import CreateReceita, ListReceita, EditReceita, DeleteReceita

urlpatterns = [
    url(r'^create/$', CreateReceita.as_view(), name='create'),
    url(r'^list/$', ListReceita.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditReceita.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteReceita.as_view(), name='delete'),
]
