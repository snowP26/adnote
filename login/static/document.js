// document.js


document.addEventListener('DOMContentLoaded', function () {
    let titleText = document.getElementById('titleText');
    let userTitleInput = document.getElementById('userTitleInput');


    titleText.addEventListener('click', function () {
        showInputField();
    });


    userTitleInput.addEventListener('blur', function () {
        saveAndHideTitle();
    });


    userTitleInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            saveAndHideTitle();
        }
    });


    document.addEventListener('click', function (event) {
        if (!titleText.contains(event.target)) {
            saveAndHideTitle();
        }
    });


    function showInputField() {
        titleText.style.display = 'none';
        userTitleInput.style.display = 'inline-block';
        userTitleInput.value = titleText.innerText.trim();
        userTitleInput.focus();
    }


    function saveAndHideTitle() {
        let newTitle = userTitleInput.value.trim();
        if (newTitle !== '') {
            saveTitle(newTitle);
            titleText.innerText = newTitle;
            titleText.style.display = 'inline-block';
            userTitleInput.style.display = 'none';
            userTitleInput.value = '';
        } else {
            titleText.style.display = 'inline-block';
            userTitleInput.style.display = 'none';
        }
    }


    function saveTitle(newTitle) {
        // Send an AJAX request to the server to save the new title
        fetch('/update_title/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Include CSRF token
            },
            body: JSON.stringify({ title: newTitle })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Optionally handle success response
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    }


    // Function to get CSRF token from cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
