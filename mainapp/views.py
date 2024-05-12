import datetime

from django.shortcuts import render


def main(request):
    title = "главная"
    products = [
        {
            "name": "Отличный стул",
            "desc": "Расположитесь комфортно.",
            "image_src": "product-1.jpg",
            "image_href": "/product/1/",
            "alt": "продукт 1",
        },
        {
            "name": "Стул повышенного качества",
            "desc": "Не оторваться.",
            "image_src": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2",
        },
    ]
    content = {'title': title, 'products': products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = 'продукты'
    content = {'title': title}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = 'контакты'
    content = {'title': title}
    visit_date = datetime.datetime.now()
    return render(request, "mainapp/contact.html", content)