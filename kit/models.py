from django.db import models

class Surfboard(models.Model):
    IDnumber = models.IntegerField(unique=True)
    location = models.TextField(default='Container')
    pastBorrowers = models.TextField(blank=True)
    
    BOARD_ABILITY = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    size = models.CharField(max_length=6)
    ability = models.CharField(choices=BOARD_ABILITY, max_length=20)
    watertight = models.BooleanField(default=True)
    condition = models.TextField(blank=True)

    def __str__(self):
        return self.brand

class Wetsuit(models.Model):
    IDnumber = models.IntegerField(unique=True)
    location = models.TextField(default='Container')
    pastBorrowers = models.TextField(blank=True)
    usable = models.BooleanField(default=True)
    
    WETSUIT_SIZES = (
        ('Childs age 16', 'Childs age 16'),
        ('Womens 6', 'Womens 6'),
        ('Womens 8', 'Womens 8'),
        ('Womens 10', 'Womens 10'),
        ('Womens 12', 'Womens 12'),
        ('Womens 14', 'Womens 14'),
        ('Womens 16', 'Womens 16'),
        ('Mens Small', 'Mens Small'),
        ('Mens Medium', 'Mens Medium'),
        ('Mens Large', 'Mens Large'),
        ('Mens Extra Large', 'Mens Extra Large'),
    )

    WETSUIT_THICKNESSES = (
        ('6/5mm', '6/5mm'),
        ('5/4/3mm', '5/4/3mm'),
        ('5/4mm', '5/4mm'),
        ('5/3mm', '5/3mm'),
        ('4/3mm', '4/3mm'),
        ('3/2mm', '3/2mm'),
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    size = models.CharField(choices=WETSUIT_SIZES, max_length=30)
    thickness = models.CharField(choices=WETSUIT_THICKNESSES, max_length=10)
    condition = models.TextField(blank=True)

    def __str__(self):
        return self.brand

class Misc_Item(models.Model):
    IDnumber = models.IntegerField(unique=True)
    location = models.TextField(default='Container')
    pastBorrowers = models.TextField(blank=True)
    
    ITEM_TYPE = (
        ('Leash', 'Leash'),
        ('Indo Board', 'Indo Board'),
        ('Soft Roof Rack', 'Soft Roof Rack'),
        ('Other', 'Other'),
    )

    item_type = models.CharField(choices=ITEM_TYPE, max_length=50)
    brand = models.CharField(max_length=50)
    condition = models.TextField(blank=True)

    def __str__(self):
        return self.item_type
