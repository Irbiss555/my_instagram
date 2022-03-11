from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Profile, UserFollowing


class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Пароль',
        strip=False,
        required=True,
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput,
        label='Повторите пароль',
        strip=False,
        required=True,
    )
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'password_confirm',
            'first_name',
            'email',
        ]


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'avatar',
            'about',
            'phone',
            'gender',
        ]


class UserFollowingForm(forms.ModelForm):
    class Meta:
        model = UserFollowing
        fields = ['user_id', 'following_user_id']


class UserSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск")
