from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from quality_control.models import BugReport, FeatureRequest


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br>"
            f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br>"
                f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = f"<h1>Cписок отчетов об ошибках</h1><ul>"
    for bug in bugs:
        bugs_html += f"<li><a href={bug.id}>{bug.title}</a>, status={bug.status}</li>"
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    feature_html = f"<h1>Cписок запросов на улучшение</h1><ul>"
    for feature in features:
        feature_html += f"<li><a href={feature.id}>{feature.title}</a>, status={feature.status}</li>"
    feature_html += "</ul>"
    return HttpResponse(feature_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = (f'<h1>{bug.title}</h1> <p>description: {bug.description}</p> <p>status={bug.status}</p>'
                         f'task={bug.task}, project={bug.project}')
        return HttpResponse(response_html)


class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = (f'<h1>{feature.title}</h1> <p>description: {feature.description}</p> '
                         f'<p>status={feature.status}</p><p>priority={feature.priority}</p>'
                         f'task={feature.task}, '
                         f'project=<a href=information_project/{feature.project.id}>{feature.project}</a>')
        return HttpResponse(response_html)


'''def feature_id_detail(request, feature_id):
    return HttpResponse(f'<h1>Детали улучшения {feature_id}</h1>')'''


'''def bug_detail(request, bug_id):
    return HttpResponse(f'<h1>Детали бага {bug_id}</h1>')'''