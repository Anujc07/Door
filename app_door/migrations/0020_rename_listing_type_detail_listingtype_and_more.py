# Generated by Django 4.1.3 on 2023-11-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_door', '0019_alter_detail_city_alter_detail_room_var'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='Listing_type',
            new_name='Listingtype',
        ),
        migrations.AlterField(
            model_name='detail',
            name='City',
            field=models.CharField(choices=[('Indore', 'Indore'), ('Gwalior', 'Gwalior'), ('Bhopal', 'Bhopal'), ('Jablpur', 'Jablpur')], default='Bhopal', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_description',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_var',
            field=models.CharField(choices=[('Single+Kitchen', 'Single+Kitchen'), ('1BHK', '1BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK'), ('SingleRoom', 'SingleRoom'), ('2BHK', '2BHK')], default=None, max_length=20),
        ),
    ]
