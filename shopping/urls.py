from django.urls import path
from shopping import views

urlpatterns = [
    path('add_to_wishlist/<pid>', views.add_to_wishlist, name='aw'),
    path('remove_from_wishlist', views.remove_from_wishlist, name='rw'),
    path('add_to_cart/<pid>/<qty>', views.add_to_cart, name='ac'),
    path('remove_from_cart', views.remove_from_cart, name='rc'),
    path('checkout', views.checkout, name='checkout'),
    path('comment', views.comment, name='comment'),
    path('review', views.review, name='review'),
    path('user_wishlist', views.show_wishlist, name='wishlist'),
    path('user_cart', views.show_cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]