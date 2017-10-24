from django.conf.urls import url

from .views import (
    CreateAulaIngrediente,
    ListAulaIngrediente,
    EditAulaIngrediente,
    DeleteAulaIngrediente
)

urlpatterns = [
    url(r'^create/$', CreateAulaIngrediente.as_view(), name='create'),
    url(r'^list/$', ListAulaIngrediente.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditAulaIngrediente.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteAulaIngrediente.as_view(), name='delete'),
]
