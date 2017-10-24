from django.conf.urls import url

from .views import CreateIngrediente, ListIngrediente, EditIngrediente, DeleteIngrediente

urlpatterns = [
    url(r'^create/$', CreateIngrediente.as_view(), name='create'),
    url(r'^list/$', ListIngrediente.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditIngrediente.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteIngrediente.as_view(), name='delete'),
]



