# Generated by Django 2.0.6 on 2018-07-01 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20180701_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='data',
            new_name='agd_Date',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='hora_fim',
            new_name='agd_hora_fim',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='hora_inicio',
            new_name='agd_hora_inicio',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='paciente',
            new_name='agd_paciente',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='procedimento',
            new_name='agd_procedimento',
        ),
    ]
