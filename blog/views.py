from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import transaction
from django.utils import timezone
from django.core.mail import send_mail

from .models import blog

from pages.models import BasePage

def blogList(request):
    basepage = BasePage.objects.get(version = "Default")
    blogs = blog.objects.all().order_by('date')
    return render(request, 'blog/blogList.html', {
        'currentPage': "Blog",
        'blogs': blogs,
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

@login_required
def blogDetail(request, blogID):
    basepage = BasePage.objects.get(version = "Default")
    Blog = blog.objects.get(id=blogID)
    return render(request, 'blog/blogDetail.html', {
    'blog': Blog,
    'currentPage': "Blog",
    'footer': basepage.footer,
    'email': basepage.email,
    'title': basepage.title,
    'facebook': basepage.facebookLink,
    'instagram': basepage.instagramLink,
    'susu': basepage.susuLink,
             })