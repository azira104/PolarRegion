from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_key', models.CharField(db_index=True, max_length=100)),
                ('ip_address', models.CharField(blank=True, max_length=64, null=True)),
                ('user_agent', models.TextField(blank=True, null=True)),
                ('device_type', models.CharField(default='desktop', max_length=30)),
                ('country', models.CharField(default='Unknown', max_length=80)),
                ('page_path', models.CharField(default='/', max_length=255)),
                ('traffic_source', models.CharField(default='direct', max_length=255)),
                ('accessed_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-accessed_at'],
            },
        ),
    ]
