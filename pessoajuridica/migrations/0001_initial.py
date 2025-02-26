# Generated by Django 5.1.5 on 2025-02-04 22:53

import django.db.models.deletion
import pessoajuridica.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0006_delete_tutorcliente'),
        ('tutores', '0007_alter_tutor_cpf_alter_tutor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=255, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=18, unique=True, validators=[pessoajuridica.models.validar_cnpj], verbose_name='CNPJ')),
                ('inscricao_estadual', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Estadual')),
                ('inscricao_municipal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Inscrição Municipal')),
                ('endereco_logradouro', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('endereco_numero', models.CharField(max_length=10, verbose_name='Número')),
                ('endereco_complemento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('endereco_bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('endereco_cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('endereco_estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('endereco_cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('site', models.URLField(blank=True, null=True, verbose_name='Site')),
                ('regime_tributario', models.CharField(blank=True, choices=[('Simples Nacional', 'Simples Nacional'), ('Lucro Presumido', 'Lucro Presumido'), ('Lucro Real', 'Lucro Real')], max_length=50, null=True, verbose_name='Regime Tributário')),
                ('contrato_social', models.FileField(blank=True, null=True, upload_to='documentos/', verbose_name='Contrato Social')),
                ('alvara_funcionamento', models.FileField(blank=True, null=True, upload_to='documentos/', verbose_name='Alvará de Funcionamento')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('clientes', models.ManyToManyField(blank=True, related_name='pessoas_juridicas', to='clientes.clientes', verbose_name='Clientes')),
                ('tutores', models.ManyToManyField(blank=True, related_name='pessoas_juridicas', to='tutores.tutor', verbose_name='Tutores')),
            ],
            options={
                'verbose_name': 'Pessoa Jurídica',
                'verbose_name_plural': 'Pessoas Jurídicas',
            },
        ),
        migrations.CreateModel(
            name='ContaBancaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banco', models.CharField(max_length=100, verbose_name='Banco')),
                ('agencia', models.CharField(max_length=10, verbose_name='Agência')),
                ('conta_corrente', models.CharField(max_length=20, verbose_name='Conta Corrente')),
                ('tipo_conta', models.CharField(choices=[('Corrente', 'Conta Corrente'), ('Poupança', 'Conta Poupança'), ('Salário', 'Conta Salário')], default='Corrente', max_length=50, verbose_name='Tipo de Conta')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('pessoa_juridica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contas_bancarias', to='pessoajuridica.pessoajuridica', verbose_name='Pessoa Jurídica')),
            ],
            options={
                'verbose_name': 'Conta Bancária',
                'verbose_name_plural': 'Contas Bancárias',
            },
        ),
    ]
