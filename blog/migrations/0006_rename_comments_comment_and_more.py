# Generated by Django 5.1.1 on 2024-11-29 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameIndex(
            model_name='comment',
            new_name='blog_commen_created_0e6ed4_idx',
            old_name='blog_commen_created_ad0231_idx',
        ),
    ]
