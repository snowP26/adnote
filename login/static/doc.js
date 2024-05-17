document.addEventListener('DOMContentLoaded', function () {
    const titleText = document.getElementById('titleText');
    const userTitleInput = document.getElementById('userTitleInput');

    const shareDialog = document.getElementById('shareDialog');
    const deleteDialog = document.getElementById('deleteDialog');

    const shareButton = document.getElementById('share');
    const deleteButton = document.getElementById('delete');
    const confirmShareButton = document.getElementById('confirmShare');
    const cancelShareButton = document.getElementById('cancelShare');
    const confirmDeleteButton = document.getElementById('confirmDelete');
    const cancelDeleteButton = document.getElementById('cancelDelete');

    const toolbarButtons = {
        'bold': () => document.execCommand('bold'),
        'italic': () => document.execCommand('italic'),
        'underline': () => document.execCommand('underline'),
        'undo': () => document.execCommand('undo'), // Undo functionality
        'redo': () => document.execCommand('redo'), // Redo functionality
    };

    const toolbarIcons = document.querySelectorAll('.toolbar .icon');
    toolbarIcons.forEach(icon => {
        icon.addEventListener('click', () => {
            const id = icon.id;
            if (id && toolbarButtons[id]) {
                toolbarButtons[id]();
            }
        });
    });

    shareButton.addEventListener('click', function () {
        shareDialog.style.display = 'block';
    });

    cancelShareButton.addEventListener('click', function () {
        shareDialog.style.display = 'none';
    });

    confirmShareButton.addEventListener('click', function () {
        shareDialog.style.display = 'none';
    });

    deleteButton.addEventListener('click', function () {
        deleteDialog.style.display = 'block';
    });

    cancelDeleteButton.addEventListener('click', function () {
        deleteDialog.style.display = 'none';
    });

    confirmDeleteButton.addEventListener('click', function () {
        deleteDialog.style.display = 'none';
    });

    titleText.addEventListener('click', function () {
        titleText.style.display = 'none';
        userTitleInput.style.display = 'inline-block';
        userTitleInput.value = titleText.innerText.trim();
        userTitleInput.focus();
    });

    userTitleInput.addEventListener('blur', saveAndHideTitle);
    userTitleInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            saveAndHideTitle();
        }
    });

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

    // Function to save title (example)
    function saveTitle(newTitle) {
        console.log('Title saved:', newTitle);

    }

    // Function to get CSRF token from cookie (example)
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
