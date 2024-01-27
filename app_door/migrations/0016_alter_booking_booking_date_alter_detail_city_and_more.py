# Generated by Django 4.1.3 on 2023-09-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_door', '0015_alter_detail_contactnumber_alter_detail_listing_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='City',
            field=models.CharField(choices=[('Jablpur', 'Jablpur'), ('Gwalior', 'Gwalior'), ('Indore', 'Indore'), ('Bhopal', 'Bhopal')], default='Bhopal', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Listing_type',
            field=models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell')], default='Sell', max_length=50),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_var',
            field=models.CharField(choices=[('4BHK', '4BHK'), ('SingleRoom', 'SingleRoom'), ('3BHK', '3BHK'), ('2BHK', '2BHK'), ('Single+Kitchen', 'Single+Kitchen'), ('1BHK', '1BHK')], default=None, max_length=20),
        ),
    ]