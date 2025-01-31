from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from validarcpf import validar_cpf
import re
from django.apps import apps
from flask import Flask, render_template
from database import get_db_connection

app = Flask(__name__)

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\(\d{2}\) \d{5}-\d{4}$', message="Telefone deve estar no formato: '(99) 99999-9999'.")
    ])
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, validators=[
        MinLengthValidator(2, message="Estado deve ter 2 caracteres.")
    ])
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-\d{3}$', message="CEP deve estar no formato: '99999-999'.")
    ])
    cpf = models.CharField(max_length=14, validators=[
        RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message="CPF deve estar no formato: '999.999.999-99'.")
    ])
    rg = models.CharField(max_length=12)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def clean(self):
        if not validar_cpf(self.cpf):
            raise ValidationError({'cpf': "CPF inválido."})

    def save(self, *args, **kwargs):
        self.telefone = self.formatar_telefone(self.telefone)
        self.cep = self.formatar_cep(self.cep)
        self.cpf = self.formatar_cpf(self.cpf)
        self.clean()
        super().save(*args, **kwargs)

    def formatar_telefone(self, telefone):
        telefone = re.sub(r'\D', '', telefone)
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

    def formatar_cep(self, cep):
        cep = re.sub(r'\D', '', cep)
        return f"{cep[:5]}-{cep[5:]}"

    def formatar_cpf(self, cpf):
        cpf = re.sub(r'\D', '', cpf)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    @app.route('/tutores')
    def tutores():
        # Conecta ao banco de dados
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Executa a consulta SQL para recuperar os tutores
                sql = "SELECT nome, telefone, email FROM tutores"  # Substitua "tutores" pelo nome da sua tabela
                cursor.execute(sql)
                tutores = cursor.fetchall()  # Recupera todos os registros
        finally:
            connection.close()  # Fecha a conexão com o banco de dados

        # Passa os tutores para o template
        return render_template('tutores.html', tutores=tutores)
    
    @app.route('/tutor/<int:tutor_id>')
    def tutor_detalhes(tutor_id):
        # Conecta ao banco de dados
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Executa a consulta SQL para recuperar os detalhes do tutor
                sql = "SELECT id, nome, telefone, email FROM tutores WHERE id = %s"
                cursor.execute(sql, (tutor_id,))
                tutor = cursor.fetchone()  # Recupera o registro do tutor
        finally:
            connection.close()  # Fecha a conexão com o banco de dados

        # Passa os detalhes do tutor para o template
        return render_template('tutordetalhes.html', tutor=tutor)

    
    def __str__(self):
        return self.nome