# Generated by Django 5.1.5 on 2025-01-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Vacina')),
                ('tipo', models.CharField(choices=[('V', 'Viral'), ('B', 'Bacteriana'), ('P', 'Polivalente'), ('VV', 'Vírus Vivo'), ('I', 'Inativada')], max_length=2, verbose_name='Tipo de Vacina')),
                ('fabricante', models.CharField(max_length=50, verbose_name='Fabricante')),
                ('lote', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do Lote')),
                ('data_validade', models.DateField(blank=True, null=True, verbose_name='Data de Validade')),
                ('doses_necessarias', models.PositiveIntegerField(default=1, verbose_name='Doses Necessárias')),
                ('intervalo_doses', models.PositiveIntegerField(default=30, verbose_name='Intervalo entre Doses (dias)')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('data_atualizacao', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Vacina',
                'verbose_name_plural': 'Vacinas',
                'ordering': ['nome'],
            },
        ),
    ]
