# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0007_subdomain_discovered_by'),
        ('spyder', '0007_auto_20161020_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscoveryRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('destination_subdomain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_subdomain', to='domains.Subdomain')),
                ('origin_subdomain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_subdomain', to='domains.Subdomain')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
