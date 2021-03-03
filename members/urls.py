from django.urls import path

from . import views

urlpatterns = [
    # Members
    path('members', views.members_listing),
    path('<int:member_id>', views.detail),
    path('search/', views.search),
]
