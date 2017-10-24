from django.conf.urls import url
from .views import planejar_aulas, aulas_concluidas
from .views import CreateAula, ListAula, EditAula, DeleteAula

urlpatterns = [
    url(r'^create/$', CreateAula.as_view(), name='create'),
    url(r'^list/$', ListAula.as_view(), name='list'),
    url(r'^edit/(?P<id>[0-9]+)$', EditAula.as_view(), name='edit'),
    url(r'^delete/(?P<id>[0-9]+)$', DeleteAula.as_view(), name='delete'),
]



'''urlpatterns = [
    url(r'^planejar_aulas$', planejar_aulas.as_view(), name='planejar_aulas'),
    url(r'^aulas_concluidas$', aulas_concluidas.as_view(), name='aulas_concluidas'),
    
]'''
