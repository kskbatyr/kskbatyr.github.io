from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class Placeholder(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Placeholder, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, ):
                    field.widget.attrs.update({'placeholder': field.label})


class SignUpForm(Placeholder):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Пароль', 'id':'password'}), )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Подтверждение пароля', 'class': 'form-control', 'id':'confirm_password'}), )
    class Meta:
        model = Profile
        widgets = {
            'email': forms.TextInput(attrs={'type': 'email', 'placeholder': '*Email'}),
        }
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'home', 'apartment', 'contract', 'password', 'password2', )


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': '*Email', 'type': 'email'}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Пароль'}),)