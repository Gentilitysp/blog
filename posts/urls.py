from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Handle the root URL
    path('<str:page>/', views.dynamic_page, name='dynamic_page'),
]

    
    # path('category/', views.category, name='category'),
    # path('contact/', views.contact, name='contact'),
    # path('singlepost/', views.singlepost, name='singlepost'),
    # path('starterpage/', views.starterpage, name='starterpage'),