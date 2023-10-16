document.addEventListener("DOMContentLoaded", function () {
    var termsPanel = document.getElementById("termsPanel"); // Add this line
    var overlay = document.querySelector(".overlay");

    function openPanel(panel) {
        panel.classList.add("open");
        panel.style.maxHeight = "500px";
        overlay.style.transition = "background 0.5s, pointer-events 0s 0.5s"; 
        overlay.classList.add("active");
    }

    var closeButton = document.getElementById("closeButton");
    closeButton.addEventListener("click", function () {
        termsPanel.classList.remove("open");
        termsPanel.style.maxHeight = "0";
        overlay.style.transition = "background 0.5s, pointer-events 0s"; 
        overlay.classList.remove("active");
    });

    // Open terms panel when clicking "Terms & Conditions"
    var termsLink = document.getElementById("terms-link");
    termsLink.addEventListener("click", function (event) {
        event.preventDefault();
        openPanel(termsPanel);
    });
});
