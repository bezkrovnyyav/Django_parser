from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .forms import UserIdForm
from .models import UserInfo
import requests

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = UserInfo
    template_name = 'user_detail.html'
    context_object_name = 'user'

class UserParserView(FormView):
    template_name = 'parser_page.html'
    form_class = UserIdForm
    success_url = reverse_lazy('parser:user_list')

    def form_valid(self, form):
        user_id = form.cleaned_data['user_id']

        if not UserInfo.objects.filter(user_id=user_id).exists():
            user_info = self.parse_user_info(user_id)
            UserInfo.objects.create(user_id=user_id, name=user_info['name'], email=user_info['email'])

        return super().form_valid(form)

    def parse_user_info(self, user_id):
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = requests.get(url)
        user_info = response.json()
        return {'name': user_info['name'], 'email': user_info['email']}
