# Generated by Django 2.0.6 on 2018-07-01 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20180701_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='agd_Date',
            new_name='agd_date',
        ),
    ]
