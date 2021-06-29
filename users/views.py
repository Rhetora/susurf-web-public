from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from pages.models import BasePage
from .forms import SignUpForm
from django.contrib.auth import get_user_model
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string

def signup(request):
    basepage = BasePage.objects.get(version = "Default")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('users:signupConfirmation')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {
        'form': form,
        'currentPage': None,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                })

def signupConfirmation(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'users/signupConfirmation.html', {
        'currentPage': None,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                })

def login_req(request):
    basepage = BasePage.objects.get(version = "Default")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff == True:
                    try:
                        committeeGroup = Group.objects.get(name='Committee')
                        committeeGroup.user_set.add(user)
                    except ObjectDoesNotExist:
                        pass
                else:
                    if user.groups.filter(name='Committee').exists():
                        user.groups.clear()

                return redirect('pages:home')
            else:
                messages.error(request, "Invalid username or password.")
                messages.error(request, "Or account has not yet been verified.")
        else:
            messages.error(request, "Invalid username or password.")
            messages.error(request, "Or account has not yet been verified.")
    form = AuthenticationForm()
    return render(request, "users/login.html", {
        "form":form,
        'currentPage': None,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                  })

def logout_req(request):
    logout(request)
    return redirect("pages:home")

def password_change(request):
    basepage = BasePage.objects.get(version = "Default")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:passwordChangeConfirmed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "users/password_change.html", {
        "form":form,
        'currentPage': None,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                  })

def passwordChangeConfirmed(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'users/passwordChangeConfirmed.html', {
        'currentPage': None,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                })