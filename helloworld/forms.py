from django import forms


class AddContactForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        required=True,
        label="Enter registered username:",
    )
    name = forms.CharField(
        max_length=20,
        required=True,
        label="Enter Name:",
        help_text="Give this user any name you want...",
    )
