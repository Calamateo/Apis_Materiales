from django.db import router
from rest_framework import routers
from django.urls import path, include
from .views import * 

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
#OMNICLAS23
# router.register('OmniClass23', OmniClass23ViewSet)
router.register('OMC23Nivel1', OMC23Nivel1ViewSet)
router.register('OMC23Nivel2', OMC23Nivel2ViewSet)
router.register('OMC23Nivel3', OMC23Nivel3ViewSet)
router.register('OMC23Nivel4', OMC23Nivel4ViewSet)
router.register('OMC23Nivel5', OMC23Nivel5ViewSet)
router.register('OMC23Nivel6', OMC23Nivel6ViewSet)
#OMNICLAS41
router.register('OMC41Nivel1', OMC41Nivel1ViewSet)
router.register('OMC41Nivel2', OMC41Nivel2ViewSet)
router.register('OMC41Nivel3', OMC41Nivel3ViewSet)
router.register('OMC41Nivel4', OMC41Nivel4ViewSet)
router.register('OMC41Nivel5', OMC41Nivel5ViewSet)
router.register('OMC41Nivel6', OMC41Nivel6ViewSet)

#MATERIALES
# router.register('CrearMaterial/', CrearMaterial)
# router.register('CrearConcreto/', CrearConcreto)
# router.register('CrearCaracEspe/', CrearCaracEspe)
#router.register('Materiales/', MostrarMateriales)


urlpatterns=[
    path('',include(router.urls)),
    path('CrearMaterial/', CrearMaterial.as_view(), name='CrearMaterial'),
    path('Materiales/', ListarMateriales.as_view(), name='MostrarMateriales'),
    path('Concreto/', ListarConcreto.as_view(), name='MostrarConcreto'),
    path('CrearConcreto/', CrearConcreto.as_view(), name='CrearConcreto'),
    path('CrearCaracEspe/', CrearCaracEspe.as_view(), name='CrearCaracEspe'),
    path('ListarEsfuerzo/', ListarEsfuerzo.as_view(), name='ListarEsfuerzo'),
    path('ListarValorEsfuerzo/', ListarValorEsfuerzo.as_view(), name='ListarValorEsfuerzo'),
    path('ListarTipoResistencia/', ListarTipoResistencia.as_view(), name='ListarTipoResistencia'),
    path('ListarAplPrincipales/', ListarAplPrincipales.as_view(), name='ListarAplPrincipales'),
    path('ListarTMA/', ListarTMA.as_view(), name='ListarTMA'),
    path('ListarRevenimiento/', ListarRevenimiento.as_view(), name='ListarRevenimiento'),
    path('ListarDensidad/', ListarDensidad.as_view(), name='ListarDensidad'),
    path('ListarSistColocacion/', ListarSistColocacion.as_view(), name='ListarSistColocacion'),
    path('ListarClasExposicion/', ListarClasExposicion.as_view(), name='ListarClasExposicion'),
    path('ListarFlujoRev/', ListarFlujoRev.as_view(), name='ListarFlujoRev'),
    path('ListarIonCloruro/', ListarIonCloruro.as_view(), name='ListarIonCloruro'),
    path('ListarFibraConcre/', ListarFibraConcre.as_view(), name='ListarFibraConcre'),
    path('ListarUnidadesMedida/', ListarUnidadesMedida.as_view(), name='ListarUnidadesMedida'),
]




