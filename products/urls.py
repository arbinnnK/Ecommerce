from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products),
    path('details/<id>', views.show_products_details)
]