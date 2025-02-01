import os
import django
from faker import Faker
from datetime import datetime, timedelta
import random

# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'systemvet_atendimento.settings')
django.setup()

from tutores.models import Tutor

fake = Faker('pt_BR')  # Usando o locale 'pt_BR' para dados em português

def create_fake_tutors(num_tutors=100):  # Agora criando 100 tutores por padrão
    for _ in range(num_tutors):
        nome = fake.name()
        email = fake.email()
        telefone = fake.phone_number()
        endereco = fake.street_address()
        cidade = fake.city()
        estado = fake.state_abbr()
        cep = fake.postcode()
        cpf = fake.cpf()
        rg = fake.rg()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)
        data_cadastro = fake.date_time_this_decade()

        # Cria o tutor no banco de dados
        Tutor.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            cep=cep,
            cpf=cpf,
            rg=rg,
            data_nascimento=data_nascimento,
            data_cadastro=data_cadastro
        )

    print(f"{num_tutors} tutores falsos criados com sucesso!")

if __name__ == "__main__":
    create_fake_tutors()  # Cria 100 tutores falsos