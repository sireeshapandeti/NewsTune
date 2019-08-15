from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'usa', 'world', 'business', 'opinion', 'health', 'entertainment', 'style', 'travel', 'sports')


class CustomUserChangeForm(UserChangeForm):
    UserChangeForm.password = None
    class Meta:
        model = CustomUser
        fields = ('usa', 'world', 'business', 'opinion', 'health', 'entertainment', 'style', 'travel', 'sports')
