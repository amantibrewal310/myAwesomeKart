from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('products/<int:myid>',views.product_view,name='product'), # <int: id> use for passing the variable in the url
    path('checkout/',views.checkout_view,name='checkout'),
]