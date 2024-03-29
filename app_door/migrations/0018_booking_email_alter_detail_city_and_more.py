# Generated by Django 4.1.3 on 2023-09-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_door', '0017_detail_is_booked_alter_detail_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='detail',
            name='City',
            field=models.CharField(choices=[('Indore', 'Indore'), ('Gwalior', 'Gwalior'), ('Jablpur', 'Jablpur'), ('Bhopal', 'Bhopal')], default='Bhopal', max_length=10),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Room_var',
            field=models.CharField(choices=[('1BHK', '1BHK'), ('SingleRoom', 'SingleRoom'), ('Single+Kitchen', 'Single+Kitchen'), ('2BHK', '2BHK'), ('4BHK', '4BHK'), ('3BHK', '3BHK')], default=None, max_length=20),
        ),
    ]
