from django.shortcuts import render
from .models import Coins, Metal


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.filter(quantity__gt=0)
    metals = None

    context = {
        'coins': coins,
        'current_metals': metals,

    }

    return render(request, 'coins/coins.html', context)
