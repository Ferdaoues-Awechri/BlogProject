from django.urls import path, include
from .views import SignUpView, ProfileView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name="registration/changepassword.html"), name='change_password'),
    path('password-change/done/', TemplateView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
