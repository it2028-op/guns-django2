# Generated by Django 4.2 on 2023-05-12 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guns', '0004_gun_type_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gun',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='gun',
            name='barrel_length',
            field=models.IntegerField(default=0, help_text='Zadejte délku hlavně zbraně v milimetrech', verbose_name='Délka hlavně zbraně (mm)'),
        ),
        migrations.AddField(
            model_name='gun',
            name='description',
            field=models.TextField(blank=True, help_text='Popište tuto zbraň (historie, vlastnosti, zvláštnosti...)', max_length=300, verbose_name='Popis zbraně'),
        ),
        migrations.AddField(
            model_name='gun',
            name='length',
            field=models.IntegerField(default=0, help_text='Zadejte délku zbraně v milimetrech', verbose_name='Celková délka zbraně (mm)'),
        ),
        migrations.AddField(
            model_name='gun',
            name='magazine',
            field=models.IntegerField(default=1, help_text='Zadejte množtví munice v základním zásobníku zbraně', verbose_name='Celková kapacita obvyklého zásobníku'),
        ),
        migrations.AddField(
            model_name='gun',
            name='rate',
            field=models.FloatField(default=5.0, help_text='Prosím, ohodnoťte na stupnici 1-10', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Hodnocení'),
        ),
        migrations.AddField(
            model_name='gun',
            name='type',
            field=models.ManyToManyField(help_text='Vyberte typ zbraně', to='guns.type'),
        ),
        migrations.AddField(
            model_name='gun',
            name='weight',
            field=models.IntegerField(default=0, help_text='Zadejte hmotnost zbraně v gramech', verbose_name='Celková hmotnost zbraně (g)'),
        ),
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Popis a charakteristika typu'),
        ),
    ]
