from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name","company","email","phone")
    list_display = ("first_name", "last_name","company","email","phone")
    list_filter = ("first_name", "last_name","company","email","phone")
    search_fields = ( "first_name", "last_name", "company","email","phone")


       