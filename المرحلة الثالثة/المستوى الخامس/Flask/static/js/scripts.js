function validateForm() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username.trim() === '' || password.trim() === '') {
        alert('يرجى ملء جميع الحقول');
        return false;
    }
    return true;
}