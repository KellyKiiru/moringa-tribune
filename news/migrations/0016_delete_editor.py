# Generated by Django 4.0.4 on 2022-06-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_alter_article_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
