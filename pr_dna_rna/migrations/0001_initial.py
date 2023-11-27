# Generated by Django 4.2.6 on 2023-11-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='C14_C13_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('island', models.CharField(max_length=50)),
                ('sample_code', models.CharField(max_length=10)),
                ('pit', models.IntegerField()),
                ('depth_cm', models.IntegerField()),
                ('sample_identifier', models.IntegerField()),
                ('DNA_relative_abundance_percentage', models.FloatField()),
                ('RNA_relative_abundance_percentage', models.FloatField()),
                ('enrichment14C_percentange_modern', models.FloatField()),
                ('modern_1_sigma_error_percentage', models.FloatField()),
                ('modelled_mean_residence_time_year', models.IntegerField()),
                ('mean_residence_time_year', models.IntegerField()),
                ('delta_13C_content_per_mille', models.FloatField()),
                ('conventional_radiocarbon_age_yr', models.IntegerField()),
                ('age_1_sigma_error_yr_BP', models.IntegerField()),
                ('SUERC_publication_code', models.CharField(max_length=50)),
                ('combustion_method', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='edaphicFactors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('island', models.CharField(max_length=50)),
                ('pit', models.IntegerField()),
                ('depth_cm', models.IntegerField()),
                ('pH_water', models.FloatField()),
                ('moisture_percentage', models.FloatField()),
                ('total_C_concentration_percentage_dwt', models.FloatField()),
                ('total_N_concentration_percentage_dwt', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='nucleotideRead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('island', models.CharField(max_length=50)),
                ('pit', models.IntegerField()),
                ('depth_cm', models.IntegerField()),
                ('nucleotide', models.CharField(max_length=10)),
                ('no_reads', models.IntegerField()),
                ('total_no_reads', models.IntegerField()),
                ('relative_abundance_percentage', models.FloatField()),
            ],
        ),
    ]
