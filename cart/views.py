from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from coins.models import Coins


def view_cart(request):
    """
    A view that renders the cart contents
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add coins to the cart
    """

    coins = get_object_or_404(Coins, pk=item_id)
    unique = Coins.objects.filter(quantity=1).values_list('id', flat=True)
    coin_quantity = int(request.POST.get('coin_quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if int(item_id) in unique:
            cart[item_id] = 1
            messages.info(request, f'Coin `{coins.name}` already added to cart')
        elif coin_quantity + cart[item_id] > coins.quantity:
            cart[item_id] = coins.quantity
            messages.error(request, f'Sorry, only {coins.quantity} `{coins.name}` are left in stock.')
        else:
            cart[item_id] += coin_quantity
            messages.success(request, f'Updated quantity of coin `{coins.name}` in cart')
    elif coin_quantity > coins.quantity:
        cart[item_id] = coins.quantity
        messages.error(request, f'Sorry, only {coins.quantity} `{coins.name}` are left in stock.')
    else:
        cart[item_id] = coin_quantity
        messages.success(request, f'Coin `{coins.name}` added to cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
