# Generated by Django 4.0.2 on 2022-02-06 18:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='uploads/')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('description', models.TextField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cronos.file')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('content', models.TextField(null=True)),
                ('title', models.CharField(max_length=150)),
                ('cover_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cronos.file')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
