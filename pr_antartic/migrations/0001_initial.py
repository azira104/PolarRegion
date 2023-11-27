# Generated by Django 4.2.6 on 2023-11-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='antarcticHotpoints',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('brightness', models.FloatField()),
                ('scan', models.FloatField()),
                ('track', models.FloatField()),
                ('acq_time', models.DateField()),
                ('satellite', models.CharField(max_length=5)),
                ('confidence', models.CharField(max_length=5)),
                ('bright_t31', models.FloatField()),
                ('frp', models.FloatField()),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='antarcticMass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('antarctic_mass', models.FloatField()),
                ('antarcticMass_1sigma_uncertainty', models.FloatField()),
            ],
        ),
    ]
