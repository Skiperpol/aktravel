# Generated by Django 3.2.11 on 2022-01-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_ksiazki'),
    ]

    operations = [
        migrations.AddField(
            model_name='ksiazki',
            name='opis',
            field=models.CharField(default='opis', max_length=400),
            preserve_default=False,
        ),
    ]
