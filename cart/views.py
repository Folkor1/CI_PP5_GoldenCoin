from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from coins.models import Coins


def view_cart(request):
    """
    A view that renders the cart contents
    """

    return render(request, 'cart/cart.html')
