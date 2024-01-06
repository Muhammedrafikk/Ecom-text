from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from products.models import Product
# from .models import Product
from cart.cart import Cart
from . models import Order
from . models import OrderItem
from .models import Wishlist

from products.models import Category,SubCategory

from .models import UserProfile
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your views here.




# cart 
@login_required(login_url="auth_login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    
    
    return redirect("products:shop")


@login_required(login_url="auth_login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("orders:cart_detail")

 
@login_required(login_url="auth_login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("orders:cart_detail")


@login_required(login_url="auth_login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("orders:cart_detail")


@login_required(login_url="auth_login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("orders:cart_detail")


@login_required(login_url="auth_login")
def cart_detail(request):

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    
    wishlist_items = Wishlist.objects.filter(user=request.user.id)

    wishlist_count = wishlist_items.count()

    context = {
        'stars': range(1, 6),
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,
    }
    return render(request, 'web/cart_detail.html',context)


# order
def checkout(request):

    user_orders = Order.objects.filter(user=request.user)

    for user_order in user_orders:
        print(f"Order ID: {user_order.id}")
    
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()


    context = {
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,
        'user_orders': user_orders,
        # 'form': form,
        # 'order': order,
    }

    if request.method == "POST":
        uid = request.session.get('_auth_user_id')

        user = User.objects.get(id=uid)
        
        cart = request.session.get('cart')
        full_name = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        district = request.POST.get("district")
        city = request.POST.get("city")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")

        order = Order(
            user=user,
            full_name=full_name,
            mobile=mobile,
            district=district,
            city=city,
            address=address,
            pincode=pincode,
        )

        order.save()

        for i in cart:
            a = float(cart[i]['price'])
            b = float(cart[i]['quantity'])
            total = a * b

            order_item = OrderItem(
                order=order,
                Product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                qunatity=cart[i]['quantity'], 
                total=total
            )


            order_item.save()     

        request.session['cart'] = {}  

    return render(request, "web/checkout.html", context)


def account_orders(request):
    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        order_items = OrderItem.objects.filter(order__in=orders)
    else:
        order_items = []

    context = {
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,
        'order_items': order_items,
    }   
    return render(request, "web/account-orders.html", context)


@login_required
def account_settings(request):
    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    if request.method == 'POST':
        # Update other fields
        user_profile.name = request.POST.get('name')
        user_profile.email = request.POST.get('email')
        user_profile.email = request.POST.get('firstname')
        user_profile.email = request.POST.get('lastname')

        profile_pic = request.FILES.get('profile_pic')
        if profile_pic:
            user_profile.profile_pic = profile_pic

        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('orders:account-settings')


    context = {
        "wishlist_items": wishlist_items,
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,     
        'user_profile': user_profile,
           
    }   
    return render(request,"web/account-settings.html",context)



def delete_address(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('orders:checkout')


# login and sigup
# @login_required(login_url="auth_login")
# def wishlist(request):
      
#     wishlist_items = Wishlist.objects.filter(user=request.user)
#     wishlist_count = wishlist_items.count()
#     categories = Category.objects.all()
#     subcategories = SubCategory.objects.all()

#     context = {
#         "wishlist_items": wishlist_items,
#         "wishlist_count": wishlist_count,
#         "wishlist_count": wishlist_count,
#         "categories": categories,
#         "subcategory": subcategories,
       
#     }
    
#     return render(request, "web/wishlist.html", context)


# @login_required(login_url="auth_login")
# def add_to_wishlist(request, product_id):
#     user = request.user
#     product = get_object_or_404(Product, id=product_id)

#     if not Wishlist.objects.filter(user=user, product=product).exists():
#         Wishlist.objects.create(user=user, product=product)
#         messages.success(request, "Product added to your wishlist.")
#     else:
#         messages.warning(request, "Product is already in your wishlist.")

#     return redirect("products:shop")


# @login_required(login_url="auth_login")
# def remove_from_wishlist(request, product_id):
#     user = request.user
#     wishlist_item = get_object_or_404(Wishlist, user=user, product_id=product_id)
#     wishlist_item.delete()

#     messages.success(request, "Product removed from your wishlist.")

#     return redirect("orders:wishlist")



from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

#wishlist
class WishlistListView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = "web/wishlist.html"
    context_object_name = "wishlist_items"
    paginate_by = 3

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        wishlist_items = Wishlist.objects.filter(user=self.request.user)
        wishlist_count = wishlist_items.count()
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()

        context = {
            "wishlist_items": wishlist_items,
            "wishlist_count": wishlist_count,
            "categories": categories,
            "subcategories": subcategories,
        }

        # Call the base implementation to merge the new context variables with the existing ones
        context.update(super().get_context_data(**kwargs))

        return context

class AddToWishlistView(View):
    def get(self, request, product_id, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'User not authenticated'}, status=401)
        
        user = request.user
        product = get_object_or_404(Product, id=product_id)

        if not Wishlist.objects.filter(user=user, product=product).exists():
            # Create a new Wishlist object
            Wishlist.objects.create(
                user=user,
                product=product
            )
            return JsonResponse({'message': 'Product Added to Wishlist successfully', 'wishlist_count': Wishlist.objects.filter(user=request.user).count()})
        else:
            return JsonResponse({'message': 'Product is already in the Wishlist.'})


class RemoveFromWishlistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get("product_id")
        user = self.request.user

        wishlist_item = get_object_or_404(Wishlist, user=user, id=product_id)
        wishlist_item.delete()

        return JsonResponse({'message': 'Product Removed from Wishlist successfully','wishlist_count':Wishlist.objects.filter(user=request.user).count()})