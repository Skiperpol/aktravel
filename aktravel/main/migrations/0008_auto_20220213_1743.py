# Generated by Django 3.2.11 on 2022-02-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220211_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazki',
            name='opis',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cena',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cena_nie_zawiera',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='cena_zawiera',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='historia',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='opis_dni',
            field=models.TextField(blank=True, max_length=30000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='termin',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='tytul',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='uwagi',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='wazne_informacje',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]