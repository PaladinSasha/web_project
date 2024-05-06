from django import forms


class FeedbackForm(forms.Form):
    """ Пользовательская форма для сбора отзывов """
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')  # Валидация электронной почты
    # forms.Textarea указывает, что поле должно быть многострочным текстовым полем
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')


from django.forms import ModelForm
from tasks.models import Project, Task


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee']
