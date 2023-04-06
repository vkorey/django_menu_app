from django.shortcuts import render


def index(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'index.html', context)


def deals(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'deals.html', context)


def about(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'about.html', context)


def sale(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'sale.html', context)


def free(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'free.html', context)


def freee(request):
    context = {
        'current_url': request.path
    }
    return render(request, 'freee.html', context)
