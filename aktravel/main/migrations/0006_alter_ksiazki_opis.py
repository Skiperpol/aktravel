# Generated by Django 3.2.11 on 2022-01-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ksiazki_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazki',
            name='opis',
            field=models.CharField(max_length=2000),
        ),
    ]
