# Generated by Django 5.0.4 on 2024-04-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fontes',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
