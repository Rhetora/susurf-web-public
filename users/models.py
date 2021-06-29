from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from fernet_fields import EncryptedTextField, EncryptedDateField, EncryptedCharField, EncryptedIntegerField


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField('Committee Member', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    #MEMBER CLASSIFICATION
    MEMBER_TYPES = (
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Alumni', 'Alumni'),
        ('Other', 'Other'),
        ('None', 'Not Affiliated'),
    )

    member_type = EncryptedCharField('Member Type', max_length = 15, choices = MEMBER_TYPES, default = 'None')

    #Personal Info
    first_name = EncryptedCharField('First Name', max_length = 30)
    last_name = EncryptedCharField('Surname', max_length = 70)
    dob = EncryptedDateField('Date of Birth', null = True)
    student_id = EncryptedCharField('Student ID', max_length = 10)
    dietary = EncryptedTextField('Dietary Requirements', blank = True)
    medical = EncryptedTextField('Medical Requirements', blank = True)
    phone = EncryptedCharField('Phone Number', max_length = 20)
    bio = EncryptedTextField('Bio', blank = True)

    #Next of Kin
    kin_name = EncryptedCharField('Next of Kin Name', max_length = 100)
    kin_relation = EncryptedCharField('Next of Kin Relation', max_length = 50)
    kin_number = EncryptedCharField('Next of Kin Phone Number', max_length = 20)
    kin_address1 = EncryptedCharField('Next of Kin Address 1', max_length = 100)
    kin_address2 = EncryptedCharField('Next of Kin Address 2', max_length = 100, blank=True)
    kin_address3 = EncryptedCharField('Next of Kin Address 3', max_length = 100, blank=True)
    kin_postcode = EncryptedCharField('Next of Kin Postcode', max_length = 8)

    #Information
    ABILITY_TYPES = (
        ('Beginner', 'New to surfing'),
        ('Novice', 'Surfing whitewater'),
        ('Intermediate', 'Surfing green waves'),
        ('Advanced', 'Confident surfer'),
        ('Pro', 'Shredding')
    )

    ability = EncryptedCharField('Ability', max_length = 30, choices = ABILITY_TYPES, default = 'Beginner')
    wetsuit = models.BooleanField('Owns a Wetsuit', default = False)
    large_board = models.BooleanField('Owns a Large Board', default = False)
    short_board = models.BooleanField('Owns a Shortboard', default = False)

    car = models.BooleanField('Owns a Car', default = False)
    car_seats = EncryptedCharField('Number of seats in car', max_length = 1, blank=True)
    minibus = models.BooleanField('Can Drive Minibus', default = False)
    swim100m = models.BooleanField('Can Swim 100m', default = False)

    #Agreements
    paid = models.BooleanField('Paid Membership', default = False)

    
    def __str__(self):
        return self.email
