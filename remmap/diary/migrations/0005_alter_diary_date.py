# Generated by Django 4.1.7 on 2023-03-14 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_alter_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
