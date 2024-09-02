# Generated by Django 5.1 on 2024-09-01 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0005_alter_registerpacientes_mensalidade"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegisterAgenda",
            fields=[
                ("id_Agendamento", models.AutoField(primary_key=True, serialize=False)),
                ("cpf_paciente", models.CharField(max_length=11)),
                ("data_hora", models.DateTimeField()),
                (
                    "nome_medico",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registrations.registermedico",
                    ),
                ),
                (
                    "nome_paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="registrations.registerpacientes",
                    ),
                ),
            ],
        ),
    ]
