# database.py
import pymysql
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_db_connection():
    """
    Cria e retorna uma conexão com o banco de dados usando as variáveis de ambiente.
    """
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST'),        # Host do banco de dados
            user=os.getenv('DB_USER'),        # Usuário do banco de dados
            password=os.getenv('DB_PASSWORD'),# Senha do banco de dados
            database=os.getenv('DB_NAME'),    # Nome do banco de dados
            cursorclass=pymysql.cursors.DictCursor  # Retorna os resultados como dicionários
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise