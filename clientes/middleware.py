# clientes/middleware.py

import logging
import os
import time
from django.conf import settings
from django.contrib.auth import logout
from django.dispatch import receiver
from django.shortcuts import redirect
from django.db.models.signals import post_save, post_delete

class UserLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log para verificar quando o middleware é chamado
        print("Middleware chamado:", request.path)

        # Verifica se a sessão existe
        if not hasattr(request, 'session') or not request.session.session_key:
            print("Sessão não encontrada no middleware!")

        # Variáveis para registrar logs (inicializadas como None)
        logger = None
        username = None

        # Verifica se o usuário está autenticado
        if request.user.is_authenticated:
            username = request.user.username
            log_file = os.path.join(settings.LOGS_DIR, f"{username}.log")

            # Garante que o diretório de logs exista
            os.makedirs(settings.LOGS_DIR, exist_ok=True)

            # Configura o logger para o usuário
            logger = logging.getLogger(f'user_logger_{username}')
            if not logger.handlers:
                handler = logging.FileHandler(log_file)
                handler.setLevel(logging.INFO)
                formatter = logging.Formatter('%(asctime)s - %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)

        # Processa a requisição
        response = self.get_response(request)

        # Lógica de logout automático por inatividade
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            if last_activity:
                idle_time = time.time() - last_activity
                if idle_time > 30 * 60:  # 30 minutos de inatividade
                    logout(request)  # Realiza o logout
                    return redirect('login')  # Redireciona para a página de login

            # Atualiza o timestamp da última atividade
            request.session['last_activity'] = time.time()

        # Registra logs apenas para ações relevantes
        if logger and username:
            method = request.method
            path = request.path
            ip = request.META.get('REMOTE_ADDR', 'unknown')

            # Filtra requisições relevantes
            if method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                status_code = response.status_code
                logger.info(f"[AÇÃO] [{method}] {path} - Status: {status_code}, IP: {ip}")

        return response


# Sinais para capturar alterações no banco de dados
@receiver(post_save)
def log_post_save(sender, instance, created, **kwargs):
    # Obtém o nome do modelo e o ID do registro
    model_name = sender.__name__
    instance_id = getattr(instance, 'id', None)

    # Registra logs apenas para modelos relevantes
    relevant_models = ['Tutor', 'Cliente', 'Usuario']  # Adicione outros modelos aqui
    if model_name in relevant_models:
        action = "Criado" if created else "Atualizado"
        logger = logging.getLogger(f'user_logger_{getattr(instance, "usuario_atual", "desconhecido")}')
        if logger:
            logger.info(f"[BANCO] {action} {model_name} ID: {instance_id}")


@receiver(post_delete)
def log_post_delete(sender, instance, **kwargs):
    # Obtém o nome do modelo e o ID do registro
    model_name = sender.__name__
    instance_id = getattr(instance, 'id', None)

    # Registra logs apenas para modelos relevantes
    relevant_models = ['Tutor', 'Cliente', 'Usuario']  # Adicione outros modelos aqui
    if model_name in relevant_models:
        logger = logging.getLogger(f'user_logger_{getattr(instance, "usuario_atual", "desconhecido")}')
        if logger:
            logger.info(f"[BANCO] Excluído {model_name} ID: {instance_id}")