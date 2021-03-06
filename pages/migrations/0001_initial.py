# Generated by Django 3.0.6 on 2020-08-22 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
                ('aboutUs', models.TextField(default='Default')),
                ('whatWeDo', models.TextField(default='Default')),
                ('learnMore', models.TextField(default='Default')),
            ],
        ),
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('footer', models.CharField(max_length=200)),
                ('facebookLink', models.CharField(max_length=200)),
                ('instagramLink', models.CharField(max_length=200)),
                ('susuLink', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
                ('PresidentName', models.CharField(max_length=50)),
                ('PresidentBio', models.CharField(max_length=300)),
                ('VPName', models.CharField(max_length=50)),
                ('VPBio', models.CharField(max_length=300)),
                ('TreasurerName', models.CharField(max_length=50)),
                ('TreasurerBio', models.CharField(max_length=300)),
                ('Trip1Name', models.CharField(max_length=50)),
                ('Trip1Bio', models.CharField(max_length=300)),
                ('Trip2Name', models.CharField(max_length=50)),
                ('Trip2Bio', models.CharField(max_length=300)),
                ('Social1Name', models.CharField(max_length=50)),
                ('Social1Bio', models.CharField(max_length=300)),
                ('Social2Name', models.CharField(max_length=50)),
                ('Social2Bio', models.CharField(max_length=300)),
                ('Beginner1Name', models.CharField(max_length=50)),
                ('Beginner1Bio', models.CharField(max_length=300)),
                ('Beginner2Name', models.CharField(max_length=50)),
                ('Beginner2Bio', models.CharField(max_length=300)),
                ('KitName', models.CharField(max_length=50)),
                ('KitBio', models.CharField(max_length=300)),
                ('SeniorName', models.CharField(max_length=50)),
                ('SeniorBio', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JoinPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SpotsPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(default='Default', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='spots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list_image', models.ImageField(upload_to='spots/')),
                ('long_description', models.TextField(default='long description for detail page')),
                ('short_description', models.TextField(default='short description for list page')),
                ('location', models.TextField(default='location TOWN, COUNTY, COUNTRY')),
                ('distance', models.TextField(default='distance away in miles (by gmaps)')),
                ('recommended', models.TextField(default='Recommended for info')),
                ('howToGetThere', models.TextField(default='How to get there info')),
                ('parking', models.TextField(default='Parking info')),
                ('latitude', models.TextField(default='51.508742')),
                ('longitude', models.TextField(default='-0.120850')),
                ('mswLink', models.CharField(default='#', max_length=200)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.SpotsPage')),
            ],
        ),
    ]
