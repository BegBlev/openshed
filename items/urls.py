from django.urls import path

from . import views

urlpatterns = [
    path('types', views.types_listing),
    path('types/<int:type_id>', views.type_detail),
    path('items', views.items_listing),
    path('items/<int:item_id>', views.item_detail),
    #path('<int:member_id>', views.detail),
    #path('search/', views.search),
]