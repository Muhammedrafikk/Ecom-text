from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = "account"

urlpatterns = [
    
     path("login", views.login, name="login"),
     path("registration_form", views.registration_form, name="registration_form"),

]