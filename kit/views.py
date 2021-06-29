from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone

from pages.models import BasePage
from .models import Surfboard, Wetsuit, Misc_Item

def kitHome(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'kit/kitHome.html', {
        'currentPage': "Kit",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

def kitBorrowing(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'kit/kitBorrowing.html', {
        'currentPage': "Kit",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

def kitCare(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'kit/kitCare.html', {
        'currentPage': "Kit",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

@login_required
def kitLogout(request):
    basepage = BasePage.objects.get(version = "Default")
    surfboards = Surfboard.objects.all().order_by('IDnumber')
    wetsuits = Wetsuit.objects.all().order_by('IDnumber')
    misc = Misc_Item.objects.all().order_by('IDnumber')
    user = request.user
    return render(request, 'kit/kitLogout.html', {
        'surfboards': surfboards,
        'wetsuits': wetsuits,
        'misc': misc,
        'user': user,
        'currentPage': "Kit",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

@login_required
def takeBoard(request, ID):
    board = Surfboard.objects.get(IDnumber=ID)
    if board.location == "Container":
        board.location = request.user.email
        board.pastBorrowers = board.pastBorrowers + request.user.first_name + " " + request.user.last_name + " - "+ request.user.email +" - " + timezone.now().strftime("%Y-%m-%d %H:%M:%S %Z") + ", \r\n"
        board.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')

@login_required
def returnBoard(request, ID):
    board = Surfboard.objects.get(IDnumber=ID)
    if board.location == request.user.email:
        board.location = "Container"
        board.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')

@login_required
def takeSuit(request, ID):
    suit = Wetsuit.objects.get(IDnumber=ID)
    if suit.location == "Container":
        suit.location = request.user.email
        suit.pastBorrowers = suit.pastBorrowers + request.user.first_name + " " + request.user.last_name + " - "+ request.user.email +" - " + timezone.now().strftime("%Y-%m-%d %H:%M:%S %Z") + ", \r\n"
        suit.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')

@login_required
def returnSuit(request, ID):
    suit = Wetsuit.objects.get(IDnumber=ID)
    if suit.location == request.user.email:
        suit.location = "Container"
        suit.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')

@login_required
def takeMisc(request, ID):
    misc = Misc_Item.objects.get(IDnumber=ID)
    if misc.location == "Container":
        misc.location = request.user.email
        misc.pastBorrowers = misc.pastBorrowers + request.user.first_name + " " + request.user.last_name + " - "+ request.user.email +" - " + timezone.now().strftime("%Y-%m-%d %H:%M:%S %Z") + ", \r\n"
        misc.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')

@login_required
def returnMisc(request, ID):
    misc = Misc_Item.objects.get(IDnumber=ID)
    if misc.location == request.user.email:
        misc.location = "Container"
        misc.save()
        return redirect('kit:kitLogout')
    else:
        return redirect('kit:kitLogout')