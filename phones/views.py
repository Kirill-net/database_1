from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort', '')

    if sort == '':
        context = {'phones': phones}
        return render(request, template, context)
    elif sort == 'name':
        sort_phones = phones.order_by('name')
        context = {'phones': sort_phones}
        return render(request, template, context)
    elif sort == 'min_price':
        sort_phones = phones.order_by('price')
        context = {'phones': sort_phones}
        return render(request, template, context)
    elif sort == 'max_price':
        sort_phones = phones.order_by('-price')
        context = {'phones': sort_phones}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phone': phones}
    return render(request, template, context)


