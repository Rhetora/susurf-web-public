from django import forms
from .models import Event, weekendSignupEntry, abroadSignupEntry, beginnerSignupEntry
from django.contrib.auth import get_user_model
 

class weekendSignupForm(forms.ModelForm):
    class Meta:
        model = weekendSignupEntry
        labels = {
            "borrowBoard": "Do you need to borrow a board?",
            "bringBoard": "Are you bringing a board?",
            "wetsuit": "Do you need to borrow a wetsuit?",
            "driveCar": "I can drive a car for this trip",
            "roofRacks": "Can you put a roofrack on your car?",
            "carSeats": "How many seats does your car have? (Inc. Driver)",
            "driveMinibus": "I can drive a Minibus for this trip",
            "tent": "If you own a tent how many people can it sleep?",
        }

        fields = [
            'borrowBoard',
            'bringBoard',
            'wetsuit',
            'driveCar',
            'roofRacks',
            'carSeats',
            'driveMinibus',
            'tent',
            'endQuestionAnswer',
        ]

        exclude = ['timestamp']

class abroadSignupForm(forms.ModelForm):
    class Meta:
        model = abroadSignupEntry
        labels = {
            "rental": "Do you want to rent equipment?",
            "lessons": "Do you want lessons?",
        }

        fields = [
            'rental',
            'lessons',
            'endQuestionAnswer',
        ]

        exclude = ['timestamp']

class beginnerSignupForm(forms.ModelForm):
    class Meta:
        model = beginnerSignupEntry
        labels = {
            "borrowBoard": "Do you need to borrow a board?",
            "wetsuit": "Do you need to borrow a wetsuit?",
            "driveCar": "I can drive a car for this trip",
            "roofRacks": "Can you put a roofrack on your car?",
            "carSeats": "How many seats does your car have? (Inc. Driver)",
        }

        fields = [
            'borrowBoard',
            'wetsuit',
            'driveCar',
            'roofRacks',
            'carSeats',
            'endQuestionAnswer',
        ]

        exclude = ['timestamp']

