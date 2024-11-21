from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from cars.models import Products


def catalog(request, category_slug=None):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        cars = Products.objects.all()
    else:
        cars = Products.objects.filter(category__slug=category_slug)
        if not cars.exists():
            raise Http404()


    if order_by and order_by != 'default':
        cars = cars.order_by(order_by)

    paginator = Paginator(cars, 3)
    current_page = paginator.page(int(page))
    # img_size = Products.rendering(100)

    context: dict = {
        'cars': current_page,
        'slug_url': category_slug,
        # 'size': img_size
    }
    return render(request, 'catalog.html', context)



def product(request, product_slug):
    products = Products.objects.get(slug=product_slug)

    context = {
        'product': products,
    }

    return render(request, 'product.html', context=context)