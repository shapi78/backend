# Generated by Django 2.2.1 on 2020-04-25 00:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0030_studyDatasets_addfields'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='StudyDataset',
                    fields=[
                        ('id',
                         models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('permission', models.CharField(
                            choices=[('full_access', 'full_access'), ('aggregated_access', 'aggregated_access')],
                            max_length=32)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('dataset',
                         models.ForeignKey(on_delete=models.deletion.CASCADE, to='mainapp.Dataset')),
                        ('study', models.ForeignKey(on_delete=models.deletion.CASCADE, to='mainapp.Study')),
                    ],
                    options={
                        'db_table': 'studies_datasets',
                        'unique_together': {('dataset', 'study')},
                    },
                ),
            ],
        ),
    ]
