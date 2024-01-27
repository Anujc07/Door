# Generated by Django 4.1.3 on 2023-09-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_door', '0005_alter_detail_city_alter_detail_listing_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='City',
            field=models.CharField(choices=[('Gwalior', 'Gwalior'), ('Jablpur', 'Jablpur'), ('Bhopal', 'Bhopal'), ('Indore', 'Indore')], default='Bhopal', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Listing_type',
            field=models.CharField(choices=[('Sell', 'Sell'), ('Rent', 'Rent')], default='Sell', max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_var',
            field=models.CharField(choices=[('4BHK', '4BHK'), ('2BHK', '2BHK'), ('1BHK', '1BHK'), ('SingleRoom', 'SingleRoom'), ('3BHK', '3BHK'), ('Single+Kitchen', 'Single+Kitchen')], default=None, max_length=20),
        ),
    ]