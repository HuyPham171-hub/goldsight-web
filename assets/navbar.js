// Update active nav link based on current path
function updateActiveNavLink() {
    const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('data-path');
        const isActive = currentPath === linkPath || 
                        (linkPath !== '/' && currentPath.startsWith(linkPath));
        
        if (isActive) {
            link.style.color = 'var(--amber-9)';
            link.style.fontWeight = 'bold';
            link.style.textDecoration = 'underline';
        } else {
            link.style.color = 'var(--gray-11)';
            link.style.fontWeight = 'medium';
            link.style.textDecoration = 'none';
        }
    });
}

// Run on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateActiveNavLink);
} else {
    updateActiveNavLink();
}

// Also run on navigation (for SPA routing)
window.addEventListener('popstate', updateActiveNavLink);
