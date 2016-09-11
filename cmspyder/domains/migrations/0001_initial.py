# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-11 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('domain',),
                'verbose_name': 'Domain',
                'verbose_name_plural': 'Domains',
            },
        ),
        migrations.CreateModel(
            name='Subdomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdomain', models.CharField(blank=True, max_length=250)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdomain', to='domains.Domain')),
            ],
            options={
                'ordering': ('subdomain',),
                'verbose_name': 'Subdomain',
                'verbose_name_plural': 'Subdomains',
            },
        ),
        migrations.CreateModel(
            name='TLD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tld', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('tld',),
                'verbose_name': 'TLD',
                'verbose_name_plural': 'TLDs',
            },
        ),
        migrations.AddField(
            model_name='domain',
            name='tld',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domain', to='domains.TLD'),
        ),
        migrations.AlterUniqueTogether(
            name='subdomain',
            unique_together=set([('subdomain', 'domain')]),
        ),
        migrations.AlterUniqueTogether(
            name='domain',
            unique_together=set([('domain', 'tld')]),
        ),
    ]
