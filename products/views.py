from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from . models import Product
from . models import Category
from . models import SubCategory
from . models import Brand
from . models import Color
from orders.models import Wishlist
from django.db.models import Q

# Create your views here.

def index(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    products = Product.objects.all() 

    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()

    context = {
        "is_index": True,
        "categories": categories,
        "subcategory": subcategories,
        "wishlist_count": wishlist_count,
        'product': products,
        'stars': range(1, 6),

    }

    return render(request, "web/index.html", context)


def shop_grid(request):
    subcategories = SubCategory.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all() 

    category_id = request.GET.get('category')
    text_search = request.GET.get('text_search')
    selected_brands = request.GET.getlist('brand')

    price_range = request.GET.get("price-range")
    sort_by = request.GET.get('sort_by', 'all_products')

    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()

    # select_option
    if sort_by == 'High to Low':
        products = products.order_by('-price')
    elif sort_by == 'low_to_high':
        products = products.order_by('price')
    elif sort_by == 'rating':
        products = products.order_by('-rating')


    category_name = None

    if category_id:       
        # category_name = SubCategory.objects.get(id=category_id)
                
        category_name = get_object_or_404(Category, id=category_id)
        
        subcategories = SubCategory.objects.filter(category=category_name)
        
        products = products.filter(subcategory__in=subcategories)


    if text_search:
        products = products.filter(Q(name__icontains=text_search))

    if selected_brands:
        products = products.filter(brand__name__in=selected_brands)

    # Range_price
    if price_range:
        amount = price_range.replace("₹", "")         
        try:
            min_amount, max_amount = map(int, amount.split("-"))
            products = products.filter(
                price__gte=min_amount,
                price__lte=max_amount,
            ).distinct()
        except ValueError:
            print("ValueError")

    # Pagination
    paginator = Paginator(products, 2)
    page_number=request.GET.get('page')
    products=paginator.get_page(page_number)

    context = {
        'colors': colors,
        'brands': brands,
        'selected_brands': selected_brands,
        'product': products,
        'stars': range(1, 6),
        'category_name': category_name,
        'category': categories,
        'subcategory': subcategories, 
        "categories": categories, 
        "subcategory": subcategories,
        "wishlist_count": wishlist_count, 

    }

    return render(request, "web/shop.html", context)


from django.http import Http404

def shop_single(request, slug):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    products = Product.objects.filter(slug=slug)


    if products.exists():

        product = products.first()
    else:
        raise Http404("Product not found or multiple products found.")

    wishlist_items = Wishlist.objects.filter(user=request.user.id)
    wishlist_count = wishlist_items.count()

    context = {
        'p': product,
        'stars': range(1, 6),
        "wishlist_count": wishlist_count,
        "categories": categories,
        "subcategory": subcategories,

    }

    return render(request, "web/shop-single.html", context)


