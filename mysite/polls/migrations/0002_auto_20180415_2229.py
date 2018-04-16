# Generated by Django 2.0.2 on 2018-04-15 16:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cycleRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='session',
            name='id',
        ),
        migrations.AddField(
            model_name='cycles',
            name='available',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='cycles',
            name='cycle_brand',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='cycles',
            name='cycle_description',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='cycles',
            name='cycle_type',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='session',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='cyclerequests',
            name='cycle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.cycles'),
        ),
        migrations.AddField(
            model_name='cyclerequests',
            name='taker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.users'),
        ),
    ]
