from django.urls import path
from . import views

urlpatterns = [
    path('content/<section>', views.show_content, name='content')
]