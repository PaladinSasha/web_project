from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from tasks.models import Project, Task


def index(request):
    return render(request, "tasks/index.html")


def projects_list(request):
    projects = Project.objects.all()
    return render(request, "tasks/projects_list.html", {'project_list': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "tasks/project_detail.html", {'project': project})


def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, "tasks/task_detail.html", {'task': task})


from tasks.forms import FeedbackForm, ProjectForm, TaskForm


def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            form.save()
            return redirect('tasks:project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_create.html', {'form': form})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['info@example.com']
            recipients.append(email)

            send_mail(subject, message, email, recipients)

            return redirect('/tasks')
    else:
        form = FeedbackForm()
    return render(request, 'tasks/feedback.html', {'form': form})


from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tasks/index.html")


from django.views.generic import ListView


class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'


from django.views.generic import DetailView


class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'  # Указывает что идентификатор проекта в url будет передан как project_id
    template_name = 'tasks/project_detail.html'


class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'










'''def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")'''