from django.contrib.auth.views import LoginView
from django.shortcuts import render, resolve_url

# Create your views here.
from core import settings


class LoginUserView(LoginView):
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_page'] = 'True'
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        return next_url or resolve_url(settings.LOGIN_REDIRECT_URL)
