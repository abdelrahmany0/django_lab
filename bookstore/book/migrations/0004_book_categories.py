# Generated by Django 3.2 on 2021-04-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210422_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='book.Category'),
        ),
    ]