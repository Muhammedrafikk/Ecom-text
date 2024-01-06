from django.contrib import admin

from . models import Order
from . models import OrderItem
from .models import Wishlist

# Register your models here.

class orderitemtube(admin.TabularInline):
    model=OrderItem
    extra = 0

class orderadmin(admin.ModelAdmin):
   inlines=[orderitemtube]

admin.site.register(Order,orderadmin)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "Product","qunatity","price","total","price")
    list_display = ("order", "Product","qunatity","price","total","price")
    list_filter = ("order", "Product","qunatity","price","total","price")
    search_fields = ( "order", "Product", "qunatity","price","total","price")


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product', )
    search_fields = ('user__username', 'product__name' )
