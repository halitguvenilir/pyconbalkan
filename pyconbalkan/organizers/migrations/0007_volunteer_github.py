# Generated by Django 2.0.5 on 2018-06-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizers', '0006_volunteer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
