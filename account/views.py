from django.shortcuts import render
from products.models import Category,SubCategory
from orders.models import Wishlist


def login(request):
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
    return render(request, "registration/login.html", context)


def registration_form(request):
    context = {"is_index": True}
    return render(request, "registration/registration_form.html", context)