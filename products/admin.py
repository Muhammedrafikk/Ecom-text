from django.contrib import admin
from django.utils.safestring import mark_safe
# add models here

from .models import ProductImage
# from .models import ProductColor


# Register your models here.

from .models import Product
from .models import Category
from .models import SubCategory
from .models import Brand
from .models import Color



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    
# class ProductColorInline(admin.TabularInline):
#     model = ProductColor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=['title']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields=['name']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['add_color', 'tag_color']
    search_fields=['tag_color']
    autocomplete_fields = []
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    # ProductColorInline
    
    autocomplete_fields = ['subcategory', 'color', 'brand']
    prepopulated_fields = {'slug': ('name',)}

    list_filter = ("subcategory", "color", "brand")
    list_display = ("name","image_preview", "price")      
    search_fields = ("name","subcategory__name")

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:70px;object-fit:contain;">'
            )
        return ""

    image_preview.short_description = 'Image Preview'

