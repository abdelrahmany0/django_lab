# Generated by Django 3.2 on 2021-04-22 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210422_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.isbn'),
            preserve_default=False,
        ),
    ]
