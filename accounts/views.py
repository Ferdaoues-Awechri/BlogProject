from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect 

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(PermissionRequiredMixin,LoginRequiredMixin, TemplateView, ):
    template_name = 'registration/profile.html'
    permission_required = 'auth.view_user'


    # def test_func(self):
    #     return self.request.user.is_superuser

    # def handle_no_permission(self):
    #     messages.error(self.request, "Access denied: Superuser only.")
    #     return redirect('home')

