document.addEventListener("DOMContentLoaded", function() {
   // Function to remove active class from all links
   function removeActiveClass() {
       navLinks.forEach(function(link) {
           link.classList.remove("active");
       });
   }

   // Get all navigation links
   var navLinks = document.querySelectorAll(".sidebar ul li a");

   // Loop through each link
   navLinks.forEach(function(navLink) {
       // Add click event listener
       navLink.addEventListener("click", function() {
           removeActiveClass(); // Remove active class from all links
           // Add active class to the clicked link
           this.classList.add("active");
       });
   });

   // Listen for hash changes
   window.addEventListener("hashchange", function() {
       // Remove active class when navigating away from the current section
       removeActiveClass();
       // Get the current hash
       var currentHash = window.location.hash;
       // Check if there's a corresponding navigation link with the current hash
       var correspondingNavLink = document.querySelector('.sidebar ul li a[href="' + currentHash + '"]');
       // If a corresponding navigation link is found, add the active class
       if (correspondingNavLink) {
           correspondingNavLink.classList.add("active");
       }
   });

   // Check if there's a hash in the URL when the page loads
   if (window.location.hash) {
       // Get the current hash
       var currentHash = window.location.hash;
       // Check if there's a corresponding navigation link with the current hash
       var correspondingNavLink = document.querySelector('.sidebar ul li a[href="' + currentHash + '"]');
       // If a corresponding navigation link is found, add the active class
       if (correspondingNavLink) {
           correspondingNavLink.classList.add("active");
       }
   }
});
