from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove all password validation messages
        self.fields['password1'].help_text = None
    

    class Meta:
        model = User
        fields = ('username', 'password1', 'first_name', 'last_name', 'phone', 'email')

    def clean(self):
        # Call the parent clean() method to perform the default validation.
        cleaned_data = super().clean()

        # Remove the check for password confirmation by clearing the error.
        self.errors.pop('password2', None)

        return cleaned_data
