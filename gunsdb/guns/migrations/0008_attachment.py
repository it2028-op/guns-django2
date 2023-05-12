# Generated by Django 4.2 on 2023-05-12 13:30

from django.db import migrations, models
import django.db.models.deletion
import guns.models


class Migration(migrations.Migration):

    dependencies = [
        ('guns', '0007_maker_gun_maker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titul obrázku')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=guns.models.meadia_attachment_path, verbose_name='Soubor')),
                ('type', models.CharField(blank=True, choices=[('image', 'Image'), ('video', 'Video')], default='image', help_text='Vyberte typ přílohy(obrázek nebo video)', max_length=5, verbose_name='Typ přílohy')),
                ('gun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guns.gun')),
            ],
            options={
                'ordering': ['-last_update', 'type'],
            },
        ),
    ]
