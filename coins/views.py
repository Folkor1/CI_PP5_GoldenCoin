from django.shortcuts import render
from .models import Coins


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.filter(quantity__gt=0)

    context = {
        'coins': coins,

    }

    return render(request, 'coins/coins.html', context)
