# Generated by Django 5.1.1 on 2024-11-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]