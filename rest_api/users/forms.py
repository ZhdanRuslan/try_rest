from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustUser
        fields = UserChangeForm.Meta.fields
