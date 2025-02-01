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
        // Redireciona para a URL de exclusão do tutor selecionado
        window.location.href = `/tutores/deletar_tutor/${tutorId}/`;
    }
}

function fecharModal() {
    document.getElementById('confirmModal').style.display = 'none';
}