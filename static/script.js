document.addEventListener("DOMContentLoaded", function () {

    //passwords match or don't

    const signupForm = document.getElementById("signup-form");

    if (signupForm) {
        const passwordField = document.getElementById("password");
        const confirmField = document.getElementById("confirm_password");
        const warning = document.getElementById("password-warning");

        function checkPasswordsMatch() {
            if (confirmField.value.length === 0) {
                warning.style.display = "none";
                return;
            }
            if (passwordField.value !== confirmField.value) {
                warning.style.display = "block";
            } else {
                warning.style.display = "none";
            }
        }

        passwordField.addEventListener("input", checkPasswordsMatch);
        confirmField.addEventListener("input", checkPasswordsMatch);

        signupForm.addEventListener("submit", function (e) {
            if (passwordField.value !== confirmField.value) {
                e.preventDefault();
                warning.style.display = "block";
            }
        });
    }
//flash mssg timeout define
    const flashBox = document.querySelector(".flash-box");
    if (flashBox) {
        setTimeout(function () {
            flashBox.style.transition = "opacity 0.5s ease";
            flashBox.style.opacity = "0";
        }, 4000);
    }
});
