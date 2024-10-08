# Generated by Django 4.2.6 on 2023-11-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr_antartic', '0001_initial'),
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
                ('acq_date', models.DateField()),
                ('acq_time', models.IntegerField()),
                ('satellite', models.CharField(max_length=5)),
                ('confidence', models.CharField(max_length=5)),
                ('bright_t31', models.FloatField()),
                ('frp', models.FloatField()),
                ('type', models.IntegerField()),
            ],
        ),
    ]
