# Generated by Django 5.0.1 on 2024-01-24 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_products_title_alter_products_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='ulike_post',
        ),
        migrations.CreateModel(
            name='PostProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_products', to='project.posts')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_products', to='project.products')),
            ],
            options={
                'db_table': 'ulike_post_products',
            },
        ),
    ]