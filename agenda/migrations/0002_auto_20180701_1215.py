# Generated by Django 2.0.6 on 2018-07-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='paciente',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
