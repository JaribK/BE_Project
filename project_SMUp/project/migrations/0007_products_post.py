# Generated by Django 4.2.5 on 2023-12-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_products_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='post',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='project.posts'),
        ),
    ]
