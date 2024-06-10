from django.contrib.auth import get_user_model
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid email or password')
        
        if not user.check_password(password):
            raise forms.ValidationError('Invalid email or password')

        return cleaned_data
