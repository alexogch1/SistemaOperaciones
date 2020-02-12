
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from catalogos.models import Ingred, Corte, Presentacion, Cliente, Marca, CasoEsp, Producto
from salidas.models import TiempoMuertoEnc, ProduccionEnc, ProduccionDet
from tmuertos.models import CausaTM, CategoriaTM

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password':{'write_only':'True'}}

    def create(self,validated_data):
        user= User(
            email=validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


 
class IngredSerializer(serializers.ModelSerializer):

    class Meta:
        model= Ingred
        fields = '__all__'

class CorteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
        )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model= Corte
        fields = '__all__'

class PresentacionSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
        )
    class Meta:
        owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
        model= Presentacion
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
        )
    class Meta:
        model= Cliente
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
        )
    class Meta:
        model= Marca
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = '__all__'

class CasoEspSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = '__all__'

class TiemposMuertosEncSerializer(serializers.ModelSerializer):
    class Meta:
        model= TiempoMuertoEnc
        fields = '__all__'

class CatTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaTM
        fields= '__all__'

class CausaTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CausaTM
        fields= '__all__'
 
class ProduccionEncSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProduccionEnc
        fields = '__all__'

class ProduccionDetSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProduccionDet
        fields = '__all__'