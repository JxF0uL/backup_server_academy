from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        label="Grupo",
        required=False,
        help_text="Selecione um grupo para o usuário"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'groups']
