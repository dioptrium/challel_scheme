# Generated by Django 4.0.1 on 2022-02-17 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0006_alter_channels_description_alter_channels_traffic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='equipment',
            field=models.CharField(max_length=100, verbose_name='Оборудование'),
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=100, verbose_name='Порт')),
                ('timeslot', models.CharField(max_length=100, verbose_name='Таймслот')),
                ('specification', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='equip_specif', to='scheme.equipment', verbose_name='Спецификация')),
            ],
        ),
    ]