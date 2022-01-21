# Generated by Django 4.0.1 on 2022-01-18 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='channels_connect',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='equipment_connect',
        ),
        migrations.AddField(
            model_name='channels',
            name='equipment_connect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipment_conn', to='scheme.equipment', verbose_name='Оборудование'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='locations_connect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location_con', to='scheme.locations', verbose_name='Прохождение по оборудованию'),
        ),
    ]