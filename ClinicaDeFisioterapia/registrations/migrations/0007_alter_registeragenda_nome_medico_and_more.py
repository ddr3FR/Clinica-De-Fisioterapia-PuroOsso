# Generated by Django 5.1 on 2024-09-01 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0006_registeragenda"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registeragenda",
            name="nome_medico",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agendas",
                to="registrations.registermedico",
            ),
        ),
        migrations.AlterField(
            model_name="registeragenda",
            name="nome_paciente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="agendas",
                to="registrations.registerpacientes",
            ),
        ),
    ]
