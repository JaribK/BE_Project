# Generated by Django 5.0.1 on 2024-01-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_alter_posts_post_date_alter_products_img_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='userposts',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]