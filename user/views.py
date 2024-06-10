from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.contrib.auth import get_user_model

User = get_user_model()
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Assuming email as USERNAME_FIELD
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_email_verified:
                    auth_login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('base')  # Redirect to home page after successful login
                else:
                    # Email not verified, call verification function
                    verify_email(request, user)  # Pass the authenticated user object
                    messages.warning(request, 'Your email is not verified. Please check your email to log in.')
                    return redirect('verify-email-done')  # Or another appropriate redirect
            else:
                messages.error(request, 'Login failed. Please check your email and password.')
        else:
            messages.error(request, 'Invalid form submission.')  # Handle invalid form data (optional)
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def verify_email(request, user):
    """
    This function sends a verification email to the user.
    It's called after a successful login attempt for unverified users.
    """
    if not user.is_email_verified:
        current_site = get_current_site(request)
        email = user.email
        subject = "Verify Email"
        message = render_to_string('user/verify_email_message.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'scheme': 'http',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            subject, message, to=[email]
        )
        email.content_subtype = 'html'
        email.send()
        messages.warning(request, 'Your email is not verified. Please check your email to log in.')
    else:
        # User is already verified, handle this case (optional)
        messages.success(request, 'Your email is already verified.')
        # Log the user in if not already logged in
        if not request.user.is_authenticated:
           auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('verify-email-done')  # Or another appropriate redirect



from django.contrib.auth import logout as auth_logout 
def logout(request):
    auth_logout(request)  
    messages.success(request, 'You are Logged out. Please Login to access the resources.')# Call the imported logout function
    return redirect('base')



def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.backend = 'email_backend'  # Set the backend here
        auth_login(request, user)
        # No need to save the user object here, it's already saved in the database

        messages.success(request, 'Your email has been verified.')
        auth_login(request, user)  # Log the user in after successful verification
        return redirect('home')  # Redirect to the home page after login
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'user/verify_email_confirm.html')


def verify_email_complete(request):
    return render(request, 'user/verify_email_complete.html')


def verify_email_done(request):
    return render(request, 'user/verify_email_done.html')
