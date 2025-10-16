function loadMenu() {
    const menuContainer = document.getElementById('menu-container');
    if (menuContainer) {
        const pathPrefix = window.location.pathname.includes('/5_Symbols/') ? '' : '5_Symbols/';
        const currentPath = window.location.pathname;
        
        // Determine which lesson is active
        let activeLesson = '';
        if (currentPath.includes('Lesson 1')) activeLesson = 'lesson1';
        else if (currentPath.includes('Lesson 2')) activeLesson = 'lesson2';
        else if (currentPath.includes('Lesson 3')) activeLesson = 'lesson3';

        menuContainer.innerHTML = `
        <nav class="top-nav">
            <div class="nav-container">
                <a href="/${pathPrefix}index.html" class="nav-brand">🛡️ AI Security Course</a>
                
                <button class="mobile-menu-toggle d-md-none" onclick="toggleMobileMenu()">
                    <i class="bi bi-list"></i>
                </button>
                
                <ul class="nav-menu d-md-flex" id="nav-menu">
                    <li class="nav-item">
                        <a href="/${pathPrefix}index.html" class="nav-link home-link">
                            <i class="bi bi-house-fill me-2"></i>
                            <span class="d-none d-lg-inline">Home</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 1/index.html" class="nav-link ${activeLesson === 'lesson1' ? 'active' : ''}">
                            <i class="bi bi-book me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 1: Attacker's Playbook</span>
                            <span class="d-lg-none">Lesson 1</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #667eea;">Vulnerabilities</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 2/index.html" class="nav-link ${activeLesson === 'lesson2' ? 'active' : ''}">
                            <i class="bi bi-shield-check me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 2: Building the Shield</span>
                            <span class="d-lg-none">Lesson 2</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #28a745;">Defenses</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 3/index.html" class="nav-link ${activeLesson === 'lesson3' ? 'active' : ''}">
                            <i class="bi bi-bug me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 3: Adversarial Testing</span>
                            <span class="d-lg-none">Lesson 3</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #dc3545;">Testing</span>
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
        `;
    }
}

function toggleMobileMenu() {
    const navMenu = document.getElementById('nav-menu');
    const toggleButton = document.querySelector('.mobile-menu-toggle i');
    
    if (navMenu) {
        navMenu.classList.toggle('show');
        
        // Toggle icon between hamburger and X
        if (navMenu.classList.contains('show')) {
            toggleButton.className = 'bi bi-x';
        } else {
            toggleButton.className = 'bi bi-list';
        }
    }
}

// Close mobile menu when clicking outside
document.addEventListener('click', function(event) {
    const navMenu = document.getElementById('nav-menu');
    const toggleButton = document.querySelector('.mobile-menu-toggle');
    const navContainer = document.querySelector('.nav-container');
    
    if (navMenu && navMenu.classList.contains('show')) {
        if (!navContainer.contains(event.target)) {
            navMenu.classList.remove('show');
            const toggleButtonIcon = document.querySelector('.mobile-menu-toggle i');
            if (toggleButtonIcon) {
                toggleButtonIcon.className = 'bi bi-list';
            }
        }
    }
});

// Close mobile menu when resizing to desktop
window.addEventListener('resize', function() {
    const navMenu = document.getElementById('nav-menu');
    const toggleButtonIcon = document.querySelector('.mobile-menu-toggle i');
    
    if (window.innerWidth >= 768 && navMenu) {
        navMenu.classList.remove('show');
        if (toggleButtonIcon) {
            toggleButtonIcon.className = 'bi bi-list';
        }
    }
});

document.addEventListener('DOMContentLoaded', loadMenu);
