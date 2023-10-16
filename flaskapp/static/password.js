document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const acceptTncCheckbox = document.getElementById("tickbox");
    const loginButton = document.getElementById("login-button");
    const bulletPoints = document.querySelectorAll("#password-strength li");

    acceptTncCheckbox.addEventListener("change", checkAllConditionsMet);

    function checkAllConditionsMet() {
        const password = passwordInput.value;
        const conditionsMet = checkPasswordStrength(password);

        bulletPoints.forEach((point, index) => {
            if (conditionsMet[index]) {
                point.classList.remove("red");
                point.classList.add("green");
            } else {
                point.classList.remove("green");
                point.classList.add("red");
            }
        });

        const allConditionsMet = conditionsMet.every((condition) => condition);
        const isAcceptTncChecked = acceptTncCheckbox.checked;

        console.log(allConditionsMet)
        console.log(acceptTncCheckbox)

        if (allConditionsMet && isAcceptTncChecked) {
            loginButton.disabled = false;
        } else {
            loginButton.disabled = true;
        }
    }

    passwordInput.addEventListener("input", checkAllConditionsMet);

    function checkPasswordStrength(password) {
        const minLength = password.length >= 16;
        const hasUppercase = /[A-Z]/.test(password);
        const hasLowercase = /[a-z]/.test(password);
        const hasDigit = /\d/.test(password);
        const hasSpecialChar = /[\!\@\#\$\%\^\&\*\)\(\+\=\.\<\>\{\}\[\]\:\;\'\"\|\~\`\_\-]/g.test(password); // Updated regex for special characters

        return [minLength, hasUppercase, hasLowercase, hasDigit, hasSpecialChar];
    }
});
