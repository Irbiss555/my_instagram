from urllib.parse import urlencode

from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import render, resolve_url, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView

from accounts.forms import MyUserCreationForm, ProfileCreateForm, UserSearchForm
from core import settings


class LoginUserView(LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/registration/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_page'] = 'True'
        return context

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        return next_url or resolve_url(settings.LOGIN_REDIRECT_URL)


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'accounts/registration/user_create.html'
    form_class = MyUserCreationForm

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['register_page'] = 'True'
        if 'profile_form' not in context:
            context['profile_form'] = self.get_profile_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        user = form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return render(self.request, self.template_name, context=context)

    def get_profile_form(self):
        form_kwargs = {}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileCreateForm(**form_kwargs)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('accounts:login')
        return next_url


class UserListView(ListView):
    model = get_user_model()
    template_name = 'accounts/user_list.html'
    context_object_name = 'user_objects'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_superuser=1)
        if self.search_value:
            query = (
                    Q(username__icontains=self.search_value) |
                    Q(first_name__icontains=self.search_value) |
                    Q(email__icontains=self.search_value)
            )
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return UserSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None
