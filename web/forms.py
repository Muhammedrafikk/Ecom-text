from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "First Name" , "required": True}),
            "last_name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Last Name" , "required": True}),
            "company": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Company" , "required": True}),
            "email": widgets.EmailInput(attrs={"class": "form-control", "placeholder": "Email" , "required": True}),
            "phone": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Phone" }),
            "comments": widgets.Textarea(attrs={"class": "form-control","placeholder": "Write your message","required": True})
        
        }
