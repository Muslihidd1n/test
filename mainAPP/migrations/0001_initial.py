# Generated by Django 5.0.2 on 2024-02-15 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Davlat',
                'verbose_name_plural': 'Davlatlar',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('rasm', models.ImageField(blank=True, null=True, upload_to='clublar/')),
                ('prezident', models.CharField(blank=True, max_length=255)),
                ('murabbiy', models.CharField(blank=True, max_length=255)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('top_transfer', models.TextField(blank=True)),
                ('kapital', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('davlat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainAPP.davlat')),
            ],
            options={
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clublar',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(blank=True, max_length=255)),
                ('narx', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('t_yil', models.DateField(blank=True, null=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainAPP.club')),
                ('davlat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainAPP.davlat')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Playerlar',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narx', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('taxmin_narx', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('sana', models.DateField(blank=True, null=True)),
                ('club_eski', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eskilar', to='mainAPP.club')),
                ('club_yangi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='yangilar', to='mainAPP.club')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainAPP.player')),
            ],
            options={
                'verbose_name': 'Transfer',
                'verbose_name_plural': 'Transferlar',
            },
        ),
    ]
