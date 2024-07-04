from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ESUser

class CustomUserCreationForm(forms.ModelForm):
    """Formulário para criar novos usuários."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ESUser
        fields = ('email', 'cpf', 'name', 'birth_date', 'phone', 'user_type')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    """Formulário para atualizar os usuários."""
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = ESUser
        fields = ('email', 'password', 'is_active', 'is_staff', 'cpf', 'name', 'birth_date', 'phone', 'user_type')

    def clean_password(self):
        return self.initial["password"]
