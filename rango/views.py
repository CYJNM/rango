from django.shortcuts import render
from rango.models import Category
from rango.models import Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)

# def index(request):
#     page_list = Page.objects.order_by('-likkes'[:5])
#     context_dict = {'pages': page_list}
#     return render(request, 'rango/index.html', context_dict=context_dict)

def about(request):
    # return HttpResponse("<a href='/rango/'>index</>")
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)
