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
    if (!selected) {
        alert("Por favor, selecione um tutor para excluir.");
        return;
    }

    const tutorId = selected.value;

    fetch(`/tutores/deletar/${tutorId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (response.ok) {
            window.location.reload(); // Recarrega a página após a exclusão
        } else {
            alert("Erro ao excluir o tutor.");
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Erro ao excluir o tutor.");
    });

    fecharModal();
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