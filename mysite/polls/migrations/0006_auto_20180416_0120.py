# Generated by Django 2.0.2 on 2018-04-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180415_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyclerequests',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]