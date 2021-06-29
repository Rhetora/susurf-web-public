from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import transaction
from django.utils import timezone
from django.core.mail import send_mail


from .models import Event
from .forms import weekendSignupForm, abroadSignupForm, beginnerSignupForm

from pages.models import BasePage


def eventsPage(request):
    basepage = BasePage.objects.get(version = "Default")
    futureEvents = Event.objects.all().order_by('startDateTime', 'name').filter(publishDateTime__lte=timezone.now()).filter(startDateTime__gte=timezone.now())
    pastEvents = Event.objects.all().order_by('-startDateTime', 'name').filter(publishDateTime__lte=timezone.now()).filter(startDateTime__lt=timezone.now())
    return render(request, 'events/eventsPage.html', {
        'futurelist': futureEvents,
        'pastlist': pastEvents,
        'currentPage': "Events",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

def eventDetail(request, eventID):
    basepage = BasePage.objects.get(version = "Default")
    event = Event.objects.get(id=eventID)
    signup_active = False
    if event.signupRequired == True:
        if event.signupPublish == None:
            event.signupPublish = timezone.now()
            event.save()
        if event.signupClose == None:
            event.signupClose = timezone.now() + timezone.timedelta(days=14)
            event.save()
        if event.signupPublish <= timezone.now() < event.signupClose:
            signup_active = True
    return render(request, 'events/event_detail.html', {
    'event': event,
    'signup_active': signup_active,
    'currentPage': "Events",
    'footer': basepage.footer,
    'email': basepage.email,
    'title': basepage.title,
    'facebook': basepage.facebookLink,
    'instagram': basepage.instagramLink,
    'susu': basepage.susuLink,
             })

@login_required
def signup(request, eventID):
    basepage = BasePage.objects.get(version = "Default")
    event = Event.objects.get(id=eventID)

    if event.signupRequired == True:
        if event.signupPublish <= timezone.now() < event.signupClose:
            if event.event_type == 'Weekend Trip':
                if request.method == 'POST':
                    form = weekendSignupForm(request.POST)
                    if form.is_valid():
                        signupInstance = form.save()
                        signupInstance.user = request.user
                        signupInstance.save()
                        
                        event.weekendSignups.add(signupInstance)

                        #Confirmation Email
                        send_mail(
                            'Signup for {}'.format(event.name),
                            'Thanks for signing up for {}.\n\nThis email is not confirmation that you have a place on this {}.\nYou will be added to a group on Facebook if you have successfully made it on the event.\n\nIf you have any questions email info@susurf.co.uk'.format(event.name, event.event_type),
                            'enquiries.susurf@gmail.com',
                            [signupInstance.user.email],
                            fail_silently=True,
                        )

                        return redirect('events:confirmation')
                else:
                    form = weekendSignupForm()

            if event.event_type == 'Abroad Trip':
                if request.method == 'POST':
                    form = abroadSignupForm(request.POST)
                    if form.is_valid():
                        signupInstance = form.save()
                        signupInstance.user = request.user
                        signupInstance.save()
                        
                        event.abroadSignups.add(signupInstance)

                        #Confirmation Email
                        send_mail(
                            'Signup for {}'.format(event.name),
                            'Thanks for signing up for {}.\n\nThis email is not confirmation that you have a place on this {}.\nYou will be added to a group on Facebook if you have successfully made it on the event.\n\nIf you have any questions email info@susurf.co.uk'.format(event.name, event.event_type),
                            'enquiries.susurf@gmail.com',
                            [signupInstance.user.email],
                            fail_silently=False,
                        )

                        return redirect('events:confirmation')
                else:
                    form = abroadSignupForm()

            if event.event_type == 'Beginner Session':
                if request.method == 'POST':
                    form = beginnerSignupForm(request.POST)
                    if form.is_valid():
                        signupInstance = form.save()
                        signupInstance.user = request.user
                        signupInstance.save()
                        
                        event.beginnerSignups.add(signupInstance)

                        #Confirmation Email
                        send_mail(
                            'Signup for {}'.format(event.name),
                            'Thanks for signing up for {}.\n\nThis email is not confirmation that you have a place on this {}.\nYou will be added to a group on Facebook if you have successfully made it on the event.\n\nIf you have any questions email info@susurf.co.uk'.format(event.name, event.event_type),
                            'enquiries.susurf@gmail.com',
                            [signupInstance.user.email],
                            fail_silently=False,
                        )

                        return redirect('events:confirmation')
                else:
                    form = beginnerSignupForm()

            return render(request, 'events/eventSignup.html', {
                "form": form,
                "event": event,
                'currentPage': "Events",
                'footer': basepage.footer,
                'email': basepage.email,
                'title': basepage.title,
                'facebook': basepage.facebookLink,
                'instagram': basepage.instagramLink,
                'susu': basepage.susuLink
                          })
        else:
            return redirect('events:events') 
    else:
        return redirect('events:events')         

def signupConfirmation(request):
    basepage = BasePage.objects.get(version = "Default")
    return render(request, 'events/signupConfirmation.html', {
        'currentPage': "Events",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })

def eventAdmin(request, eventID):
    basepage = BasePage.objects.get(version = "Default")
    event = Event.objects.get(id=eventID)

    if event.event_type == 'Weekend Trip':
        signups = event.weekendSignups.all()
    if event.event_type == 'Abroad Trip':
        signups = event.abroadSignups.all()
    if event.event_type == 'Beginner Session':
        signups = event.beginnerSignups.all()

    if request.user.is_staff:
        return render(request, 'events/event_admin.html', {
        'event': event,
        'signups': signups,
        'currentPage': "Events",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,
                 })
    else:
        return redirect('events:events')