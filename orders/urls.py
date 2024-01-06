from django.urls import path
from . import views
# from django.views.generic import TemplateView
# from .views import wishlist, add_to_wishlist, remove_from_wishlist


app_name = "orders"

urlpatterns = [
    
    path("checkout/", views.checkout, name="checkout"),

    # path('wishlist/', wishlist, name='wishlist'),
    # path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    # path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    path("shop/wishlist/", views.WishlistListView.as_view(), name="wishlist"),
    path('shop/wishlist/add/<int:product_id>/', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path("shop/wishlist/remove/<int:product_id>/",views.RemoveFromWishlistView.as_view(),name="remove_from_wishlist"),
    
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),

    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
   
    # order
    path("account-orders", views.account_orders, name="account-orders"),
    path("account-settings", views.account_settings, name="account-settings"),

   # update
   #path('update_address/<int:order_id>/', views.update_address, name='update_address'),

    # address delete
   path('delete_address/<int:order_id>/', views.delete_address, name='delete_address'),

]