# Generated by Django 5.0.4 on 2024-04-12 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0002_category_city_marker_created_at_marker_description_and_more'),
        ('posts', '0005_remove_post_marcador'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
