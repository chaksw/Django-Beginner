const importBtn = document.getElementById("importBtn");
const importModal = new bootstrap.Modal(document.getElementById("importModal"));

const showModal = function () {
    importModal.show();
};

importBtn.addEventListener("click", showModal);
