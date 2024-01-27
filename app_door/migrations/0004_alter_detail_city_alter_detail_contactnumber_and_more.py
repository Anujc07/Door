# Generated by Django 4.1.3 on 2023-08-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_door', '0003_detail_latitude_detail_longitude_alter_detail_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='City',
            field=models.CharField(choices=[('Jablpur', 'Jablpur'), ('Indore', 'Indore'), ('Gwalior', 'Gwalior'), ('Bhopal', 'Bhopal')], default='Bhopal', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Contactnumber',
            field=models.IntegerField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_var',
            field=models.CharField(choices=[('Single+Kitchen', 'Single+Kitchen'), ('4BHK', '4BHK'), ('3BHK', '3BHK'), ('2BHK', '2BHK'), ('1BHK', '1BHK'), ('SingleRoom', 'SingleRoom')], default=None, max_length=20),
        ),
    ]