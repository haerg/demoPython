# Generated by Django 2.1.7 on 2019-02-15 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FsInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_name', models.CharField(max_length=50, null=True)),
                ('contact_email', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(choices=[('LP', 'LP'), ('GP', 'GP')], default=None, max_length=50, null=True)),
                ('signed_nda', models.BooleanField(default=False)),
                ('needs_to_sign', models.BooleanField(default=True)),
                ('is_investor', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='api.FsInstitution')),
            ],
            options={
                'verbose_name': 'Institution',
                'db_table': 'fs_institution',
            },
        ),
        migrations.CreateModel(
            name='FsInstitutionNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('type', models.CharField(default='notification', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FsInstitution')),
            ],
            options={
                'verbose_name': 'Institution Notification',
                'db_table': 'fs_institution_notification',
            },
        ),
        migrations.CreateModel(
            name='FsInstitutionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FsInstitution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Institution User',
                'db_table': 'fs_institution_user',
            },
        ),
        migrations.AddField(
            model_name='fsinstitution',
            name='users',
            field=models.ManyToManyField(related_name='institution_user', through='api.FsInstitutionUser', to=settings.AUTH_USER_MODEL),
        ),
    ]