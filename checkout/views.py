from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from coins.models import Coins
from .models import Order, OrderLineItem
from .forms import OrderForm
from django.views.decorators.http import require_POST
from cart.contexts import cart_contents
import json


def checkout(request):
    """
    View the checkout page
    """

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_nr': request.POST['phone_nr'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            for item_id, item_data in cart.items():
                try:
                    coins = Coins.objects.get(id=item_id)
                    coin = get_object_or_404(Coins, id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            coins=coins,
                            coin_quantity=item_data,
                        )
                        coin.quantity = coin.quantity - item_data
                        coin.save()
                        order_line_item.save()
                except Coins.DoesNotExist:
                    messages.error(request, (
                        "One of the coins in cart wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_nr]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in cart at the moment")
            return redirect(reverse('coins'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']

    template = 'checkout/checkout.html'
    context = {

    }

    return render(request, template, context)
