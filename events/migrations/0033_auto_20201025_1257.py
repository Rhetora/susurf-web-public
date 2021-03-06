# Generated by Django 3.1.1 on 2020-10-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0032_beginnersignupentry_endquestionanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beginnersignupentry',
            name='roofRacks',
            field=models.CharField(choices=[('No', 'No'), ('I have a hard roofrack', 'I have a hard roofrack'), ('I have a soft roofrack', 'I have a soft roofrack'), ('I can put a club soft roof rack on', 'I can put a club soft roof rack on')], default="Can't use a roofrack", max_length=100),
        ),
        migrations.AlterField(
            model_name='weekendsignupentry',
            name='roofRacks',
            field=models.CharField(choices=[('No', 'No'), ('I have a hard roofrack', 'I have a hard roofrack'), ('I have a soft roofrack', 'I have a soft roofrack'), ('I can put a club soft roof rack on', 'I can put a club soft roof rack on')], default="Can't use a roofrack", max_length=100),
        ),
    ]
