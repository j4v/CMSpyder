# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
        ('spyder', '0004_auto_20160911_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('error', models.TextField()),
                ('subdomain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='error', to='domains.Subdomain')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pluginresult',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='pluginresult',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]