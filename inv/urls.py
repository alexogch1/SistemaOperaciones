from django.urls import path

from .views  import CategoriaView, CategoriaNew, CategoriaEdit, \
    CategoriaDel, \
        SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel, SubCategoria_Inactivar, \
            OrigenView, OrigenNew, OrigenEdit, Origen_Inactivar

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name = 'categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name = 'categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name = 'categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDel.as_view(), name = 'categoria_del'),

    path('subcategorias/', SubCategoriaView.as_view(), name = 'subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name = 'subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name = 'subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDel.as_view(), name = 'subcategoria_del'),
    path('subcategorias/inactivar/<int:id>', SubCategoria_Inactivar, name = 'subcategoria_inactivar'),

    path('origenes/', OrigenView.as_view(), name = 'origen_list'),
    path('origenes/new', OrigenNew.as_view(), name = 'origen_new'),
    path('origenes/edit/<int:pk>', OrigenEdit.as_view(), name = 'origen_edit'),
    path('origenes/inactivar/<int:id>', Origen_Inactivar, name = 'origen_inactivar'),

]
