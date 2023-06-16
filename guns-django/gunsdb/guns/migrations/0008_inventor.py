# Generated by Django 4.2 on 2023-06-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guns', '0007_maker_gun_maker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Zadejte jméno vynálezce', max_length=80, verbose_name='Jméno vynálezce')),
                ('surname', models.CharField(help_text='Zadejte příjmení vynálezce', max_length=50, verbose_name='Příjmení vynálezce')),
                ('birth', models.DateField(blank=True, null=True, verbose_name='Datum narození')),
                ('death', models.DateField(blank=True, null=True, verbose_name='Datum úmrtí')),
                ('about', models.TextField(blank=True, verbose_name='O vynálezci')),
                ('foto', models.ImageField(upload_to='inventors', verbose_name='Fotografie')),
            ],
            options={
                'verbose_name': 'Vynálezce',
                'verbose_name_plural': 'Vynálezci',
                'ordering': ['surname', 'name'],
            },
        ),
    ]
