from django import forms
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField(max_length=254)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
class SigninForm(UserCreationForm):
    class Meta:
        # merelasikan form dengan model
        model = User
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ['username', 'password1']
        # mengatur teks label untuk setiap field
        # labels = {
        #     'username': _('Username'),
        #     'password': _('Password')
        # }
        # error_messages = {
        #     'username': {
        #         'required': _("Please enter your username."),
        #     },
        #     'password': {
        #         'required': _("Please enter your password."),
        #     },
        # }