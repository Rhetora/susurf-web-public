from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    #Personal
    first_name = forms.CharField(max_length=30, help_text='*')
    last_name = forms.CharField(max_length=30, help_text='*')
    email = forms.EmailField(max_length=254, help_text='* Use your student email if applicable')
    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(years =range(1940, 2020)), help_text='*')
    member_type = forms.ChoiceField(choices=CustomUser.MEMBER_TYPES, help_text='*')
    student_id = forms.CharField(label='Student ID Number', max_length=10, help_text='*')
    phone = forms.CharField(label='Mobile Phone Number', max_length=20, help_text='*')
    #Medical/Dietary
    medical = forms.CharField(label='Medical Requirements', widget=forms.Textarea, required=False)
    dietary = forms.CharField(label='Dietary Requirements', widget=forms.Textarea, required=False)
    kin_name = forms.CharField(label='Next of Kin Name', max_length = 100, help_text='*')
    kin_relation = forms.CharField(label='Next of Kin Relation', max_length = 50, help_text='*')
    kin_number = forms.CharField(label='Next of Kin Phone Number', max_length = 20, help_text='*')
    kin_address1 = forms.CharField(label='Next of Kin Address 1', max_length = 100, help_text='*')
    kin_address2 = forms.CharField(label='Next of Kin Address 2', max_length = 100, required=False)
    kin_address3 = forms.CharField(label='Next of Kin Address 3', max_length = 100, required=False)
    kin_postcode = forms.CharField(label='Next of Kin Postcode', max_length = 8, help_text='*')
    #Surfing
    ability = forms.ChoiceField(choices=CustomUser.ABILITY_TYPES, help_text='*')
    wetsuit = forms.BooleanField(label='I own a Wetsuit', required=False)
    large_board = forms.BooleanField(label='I own a Large Board', required=False)
    short_board = forms.BooleanField(label='I own a Shortboard', required=False)
    car = forms.BooleanField(label='I Have a car to drive to trips', required=False)
    car_seats = forms.CharField(label='Number of seats in my car (including driver)', max_length = 1, required=False)
    minibus = forms.BooleanField(label='I can drive a SUSU Minibus', required=False)
    #Agreements
    swim100m = forms.BooleanField(label='I can Swim 100m', required=False)
    paid = forms.BooleanField(label='I Have Paid Membership (SUSU Box Office)', required=False)
    agree = forms.BooleanField(label='I agree to the Club Rules', required = True, help_text='*')

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'member_type',
            'dob',
            'student_id',
            'phone',
            'medical',
            'dietary',
            'kin_name',
            'kin_relation',
            'kin_number',
            'kin_address1',
            'kin_address2',
            'kin_address3',
            'kin_postcode',
            'ability',
            'wetsuit',
            'large_board',
            'short_board',
            'car',
            'car_seats',
            'minibus',
            'swim100m',
            'paid',
            'agree'
            )