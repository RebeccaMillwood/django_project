# Generated by Django 3.0.8 on 2020-09-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_favourite_cupcake_flavour'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.TextField(blank=True),
        ),
    ]
