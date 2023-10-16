document.addEventListener("DOMContentLoaded", function () {
    var usernameElement = document.getElementById("username");
    var userPanel = document.getElementById("userPanel");
    var editForm = document.getElementById("editForm");
    var overlay = document.querySelector(".overlay");

    usernameElement.addEventListener("click", function () {
        userPanel.classList.toggle("open");
        userPanel.style.maxHeight = userPanel.classList.contains("open") ? "1000px" : "0";
        overlay.style.transition = "background 0.5s, pointer-events 0s 0.5s"; 
        overlay.classList.add("active");
    });

    var closeButton = document.getElementById("closeButton");
    closeButton.addEventListener("click", function () {
        userPanel.classList.remove("open");
        userPanel.style.maxHeight = "0";
        overlay.style.transition = "background 0.5s, pointer-events 0s"; 
        overlay.classList.remove("active");
    });

    editForm.addEventListener("submit", function (event) {
        event.preventDefault();

        var editedUsername = document.getElementById("editUsername").value;
        var editedPassword = document.getElementById("editPassword").value;
        var editedEmail = document.getElementById("editEmail").value;

        // TODO: Actions to update the user's information, e.g., send to a server

        userPanel.classList.remove("open");
        userPanel.style.maxHeight = "0";
        overlay.style.transition = "background 0.5s, pointer-events 0s";
        overlay.classList.remove("active");
    });
});