from django import forms

from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
	username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
	email = forms.CharField(
		required = True,
        label = 'Email',
        max_length = 32,)
	password = forms.CharField(
		required = True,
        label = 'Password',
        max_length = 32,
        widget=forms.PasswordInput)
class Meta:
        model = User
        fields = ('username', 'email', 'password')

class donationForm(forms.Form):
    Name = forms.CharField(
        required = True,
        label = 'Name',
        max_length = 15,
 )
    Amount = forms.IntegerField(
        required = True,
        label = 'Amount',



        )

        



