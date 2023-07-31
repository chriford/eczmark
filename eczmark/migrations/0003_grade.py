# Generated by Django 3.2 on 2023-07-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eczmark', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('grade', models.SmallIntegerField(null=True, verbose_name='Grade')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]