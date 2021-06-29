from django.db import models

class BasePage(models.Model):
    version = models.CharField(max_length=30, default="Default")

    title = models.CharField(max_length=200)
    footer = models.CharField(max_length=200)
    facebookLink = models.CharField(max_length=200)
    instagramLink = models.CharField(max_length=200)
    susuLink = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.version


class HomePage(models.Model):
    version = models.CharField(max_length=30, default="Default")

    def __str__(self):
        return self.version


class AboutPage(models.Model):
    version = models.CharField(max_length=30, default="Default")
    aboutUs = models.TextField(default="Default")
    whatWeDo = models.TextField(default="Default")
    learnMore = models.TextField(default="Default")
    pic1 = models.ImageField(upload_to="about/", blank=True)
    pic2 = models.ImageField(upload_to="about/", blank=True)
    pic3 = models.ImageField(upload_to="about/", blank=True)

    def __str__(self):
        return self.version


class CommitteePage(models.Model):
    version = models.CharField(max_length=30, default="Default")

    PresidentName = models.CharField(max_length=50)
    PresidentBio = models.CharField(max_length=300)
    PresidentPic = models.ImageField(upload_to="committee/", blank=True)

    VPName = models.CharField(max_length=50)
    VPBio = models.CharField(max_length=300)
    VPPic = models.ImageField(upload_to="committee/", blank=True)

    TreasurerName = models.CharField(max_length=50)
    TreasurerBio = models.CharField(max_length=300)
    TreasurerPic = models.ImageField(upload_to="committee/", blank=True)

    Trip1Name = models.CharField(max_length=50)
    Trip1Bio = models.CharField(max_length=300)
    Trip1Pic = models.ImageField(upload_to="committee/", blank=True)

    Trip2Name = models.CharField(max_length=50)
    Trip2Bio = models.CharField(max_length=300)
    Trip2Pic = models.ImageField(upload_to="committee/", blank=True)

    Social1Name = models.CharField(max_length=50)
    Social1Bio = models.CharField(max_length=300)
    Social1Pic = models.ImageField(upload_to="committee/", blank=True)

    Social2Name = models.CharField(max_length=50)
    Social2Bio = models.CharField(max_length=300)
    Social2Pic = models.ImageField(upload_to="committee/", blank=True)

    Beginner1Name = models.CharField(max_length=50)
    Beginner1Bio = models.CharField(max_length=300)
    Beginner1Pic = models.ImageField(upload_to="committee/", blank=True)

    Beginner2Name = models.CharField(max_length=50)
    Beginner2Bio = models.CharField(max_length=300)
    Beginner2Pic = models.ImageField(upload_to="committee/", blank=True)

    KitName = models.CharField(max_length=50)
    KitBio = models.CharField(max_length=300)
    KitPic = models.ImageField(upload_to="committee/", blank=True)

    SeniorName = models.CharField(max_length=50)
    SeniorBio = models.CharField(max_length=300)
    SeniorPic = models.ImageField(upload_to="committee/", blank=True)

    def __str__(self):
        return self.version

class JoinPage(models.Model):
    version = models.CharField(max_length=30, default="Default")

    def __str__(self):
        return self.version

class SpotsPage(models.Model):
    version = models.CharField(max_length=30, default="Default")

    def __str__(self):
        return self.version

class spots(models.Model):
    name = models.CharField(max_length=50)
    list_image = models.ImageField(upload_to="spots/")
    long_description = models.TextField(default="long description for detail page")
    short_description = models.TextField(default="short description for list page")
    location = models.TextField(default="location TOWN, COUNTY, COUNTRY")
    distance = models.IntegerField(default="distance away in miles (by gmaps)")
    recommended = models.TextField(default="Recommended for info")
    howToGetThere = models.TextField(default="How to get there info")
    parking = models.TextField(default="Parking info")
    latitude = models.TextField(default="51.508742")
    longitude = models.TextField(default="-0.120850")
    mswLink = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.name