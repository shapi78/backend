# Generated by Django 2.2.1 on 2019-05-22 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('first_login', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('users', models.ManyToManyField(related_name='datasets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'datasets',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('datasets', models.ManyToManyField(related_name='studies', to='mainapp.Dataset')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='studies', to='mainapp.Organization')),
                ('users', models.ManyToManyField(related_name='studies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'studies',
            },
        ),
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, null=True)),
                ('study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executions', to='mainapp.Study')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'executions',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='mainapp.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
