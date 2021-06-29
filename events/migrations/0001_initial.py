# Generated by Django 3.0.6 on 2020-08-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('Weekend Trip', 'Weekend Trip'), ('Abroad Trip', 'Abroad Trip'), ('Day Trip', 'Day Trip'), ('Beginner Session', 'Beginner Session'), ('Social', 'Social'), ('Misc.', 'Misc.')], default='Misc.', max_length=30, verbose_name='Event Type')),
                ('name', models.CharField(max_length=200)),
                ('eventDateTime', models.DateTimeField()),
                ('publishDateTime', models.DateTimeField()),
                ('location', models.TextField()),
                ('shortDescription', models.TextField()),
                ('longDescription', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
                ('signupRequired', models.BooleanField(default=False)),
                ('spacesAvailable', models.IntegerField(default=0)),
                ('spacesRemaining', models.IntegerField(default=0)),
            ],
        ),
    ]