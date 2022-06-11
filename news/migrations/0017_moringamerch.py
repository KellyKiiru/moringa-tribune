# Generated by Django 4.0.4 on 2022-06-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_delete_editor'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoringaMerch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
