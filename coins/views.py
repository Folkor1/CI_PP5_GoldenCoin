from django.shortcuts import render
from .models import Coins, Metal
from django.db.models import Q


def all_coins(request):
    """
    A view to show all coins
    """
    coins = Coins.objects.filter(quantity__gt=0)
    query = None
    eras = None
    metals = None
    sort = None
    direction = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('coins'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(origin__icontains=query) |
                Q(condition__icontains=query) |
                Q(year__icontains=query)
                )
            coins = coins.filter(queries)

    if 'era' in request.GET:
        eras = request.GET['era'].split(',')
        coins = coins.filter(era__in=eras)
        eras = Coins.objects.filter(name__in=eras)

    if 'metal' in request.GET:
        metals = request.GET['metal'].split(',')
        coins = coins.filter(metal__name__in=metals)
        metals = Metal.objects.filter(name__in=metals)

    context = {
        'coins': coins,
        'search_term': query,
        'current_metals': metals,
    }

    return render(request, 'coins/coins.html', context)
