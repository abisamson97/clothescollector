from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes_index, name='index'),
    path('clothes/<int:clothes_id>/', views.clothes_detail, name='detail'),
    path('clothes/create/', views.ClothesCreate.as_view(), name='clothes_create'),
    path('clothes/<int:pk>/update/', views.ClothesUpdate.as_view(), name='clothes_update'),
    path('clothes/<int:pk>/delete/', views.ClothesDelete.as_view(), name='clothes_delete'),
    path('clothes/<int:clothes_id>/add_wearing/', views.add_wearing, name='add_wearing'),
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('clothes/<int:clothes_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
]