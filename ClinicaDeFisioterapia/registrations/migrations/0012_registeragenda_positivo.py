# Generated by Django 5.1 on 2024-09-02 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0011_registeragenda_obs_consulta_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="registeragenda",
            name="positivo",
            field=models.BooleanField(default=False),
        ),
    ]
