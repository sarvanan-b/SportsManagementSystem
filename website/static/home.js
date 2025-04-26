const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
    
});

btnPopup.addEventListener('click', () => {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
});

// Add this to your existing JavaScript or create a new JS file
document.addEventListener("DOMContentLoaded", function () {
    const closeButtons = document.querySelectorAll(".icon-close");

    closeButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const flashMessage = this.closest(".flash-message");
            if (flashMessage) {
                flashMessage.style.display = "none";
            }
        });
    });

    // Auto-hide success messages after a certain time (e.g., 5 seconds)
    const successMessages = document.querySelectorAll(".flash-message.success");

    successMessages.forEach((message) => {
        setTimeout(() => {
            message.style.display = "none";
        }, 5000);
    });
});



 // JavaScript function for logout
 function logout() {
    // Redirect to the logout page or perform logout logic
    window.location.href = "{{url_for('views.home')}}";
}
