# from django.shortcuts import render

# # Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ChangeAccountView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # success_url = reverse_lazy('news:index')
    template_name = 'users/changeAccount.html'

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('users:changeAccount', kwargs={'pk': userid})



