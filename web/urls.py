from django.urls import path
from . import views
# from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [

   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
  

]