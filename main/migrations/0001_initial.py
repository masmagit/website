# Generated by Django 3.2 on 2021-05-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(blank=True, max_length=50)),
                ('param1', models.CharField(blank=True, max_length=250)),
                ('param2', models.JSONField(blank=True, null=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
