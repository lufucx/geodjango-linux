# Generated by Django 5.0.4 on 2024-06-18 17:27

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobre', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Sobre')),
            ],
            options={
                'verbose_name_plural': 'Editar o sobre',
            },
        ),
    ]
