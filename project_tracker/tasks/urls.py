from django.urls import path
from tasks import views
from quality_control import views as views_from_quality

app_name = 'tasks'

urlpatterns = [
    path('', views.index),
    path('another/', views.another_page, name='another_page'),
    path('quality_control/', views_from_quality.index, name='quality_control'),
]