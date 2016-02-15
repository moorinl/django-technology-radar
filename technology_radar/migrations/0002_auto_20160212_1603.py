# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 16:03
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technology_radar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name')),
            ],
        ),
        migrations.AlterField(
            model_name='blip',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blips', to='technology_radar.Area'),
        ),
        migrations.AlterField(
            model_name='blip',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blips', to='technology_radar.Status'),
        ),
        migrations.AlterField(
            model_name='historicalblip',
            name='area',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='technology_radar.Area'),
        ),
        migrations.AlterField(
            model_name='historicalblip',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='technology_radar.Status'),
        ),
    ]