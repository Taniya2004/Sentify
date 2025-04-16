document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.getElementById('userToggleBtn');
    const dropdown = document.getElementById('userDropdown');

    toggleBtn.addEventListener('click', function() {
        if (dropdown.style.display === 'none' || dropdown.style.display === '') {
            dropdown.style.display = 'block';
        } else {
            dropdown.style.display = 'none';
        }
    });

    // Close dropdown if clicked outside
    document.addEventListener('click', function(event) {
        if (!toggleBtn.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.style.display = 'none';
        }
    });
});
