# Generated by Django 4.0.4 on 2022-05-26 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.editor'),
        ),
        migrations.AlterField(
            model_name='article',
            name='post',
            field=models.CharField(max_length=60),
        ),
    ]