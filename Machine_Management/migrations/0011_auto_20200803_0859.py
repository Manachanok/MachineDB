# Generated by Django 3.0.8 on 2020-08-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine_Management', '0010_auto_20200803_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production_line',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]