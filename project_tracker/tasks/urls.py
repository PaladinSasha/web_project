from django.urls import path
from tasks import views
from quality_control import views as views_from_quality

app_name = 'tasks'

urlpatterns = [
    # path('', views.index),
    path('quality_control/', views_from_quality.index, name='quality_control'),
    # path('projects/', views.projects_list, name='projects_list'),
    # path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    # path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_details, name='task_detail'),

    path('', views.IndexView.as_view()),
    path('projects/', views.ProjectListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
]
