# Generated by Django 4.2.6 on 2023-10-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classviewshome', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='article',
        ),
        migrations.AddField(
            model_name='book',
            name='article',
            field=models.ManyToManyField(to='classviewshome.article', verbose_name='Статьи'),
        ),
    ]
