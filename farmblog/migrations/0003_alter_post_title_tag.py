# Generated by Django 3.2.5 on 2021-08-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Give a Tag for your Post', max_length=255),
        ),
    ]
