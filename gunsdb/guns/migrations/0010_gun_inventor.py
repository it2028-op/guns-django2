# Generated by Django 4.2 on 2023-06-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guns', '0009_remove_inventor_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='gun',
            name='inventor',
            field=models.ManyToManyField(help_text='Vyberte vynálezces zbraně', to='guns.inventor'),
        ),
    ]