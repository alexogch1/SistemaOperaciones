
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from rest_framework_swagger.views import get_swagger_view

eschema_view = get_swagger_view(title='RestFul Api Mar Bran' )

from rest_framework_simplejwt import views as jwt_views
from rest_framework.documentation import include_docs_urls

from .apiview import UserCreate, LoginView, \
     IngredApiList, \
    IngredViewSet, CorteViewSet, PresentaViewSet, \
        ClienteViewSet, MarcaViewSet, CEViewSet, ProductoViewSet, \
            ProduccionEncViewSet, ProduccionDetViewSet, \
                CatTMViewSet, CausaTMViewSet, \
CorteApiList, PresentacionApiList, ClienteApiList, MarcaApiList, CasoEspApiList,\
    ProductoList, ProductoDetalle, \
    ProductoList2, ProductoDetalle2, CatTMList2,\
    IngredSave, CorteSave, PresentacionSave, ClienteSave, MarcaSave, CasoEspSave, ProductoSave, \
        IngredApiDetalle, \
TiemposMuertosEncApiList, TiemposMuertosEncApiDetalle, \
    ProduccionEncApiList, ProduccionEncApiDetalle, ProduccionEncApiList, ProduccionEncApiDetalle, \
        CausaTMSave, CategoriaTMSave, CausaTMAdd,\
            CatTMDetalle, CausaTMList, CausaTMAdd, \
                ingred_resumen_list, ingred_resumen_detalle
            
            
from rest_framework.authtoken import views

router = DefaultRouter()
#router.register ('v2/Ingreds',IngredViewSet,base_name='Ingreds'),
#router.register ('v2/Cortes',CorteViewSet,base_name='Cortes')
#router.register ('v2/Presenta',PresentaViewSet,base_name='Presentacion')
#router.register ('v2/Cliente',ClienteViewSet,base_name='Cliente')
#router.register ('v2/Marca',MarcaViewSet,base_name='Marca')
#router.register ('v2/CE',CEViewSet,base_name='CasoEspe')
#router.register('v2/Producto',ProductoViewSet, base_name='Products')
#router.register('v2/ProduccionEnc',ProduccionEncViewSet, base_name='ProdEnc')
#router.register('v2/ProduccionDet',ProduccionDetViewSet, base_name='ProdDet')
#router.register('v2/CatTM',CatTMViewSet,base_name='CatTM')
#router.register('v2/CausaTM',CausaTMViewSet,base_name='CausaTM')


urlpatterns = [
    # estas dos rutas son para las apis que se crearon django puro (sin rest framework)
    #path('v7/ingredientes/', ingred_resumen_list, name='ingrediente_resumen_list'),
    #path('v7/ingredientes/<int:pk>', ingred_resumen_detalle, name='ingrediente_resumen_detqlle'),

    
    #API para crear un usuario
    path('v0/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    #API para login en el sistema
    path('v0/login/', LoginView.as_view(), name='login'),

    #API para obtener el Token, esta no se usa porque se está obteniendo con jwt_view
    #path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
 
    path('v6/Productos2/', ProductoList2.as_view(),name='Productos_list2'),
    path('v6/Productos2/<int:pk>', ProductoDetalle2.as_view(),name='Productos_Detalle2' ),

    # estas dos rutas son para ver las tablas de los tiempos muertos (causas y categorías)
    path('v6/CatTM2/', CatTMList2.as_view(),name='CatTM_list2' ),
    path('v6/CatTM2/<int:pk>/causatm/', CausaTMList.as_view(),name='cattm_list' ),
    
    #API para crear una categoria de tiempo muerto
    path('v6/CatTM2/<int:cat_pk>/addcausatm/', CausaTMAdd.as_view(),name='causatm_apiview' ),



    path('v1/TiemposMuertosEnc/', TiemposMuertosEncApiList.as_view(),name='tiempos_muertos_api_list' ),
    path('v1/TiemposMuertosEnc/<int:pk>', TiemposMuertosEncApiDetalle.as_view(),name='Tiempos_muetos_api_detalle' ),

    path('v1/ProduccionEnc/', ProduccionEncApiList.as_view(),name='produccion_api_list' ),
    path('v1/ProduccionEnc/<int:pk>', ProduccionEncApiDetalle.as_view(),name='produccion_api_detalle' ),

    #path('v1/causasTM/', CausaTMSave.as_view(),name='causaTM_save' ),
    #path('v1/categoriasTM/', CategoriaTMSave.as_view(),name='categoriaTM_save' ),

    

    #rutas para tiempos muertos
    path('v1/catTM/<int:pk>', CatTMDetalle.as_view(),name='cat_tm_list' ),
    path('v1/catTM/<int:pk>/causaTM/', CausaTMList.as_view(),name='causa_tm_list' ),
    path('v1/categoriasTM/<int:cat_pk>/addcausatm/', CausaTMAdd.as_view(),name='causaTM_apiview' ),

    path('swagger-docs/', eschema_view),
    path('coreapi-docs',include_docs_urls(title='Documentacion Apis MarBran')),
    
    path('v0/token/', jwt_views.TokenObtainPairView.as_view(),name='token_obtain' ),
    path('v0/token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh' ),
]

urlpatterns += router.urls