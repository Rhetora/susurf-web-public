from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Event(models.Model):

    EVENT_TYPES = (
        ('Weekend Trip', 'Weekend Trip'),
        ('Abroad Trip', 'Abroad Trip'),
        ('Beginner Session', 'Beginner Session'),
        ('Social', 'Social'),
        ('Misc.', 'Misc.'),
    )

    event_type = models.CharField('Event Type', max_length = 30, choices = EVENT_TYPES, default = 'Misc.')
    name = models.CharField(max_length = 200)
    location = models.TextField()
    shortDescription = models.TextField()
    longDescription = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    #Time fields
    startDateTime = models.DateTimeField(help_text="When the event starts")
    endDateTime = models.DateTimeField(help_text="When the event ends (optional)")

    #Publish
    publishDateTime = models.DateTimeField(help_text="When the event will appear on the events page")

    #Signup
    signupRequired = models.BooleanField(default=False, help_text="Is a signup is required? (For weekend, abroad, and beginner trips)")
    spaces = models.IntegerField(blank=True, null=True, help_text="Spaces on the trip")
    endQuestion = models.TextField(blank=True, help_text="Fun question for the end of signup")
    signupPublish = models.DateTimeField(blank=True, null=True, help_text="When the signup appears on the event page")
    signupClose = models.DateTimeField(blank=True, null=True, help_text="When the signup will dissapear")

    #Weekend
    camping = models.BooleanField(default=False, help_text="Is it a camping trip?")
    weekendSignups = models.ManyToManyField('weekendSignupEntry', blank=True)

    #Abroad
    rentalAvailable = models.BooleanField(default=False, help_text="Is equipment rental available?")
    lessonsAvailable = models.BooleanField(default=False, help_text="Are lessons available?")
    abroadSignups = models.ManyToManyField('abroadSignupEntry', blank=True)

    #Beginner
    beginnerSignups = models.ManyToManyField('beginnerSignupEntry', blank=True)


    def __str__(self):
        return self.name

class weekendSignupEntry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    BORROW_BOARD_TYPES = (
        ('None', 'None'),
        ('Foamie', 'Foamie (Beginner Board)'),
        ('Bic', 'Bic (Hard Intermediate Board)'),
        ('Foamie Shortboard', 'Foamie Shortboard (Intermediates)'),
        ('Shortboard', 'Shortboard'),
    )

    BRING_BOARD_TYPES = (
        ('None', 'None'),
        ('Long', 'Board over 8ft'),
        ('Medium', 'Board between 6ft6 and 7ft6'),
        ('Short', 'Board under 6ft6'),
    )

    WETSUIT_TYPES = (
        ('None', "I'll bring my own"),
        ('w-6', 'Womens 6'),
        ('w-8', 'Womens 8'),
        ('w-10', 'Womens 10'),
        ('w-12', 'Womens 12'),
        ('w-14', 'Womens 14'),
        ('w-16', 'Womens 16'),
        ('m-S', 'Mens Small'),
        ('m-M', 'Mens Medium'),
        ('m-L', 'Mens Large'),
        ('m-XL', 'Mens Extra Large'),
    )

    ROOFRACK_TYPES = (
        ("No", "No"),
        ('I have a hard roofrack', 'I have a hard roofrack'),
        ('I have a soft roofrack', 'I have a soft roofrack'),
        ('I can put a club soft roof rack on', 'I can put a club soft roof rack on'),
    )
    
    borrowBoard = models.CharField(max_length=20, choices=BORROW_BOARD_TYPES, default='None')
    bringBoard = models.CharField(max_length=20, choices=BRING_BOARD_TYPES, default='None')
    wetsuit = models.CharField(max_length=20, choices=WETSUIT_TYPES, default='None')

    tent = models.TextField(blank=True)
    driveCar = models.BooleanField(default=False)
    roofRacks = models.CharField(max_length=100, choices = ROOFRACK_TYPES, default="Can't use a roofrack")
    carSeats = models.IntegerField(blank=True, null=True)

    driveMinibus = models.BooleanField(default=False)

    endQuestionAnswer = models.TextField(blank=True)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

class abroadSignupEntry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    rental = models.BooleanField(default=False)
    lessons = models.BooleanField(default=False)

    endQuestionAnswer = models.TextField(blank=True)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

class beginnerSignupEntry(models.Model):

    BORROW_BOARD_TYPES = (
        ('None', 'None'),
        ('Foamie', 'Foamie (Beginner Board)'),
        ('Bic', 'Bic (Hard Intermediate Board)'),
        ('Foamie Shortboard', 'Foamie Shortboard (Intermediates)'),
        ('Shortboard', 'Shortboard'),
    )

    WETSUIT_TYPES = (
        ('None', "I'll bring my own"),
        ('w-6', 'Womens 6'),
        ('w-8', 'Womens 8'),
        ('w-10', 'Womens 10'),
        ('w-12', 'Womens 12'),
        ('w-14', 'Womens 14'),
        ('w-16', 'Womens 16'),
        ('m-S', 'Mens Small'),
        ('m-M', 'Mens Medium'),
        ('m-L', 'Mens Large'),
        ('m-XL', 'Mens Extra Large'),
    )

    ROOFRACK_TYPES = (
        ("No", "No"),
        ('I have a hard roofrack', 'I have a hard roofrack'),
        ('I have a soft roofrack', 'I have a soft roofrack'),
        ('I can put a club soft roof rack on', 'I can put a club soft roof rack on'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    wetsuit = models.CharField(max_length=20, choices=WETSUIT_TYPES, default='None')
    borrowBoard = models.CharField(max_length=20, choices=BORROW_BOARD_TYPES, default='None')

    driveCar = models.BooleanField(default=False)
    roofRacks = models.CharField(max_length=100, choices = ROOFRACK_TYPES, default="Can't use a roofrack")
    carSeats = models.IntegerField(blank=True, null=True)

    endQuestionAnswer = models.TextField(blank=True)

    def __str__(self):
        return str(self.user.first_name) + " " + str(self.user.last_name)

