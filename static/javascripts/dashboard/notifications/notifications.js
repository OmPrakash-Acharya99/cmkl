console.log('Notifications JavaScript file loaded');
document.addEventListener('DOMContentLoaded', function() {
    const badge = document.getElementById('unread-count');
    if (badge) {
        // Make an AJAX request to fetch the number of unread notifications
        fetch('/api/notifications/unread_count/')
            .then(response => response.json())
            .then(data => {
                if (data.unread_count > 0) {
                    badge.textContent = data.unread_count;
                    badge.style.display = 'inline';  // Show the badge
                } else {
                    badge.style.display = 'none';  // Hide the badge if there are no unread notifications
                }
            })
            .catch(error => {
                console.error('Error fetching unread notification count:', error);
            });
    }
});
