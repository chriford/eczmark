# Generated by Django 3.2 on 2023-07-31 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eczmark', '0004_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('message', models.TextField(help_text='Report an issue to the support team', max_length=350, null=True, verbose_name='Message body')),
                ('active', models.BooleanField(default=True)),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eczmark.issue', verbose_name='Title')),
                ('user', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Marker')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
