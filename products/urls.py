from django.urls import path
from . import views
# from .views import ShopDetailView

app_name = "products"

urlpatterns = [
    path("", views.index, name="index"),  
    path("shop/", views.shop_grid, name="shop"),
    path("shop-single/<slug:slug>/", views.shop_single, name="shop-single"),

]