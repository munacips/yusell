from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item, Category, ItemPic
from .forms import SearchForm

def home(request):
    searchform = SearchForm(request.POST or None)
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        items = Item.objects.filter(item_name__icontains=query)
        categories = Category.objects.filter(name__icontains=query)
        cart = request.session.get('cart', {})
        cartlen = len(cart.items())
        searchform = SearchForm()
        context = {
            'items' : items,
            'categories' : categories,
            'cartlen' : cartlen,
            'search' : True,
            'searchform' : searchform,
        }
        return render(request,'main/home.html',context)
    categories = Category.objects.all()
    items = Item.objects.all()
    cart = request.session.get('cart', {})
    cartlen = len(cart.items())
    context = {
        'items' : items,
        'categories' : categories,
        'cartlen' : cartlen,
        'searchform' : searchform,
    }
    return render(request,'main/home.html',context)

def category(request,id):
    searchform = SearchForm(request.POST or None)
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        items = Item.objects.filter(item_name__icontains=query)
        categories = Category.objects.filter(name__icontains=query)
        cart = request.session.get('cart', {})
        cartlen = len(cart.items())
        searchform = SearchForm()
        context = {
            'items' : items,
            'categories' : categories,
            'cartlen' : cartlen,
            'search' : True,
            'searchform' : searchform,
        }
        return render(request,'main/home.html',context)
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    items = Item.objects.filter(category=category)
    cart = request.session.get('cart', {})
    cartlen = len(cart.items())
    context = {
        'items' : items,
        'categories' : categories,
        'category' : category,
        'cartlen' : cartlen,
        'searchform' : searchform,
    }
    return render(request,'main/home.html',context)

def details(request,id):
    searchform = SearchForm(request.POST or None)
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        items = Item.objects.filter(item_name__icontains=query)
        categories = Category.objects.filter(name__icontains=query)
        cart = request.session.get('cart', {})
        cartlen = len(cart.items())
        searchform = SearchForm()
        context = {
            'items' : items,
            'categories' : categories,
            'cartlen' : cartlen,
            'search' : True,
            'searchform' : searchform,
        }
        return render(request,'main/home.html',context)
    item = Item.objects.get(id=id)
    pics = ItemPic.objects.filter(item=item)
    cart = request.session.get('cart', {})
    cartlen = len(cart.items())
    context = {
        'item' : item,
        'pics' : pics,
        'cartlen' : cartlen,
        'searchform' : searchform,
    }
    return render(request,'main/details.html',context)

def add_to_cart(request,id):
    product = Item.objects.get(id=id)
    cart = request.session.get('cart', {})
    cart[product.id] = cart.get(product.id, 0) + 1
    request.session['cart'] = cart
    return redirect('/')

def view_cart(request):
    searchform = SearchForm(request.POST or None)
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        items = Item.objects.filter(item_name__icontains=query)
        categories = Category.objects.filter(name__icontains=query)
        cart = request.session.get('cart', {})
        cartlen = len(cart.items())
        searchform = SearchForm()
        context = {
            'items' : items,
            'categories' : categories,
            'cartlen' : cartlen,
            'search' : True,
            'searchform' : searchform,
        }
        return render(request,'main/home.html',context)
    cart = request.session.get('cart', {})
    cartlen = len(cart.items())
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = Item.objects.get(id=product_id)
        total_price += product.price * quantity
        cart_items.append({'product': product, 'quantity': quantity})
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'searchform' : searchform,
        'cartlen' : cartlen
    }
    return render(request, 'main/cart.html', context)

def remove_from_cart(request,id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart
    return redirect('/')