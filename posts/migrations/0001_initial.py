# Generated by Django 4.2.11 on 2024-04-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tema', models.CharField(max_length=255)),
                ('municipio_atingido', models.CharField(max_length=255)),
                ('atores_envolvidos', models.CharField(max_length=255)),
                ('populacao_atingida', models.CharField(max_length=255)),
            ],
        ),
    ]