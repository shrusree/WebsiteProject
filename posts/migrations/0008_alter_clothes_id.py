# Generated by Django 3.2 on 2021-05-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201223_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]