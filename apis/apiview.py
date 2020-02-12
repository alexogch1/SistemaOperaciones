#from rest_framework.views import APIView
#from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import json
from django.http import JsonResponse

from catalogos.models import Ingred, Corte, Presentacion, Cliente, Marca, CasoEsp, Producto
from salidas.models import TiempoMuertoEnc, ProduccionEnc, ProduccionDet
from tmuertos.models import CausaTM, CategoriaTM
from .serializers import IngredSerializer, CorteSerializer, PresentacionSerializer, \
    ClienteSerializer, MarcaSerializer, PresentacionSerializer, CasoEspSerializer, ProductoSerializer, \
    TiemposMuertosEncSerializer, CatTMSerializer, CausaTMSerializer, \
    ProduccionEncSerializer, ProduccionDetSerializer,\
        CatTMSerializer, CausaTMSerializer,\
             UserSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes=()
    permission_classes=()
    serializer_class = UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email","password" )
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_class = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

#Primeras APIS utilizando serializadores
class ProductoList(APIView):
    def get(self, request):
        producto=Producto.objects.all()
        data=ProductoSerializer(producto,many=True).data
        return Response(data)

class ProductoDetalle(APIView):
    def get(self, request,pk):
        producto=get_object_or_404(Producto, pk=pk)
        data=ProductoSerializer(producto).data
        return Response(data)

#APIS Utilizando vistas genericas (permiten más opciones)
class ProductoList2(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetalle2(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


#APIS para filtrar los tiempos muertos

class CatTMList2(generics.ListCreateAPIView):
    queryset = CategoriaTM.objects.all()
    serializer_class = CatTMSerializer

class CatTMDetalle(generics.RetrieveDestroyAPIView):
    queryset = CategoriaTM.objects.all()
    serializer_class = CatTMSerializer

class CausaTMList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = CausaTM.objects.filter(categoriatm_id=self.kwargs["pk"])
        return queryset
    serializer_class = CausaTMSerializer
    

# APIS de Django Puro

def ingred_resumen_list(request):
    MAX_OBJECTS = 20
    ingred = Ingred.objects.all()[:MAX_OBJECTS]
    data = {"results": list(ingred.values("descripcion_ing","estado"))}
    return JsonResponse(data)
 
def ingred_resumen_detalle(request,pk):
    ingred = get_object_or_404(Ingred, pk=pk)
    data = {"results": {
        "descripcion": ingred.descripcion_ing,
        "estado": ingred.estado
        }}
    return JsonResponse(data)




#APIs para armar la clave y el còdigo del producto
class IngredList(APIView):
    def get(self,request):
        ing= Ingred.objects.all()
        data=IngredSerializer(ing,many=True).data
        return Response(data)

class IngredDetalle(APIView):
    def get(self, request,id_ingred):
        ing=get_object_or_404(Ingred,id_ingred=id_ingred)
        data=IngredSerializer(ing).data
        return Response(data)

class CorteList(APIView):
    def get(self,request):
        corte= Corte.objects.all()
        data=CorteSerializer(corte,many=True).data
        return Response(data)

class CorteDetalle(APIView):
    def get(self, request,id_corte):
        corte=get_object_or_404(Corte,id_corte=id_corte)
        data=CorteSerializer(corte).data
        return Response(data)








#definicion de la clase para una API VIEWSET
class IngredViewSet(viewsets.ModelViewSet):
    queryset = Ingred.objects.all()
    serializer_class = IngredSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class CorteViewSet(viewsets.ModelViewSet):
    queryset = Corte.objects.all()
    serializer_class = CorteSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class PresentaViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class CEViewSet(viewsets.ModelViewSet):
    queryset = CasoEsp.objects.all()
    serializer_class = CasoEspSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = ([IsAuthenticated,IsOwner])

class ProduccionEncViewSet(viewsets.ModelViewSet):
    queryset = ProduccionEnc.objects.all()
    serializer_class=ProduccionEncSerializer
    #permission_classes = (IsAuthenticated, IsOwner)

class ProduccionDetViewSet(viewsets.ModelViewSet):
    queryset = ProduccionDet.objects.all()
    serializer_class=ProduccionDetSerializer
    #permission_classes = (IsAuthenticated, IsOwner)

class CatTMViewSet(viewsets.ModelViewSet):
    queryset=CategoriaTM.objects.all()
    serializer_class =CatTMSerializer
    #permission_classes=(IsAuthenticated, IsOwner)

class CausaTMViewSet(viewsets.ModelViewSet):
    queryset=CausaTM.objects.all()
    serializer_class=CausaTMSerializer
    #permission_classes=(IsAuthenticated,IsOwner)


class IngredApiList(generics.ListCreateAPIView):
    queryset = Ingred.objects.all()
    serializer_class = IngredSerializer

class CorteApiList(generics.ListCreateAPIView):
    queryset = Corte.objects.all()
    serializer_class = CorteSerializer

class PresentacionApiList(generics.ListCreateAPIView):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer

class ClienteApiList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MarcaApiList(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CasoEspApiList(generics.ListCreateAPIView):
    queryset = CasoEsp.objects.all()
    serializer_class = CasoEspSerializer



class IngredSave(generics.CreateAPIView):
        serializer_class = IngredSerializer

class CorteSave(generics.CreateAPIView):
        serializer_class = CorteSerializer

class PresentacionSave(generics.CreateAPIView):
        serializer_class = PresentacionSerializer        

class ClienteSave(generics.CreateAPIView):
        serializer_class = ClienteSerializer

class MarcaSave(generics.CreateAPIView):
        serializer_class = MarcaSerializer

class CasoEspSave(generics.CreateAPIView):
        serializer_class = CasoEspSerializer

class ProductoSave(generics.CreateAPIView):
        serializer_class = ProductoSerializer

class IngredApiDetalle(generics.RetrieveDestroyAPIView):
    queryset = Ingred.objects.all()
    serializer_class = IngredSerializer

class TiemposMuertosEncApiList(generics.ListCreateAPIView):
    queryset = TiempoMuertoEnc.objects.all()
    serializer_class = TiemposMuertosEncSerializer

class TiemposMuertosEncApiDetalle(generics.RetrieveDestroyAPIView):
    queryset = TiempoMuertoEnc.objects.all()
    serializer_class = TiemposMuertosEncSerializer
    
class ProduccionEncApiList(generics.ListCreateAPIView):
    queryset = ProduccionEnc.objects.all()
    serializer_class = ProduccionEncSerializer

class ProduccionEncApiDetalle(generics.RetrieveDestroyAPIView):
    queryset = ProduccionEnc.objects.all()
    serializer_class = ProduccionEncSerializer

class CategoriaTMSave(generics.CreateAPIView):
    serializer_class = CatTMSerializer
 
class CausaTMSave(generics.CreateAPIView):
        serializer_class = CausaTMSerializer



class CausaTMAdd(APIView):
    def post(self,request,cat_pk):
        descripcion = request.data.get("descripcion")
        data = {'categoria_tm': cat_pk, 'descripcion':descripcion}
        serializer = CausaTMSerializer(data=data)
        if serializer.is_valid():
            causa = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
