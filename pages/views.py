from django.shortcuts import render
from django.http import HttpResponse

from .models import BasePage, HomePage, CommitteePage, AboutPage, JoinPage, SpotsPage, spots

# Create your views here.
def homePage(request):
    basepage = BasePage.objects.get(version = "Default")
    homepage = HomePage.objects.get(version = "Default")
    return render(request, 'pages/homePage.html', {
        'currentPage': "Home",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                 })

def aboutPage(request):
    basepage = BasePage.objects.get(version = "Default")
    aboutpage = AboutPage.objects.get(version = "Default")
    return render(request, 'pages/aboutPage.html', {
        'currentPage': "About",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,

        'about': aboutpage.aboutUs,
        'what': aboutpage.whatWeDo,
        'learn': aboutpage.learnMore,
        'pic1': aboutpage.pic1,
        'pic2': aboutpage.pic2,
        'pic3': aboutpage.pic3,
                 })

def committeePage(request):
    basepage = BasePage.objects.get(version = "Default")
    committeepage  = CommitteePage.objects.get(version = "Default")
    return render(request, 'pages/committeePage.html', {
        'currentPage': "Committee",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink,

        'presName': committeepage.PresidentName,
        'presBio': committeepage.PresidentBio,
        'presPic': committeepage.PresidentPic,
        'vpName': committeepage.VPName,
        'vpBio': committeepage.VPBio,
        'vpPic': committeepage.VPPic,
        'treasName': committeepage.TreasurerName,
        'treasBio': committeepage.TreasurerBio,
        'treasPic': committeepage.TreasurerPic,
        'trip1Name': committeepage.Trip1Name,
        'trip1Bio': committeepage.Trip1Bio,
        'trip1Pic': committeepage.Trip1Pic,
        'trip2Name': committeepage.Trip2Name,
        'trip2Bio': committeepage.Trip2Bio,
        'trip2Pic': committeepage.Trip2Pic,
        'social1Name': committeepage.Social1Name,
        'social1Bio': committeepage.Social1Bio,
        'social1Pic': committeepage.Social1Pic,
        'social2Name': committeepage.Social2Name,
        'social2Bio': committeepage.Social2Bio,
        'social2Pic': committeepage.Social2Pic,
        'beginner1Name': committeepage.Beginner1Name,
        'beginner1Bio': committeepage.Beginner1Bio,
        'beginner1Pic': committeepage.Beginner1Pic,
        'beginner2Name': committeepage.Beginner2Name,
        'beginner2Bio': committeepage.Beginner2Bio,
        'beginner2Pic': committeepage.Beginner2Pic,
        'kitName': committeepage.KitName,
        'kitBio': committeepage.KitBio,
        'kitPic': committeepage.KitPic,
        'seniorName': committeepage.SeniorName,
        'seniorBio': committeepage.SeniorBio,
        'seniorPic': committeepage.SeniorPic,
                })

def joinPage(request):
    basepage = BasePage.objects.get(version = "Default")
    joinpage = HomePage.objects.get(version = "Default")
    return render(request, 'pages/joinPage.html', {
        'currentPage': "Join",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
                 })

def spotsPage(request):
    basepage = BasePage.objects.get(version = "Default")
    spotspage = SpotsPage.objects.get(version = "Default")
    spotlist = spots.objects.all().order_by('distance')
    return render(request, 'pages/spotsPage.html', {
        'spotspage': spotspage,
        'spots': spotlist,
        'currentPage': "Resources",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
        })

def spot_detail(request, spot):
    basepage = BasePage.objects.get(version = "Default")
    spotspage = SpotsPage.objects.get(version = "Default")
    spot = spots.objects.filter(name__iexact=spot).get()
    return render(request, 'pages/spot_detail.html', {
        'spot':spot,
        'currentPage': "Resources",
        'footer': basepage.footer,
        'email': basepage.email,
        'title': basepage.title,
        'facebook': basepage.facebookLink,
        'instagram': basepage.instagramLink,
        'susu': basepage.susuLink
        })

