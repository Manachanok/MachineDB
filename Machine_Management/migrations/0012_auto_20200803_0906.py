# Generated by Django 3.0.8 on 2020-08-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine_Management', '0011_auto_20200803_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_line',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
