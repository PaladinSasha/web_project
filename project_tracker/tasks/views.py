from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')
    main_quality_url = reverse('tasks:quality_control')
    html = (f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a><br>"
            f"<a href='{main_quality_url}'>Страница контроля качества</a>")
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")
