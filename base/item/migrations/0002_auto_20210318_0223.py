# Generated by Django 3.1.7 on 2021-03-18 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='seller',
            new_name='idn',
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
