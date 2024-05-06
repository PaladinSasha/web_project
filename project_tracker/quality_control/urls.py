from django.urls import path
from quality_control import views
from tasks import views as views_from_tasks

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_id_detail, name='feature_id_detail')
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_id_detail'),
    path('features/<int:feature_id>/information_project/<int:project_id>/', views_from_tasks.ProjectDetailView.as_view(),
         name='information_project_from_features'),
    path('bugreport/new/', views.create_bugreport, name='create_bugreport'),
    path('features/new/', views.create_featurerequest, name='create_featurerequest')
]