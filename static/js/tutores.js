// static/js/tutores.js

function editarTutor() {
    const selected = document.querySelector('input[name="tutor_id"]:checked');
    if (selected) {
        const tutorId = selected.value;
        // Redireciona para a URL de edição do tutor selecionado
        window.location.href = `/tutores/editar_tutor/${tutorId}/`;
    } else {
        alert("Por favor, selecione um tutor para editar.");
    }
}

function confirmarExclusao() {
    const selected = document.querySelector('input[name="tutor_id"]:checked');
    if (selected) {
        document.getElementById('confirmModal').style.display = 'block';
    } else {
        alert("Por favor, selecione um tutor para excluir.");
    }
}

function excluirTutor() {
    const selected = document.querySelector('input[name="tutor_id"]:checked');
    if (selected) {
        const tutorId = selected.value;
        
        // Envia uma requisição AJAX para excluir o tutor
        fetch(`/tutores/deletar_tutor/${tutorId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Adiciona o token CSRF
                'Content-Type': 'application/json'
            },
        })
        .then(response => {
            if (response.ok) {
                // Recarrega a página após a exclusão
                window.location.reload();
            } else {
                alert("Erro ao excluir o tutor.");
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
    }
}

function fecharModal() {
    document.getElementById('confirmModal').style.display = 'none';
}

// Função para obter o token CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}