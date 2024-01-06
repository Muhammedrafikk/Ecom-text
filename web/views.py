from django.shortcuts import render,redirect
from .forms import ContactForm
from products.models import Category, SubCategory
from orders.models import Wishlist

# Create your views here.

def about(request):
    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()


    context = {
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,
       
        
    }   
    return render(request,"web/about.html",context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:contact')  
    else:
        form = ContactForm()

    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()


    context = {
        "form": form,
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,
       
    }
    return render(request, "web/contact.html", context)

