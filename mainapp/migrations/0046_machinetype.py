# Generated by Django 2.2.1 on 2020-10-01 08:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_user_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('vCPUs', models.IntegerField()),
                ('RAM', models.IntegerField()),
                ('GPU', models.CharField(blank=True, max_length=255)),
                ('EC2Instance', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('available_for_batch', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'machine_types',
            },
        ),
    ]
