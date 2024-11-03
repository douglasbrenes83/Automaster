# Generated by Django 5.1.2 on 2024-11-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_repuesto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('vehiculo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('completada', 'Completada'), ('en_proceso', 'En Proceso'), ('cancelada', 'Cancelada')], default='pendiente', max_length=20)),
                ('mecanico', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
