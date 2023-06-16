from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guns/', views.GunListView.as_view(), name='guns'),
    path('guns/<int:pk>', views.GunDetailView.as_view(), name='gun_detail'),
]