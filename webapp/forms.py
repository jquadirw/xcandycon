from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="username", widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password1 = forms.CharField(
        label="password1",
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )
    password2 = forms.CharField(
        label="password2",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),
    )
    first_name = forms.CharField(
        label="firstname", widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        label="lastname", widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
    email = forms.EmailField(
        label="email", widget=forms.TextInput(attrs={"placeholder": "Email Address"}),
    )
    accept = forms.BooleanField(
        label="accept", widget=forms.CheckboxInput(), required=True,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "accept",
        )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        email = cleaned_data.get("email")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        accept = cleaned_data.get("accept")

        if accept is None or accept == False:
            raise forms.ValidationError("Please check the Terms & Conditions to proceed!")

        if not email and not first_name and not last_name:
            raise forms.ValidationError("You have to write something!")


class SignInForm(forms.Form):
    username = forms.CharField(
        label="username", widget=forms.TextInput(attrs={"placeholder": "username"}),
    )
    password = forms.CharField(
        label="password", widget=forms.PasswordInput(attrs={"placeholder": "password"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid login credentials. Please try again.")

        if not user.is_active:
            raise forms.ValidationError(
                "Your account is disabled. Contact AnyValet Support."
            )

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        return user

