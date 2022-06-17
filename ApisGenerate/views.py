from django.contrib.auth.models import User, Group
from ApisGenerate.serializers import *
from ApisGenerate.models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


#VISTAS PARA EL OMNICLASS 23

# class OmniClass23ViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = OmniClass23.objects.all()
#     serializer_class = OmniClass23Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel1ViewSet(viewsets.ModelViewSet):
    queryset =OMC23Nivel1.objects.all()
    serializer_class = OMC23Nivel1Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC23Nivel2ViewSet(viewsets.ModelViewSet):
    queryset =OMC23Nivel2.objects.all()
    serializer_class = OMC23Nivel2Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC23Nivel3ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel3.objects.all()
    serializer_class = OMC23Nivel3Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel4ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel4.objects.all()
    serializer_class = OMC23Nivel4Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel5ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel5.objects.all()
    serializer_class = OMC23Nivel5Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class OMC23Nivel6ViewSet(viewsets.ModelViewSet):
    queryset = OMC23Nivel6.objects.all()
    serializer_class = OMC23Nivel6Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#VISTAS PARA EL OMNICLAS 41

class OMC41Nivel1ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel1.objects.all()
    serializer_class = OMC41Nivel1Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC41Nivel2ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel2.objects.all()
    serializer_class = OMC41Nivel2Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC41Nivel3ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel3.objects.all()
    serializer_class = OMC41Nivel3Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC41Nivel4ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel4.objects.all()
    serializer_class = OMC41Nivel4Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC41Nivel5ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel5.objects.all()
    serializer_class = OMC41Nivel5Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class OMC41Nivel6ViewSet(viewsets.ModelViewSet):
    queryset =OMC41Nivel6.objects.all()
    serializer_class = OMC41Nivel6Serializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#VISTAS PARA MATERIALES

#vistas que insertan en base de datos
class CrearMaterial(CreateAPIView):
    serializer_class = MaterialesSerializer
    queryset = Materiales.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearConcreto(CreateAPIView):
    serializer_class = ConcretoSerializer
    queryset = Concreto.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CrearCaracEspe(CreateAPIView):
    serializer_class = CaracEspeSerializer
    queryset = CaracEspe.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#vistas de solo consulta
class ListarMateriales(ListAPIView):
    serializer_class = MaterialesSerializer
    def get_queryset(self):
        return Materiales.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarConcreto(ListAPIView):
    serializer_class = ConcretoSerializer
    def get_queryset(self):
        return Concreto.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarEsfuerzo(ListAPIView):
    serializer_class = EsfuerzoSerializer
    queryset = Esfuerzo.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarValorEsfuerzo(ListAPIView):
    serializer_class = ValorEsfuerzoSerializer
    queryset = ValorEsfuerzo.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarTipoResistencia(ListAPIView):
    serializer_class = TipoResistenciaSerializer
    queryset = TipoResistencia.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarAplPrincipales(ListAPIView):
    serializer_class = AplPrincipalesSerializer
    queryset = AplPrincipales.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarTMA(ListAPIView):
    serializer_class = TMASerializer
    queryset = TMA.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarRevenimiento(ListAPIView):
    serializer_class = RevenimientoSerializer
    queryset = Revenimiento.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarDensidad(ListAPIView):
    serializer_class = DensidadSerializer
    queryset = Densidad.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarSistColocacion(ListAPIView):
    serializer_class = SistColocacionSerializer
    queryset = SistColocacion.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarClasExposicion(ListAPIView):
    serializer_class = ClasExposicionSerializer
    queryset = ClasExposicion.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarFlujoRev(ListAPIView):
    serializer_class = FlujoRevSerializer
    queryset = FlujoRev.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarIonCloruro(ListAPIView):
    serializer_class = IonCloruroSerializer
    queryset = IonCloruro.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarFibraConcre(ListAPIView):
    serializer_class = FibraConcreSerializer
    queryset = FibraConcre.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListarUnidadesMedida(ListAPIView):
    serializer_class = UnidadesMedidaSerializer
    queryset = UnidadesMedida.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]