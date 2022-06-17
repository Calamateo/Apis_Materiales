from dataclasses import fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers 
from ApisGenerate.models import *

#SERIALIZERS PARA EL OMNICLAS 23

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email','groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'url']
        
        
# class OmniClass23Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = OmniClass23
#         fields = ['idOmc23', 'numMat', 'Codigo', 'descriEng', 'descriSpa', 'Nivel', 'regFinal']

class OMC23Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel1
        fields = '__all__'


class OMC23Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel2
        fields = [ 'idOmc23N2', 'numMat', 'Codigo', 'descriSpa', 'descriEng','definicionEng', 'definicionSpa', 'ejemploEng', 'ejemploSpa', 'regFinal', 'fk_Omc23N1']

class OMC23Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel3
        fields = [ 'idOmc23N3', 'numMat', 'Codigo', 'descriSpa', 'descriEng','definicionEng', 'definicionSpa', 'ejemploEng', 'ejemploSpa', 'regFinal', 'fk_Omc23N2']
    
class OMC23Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel4
        fields = [ 'idOmc23N4', 'numMat', 'Codigo', 'descriSpa', 'descriEng', 'definicionEng', 'definicionSpa', 'ejemploEng', 'ejemploSpa', 'regFinal', 'fk_Omc23N3']
    
class OMC23Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel5
        fields = [ 'idOmc23N5', 'numMat', 'Codigo', 'descriSpa', 'descriEng', 'definicionEng', 'definicionSpa', 'ejemploEng', 'ejemploSpa', 'regFinal', 'fk_Omc23N4']
    
class OMC23Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel6
        fields = [ 'idOmc23N6', 'numMat', 'Codigo', 'descriSpa', 'descriEng', 'definicionEng', 'definicionSpa', 'ejemploEng', 'ejemploSpa', 'regFinal', 'fk_Omc23N5']

#SERIALIZERS PARA EL OMNILCAS 41

class OMC41Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel1
        fields = [ 'idOmc41N1', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa']

class OMC41Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel2
        fields = [ 'idOmc41N2', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa','fk_Omc41N1']

class OMC41Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel3
        fields = [ 'idOmc41N3', 'numMat', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa', 'regFinal', 'fk_Omc41N2']

class OMC41Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel4
        fields = [ 'idOmc41N4', 'numMat', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa', 'regFinal', 'fk_Omc41N3']

class OMC41Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel5
        fields = [ 'idOmc41N5', 'numMat', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa', 'regFinal', 'fk_Omc41N4']

class OMC41Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel6
        fields = [ 'idOmc41N6', 'numMat', 'Codigo', 'nombreSpa', 'nombreEng', 'definicionEng', 'definicionSpa', 'regFinal', 'fk_Omc41N5']

#SERIALIZERS CORRESPONDIENTES A ENTIDADES RELACIONADAS A MATERIALES

class MaterialesSerializer(serializers.ModelSerializer):  #ESTE ME DEBERIA SERVIR PARA GENERAR EL CONSECUTIVO
    class Meta:
        model = Materiales
        fields = '__all__'

class ConcretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concreto
        fields = '__all__'

class CaracEspeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracEspe
        fields = '__all__'

class EsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esfuerzo
        fields = '__all__'

class ValorEsfuerzoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorEsfuerzo
        fields = '__all__'

class TipoResistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResistencia
        fields = '__all__'

class AplPrincipalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplPrincipales
        fields = '__all__'

class TMASerializer(serializers.ModelSerializer):
    class Meta:
        model = TMA
        fields = '__all__'

class RevenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenimiento
        fields = '__all__'

class DensidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Densidad
        fields = '__all__'

class SistColocacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistColocacion
        fields = '__all__'

class ClasExposicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClasExposicion
        fields = '__all__'

class FlujoRevSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlujoRev
        fields = '__all__'

class IonCloruroSerializer(serializers.ModelSerializer):
    class Meta:
        model = IonCloruro
        fields = '__all__'

class FibraConcreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibraConcre
        fields = '__all__'

class UnidadesMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesMedida
        fields = '__all__'
