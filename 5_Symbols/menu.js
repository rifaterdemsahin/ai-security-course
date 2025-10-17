function loadMenu() {
    const menuContainer = document.getElementById('menu-container');
    if (menuContainer) {
        const currentPath = window.location.pathname;
        
        // Determine base path for GitHub Pages
        let basePath = '';
        if (currentPath.includes('/ai-security-course/')) {
            // We're on GitHub Pages
            basePath = '/ai-security-course/5_Symbols/';
        } else if (currentPath.includes('/5_Symbols/')) {
            // We're already in 5_Symbols
            basePath = './';
            if (currentPath.includes('Lessons/')) {
                basePath = '../../';
            } else if (currentPath.includes('Apply/')) {
                basePath = '../';
            }
        } else {
            // We're at root level
            basePath = '5_Symbols/';
        }
        
        // Determine which lesson is active
        let activeLesson = '';
        if (currentPath.includes('Lesson 1')) activeLesson = 'lesson1';
        else if (currentPath.includes('Lesson 2')) activeLesson = 'lesson2';
        else if (currentPath.includes('Lesson 3')) activeLesson = 'lesson3';

        menuContainer.innerHTML = `
        <nav class="top-nav">
            <div class="nav-container">
                <a href="${basePath}index.html" class="nav-brand">🛡️ AI Security Course</a>
                
                <!-- Admin Mode Toggle -->
                <div class="admin-toggle-container">
                    <label class="admin-toggle">
                        <input type="checkbox" id="admin-mode-toggle" onchange="toggleAdminMode()">
                        <span class="admin-slider">
                            <i class="bi bi-person-fill"></i>
                            <i class="bi bi-gear-fill"></i>
                        </span>
                        <span class="admin-label">Admin</span>
                    </label>
                </div>
                
                <button class="mobile-menu-toggle d-md-none" onclick="toggleMobileMenu()">
                    <i class="bi bi-list"></i>
                </button>
                
                <ul class="nav-menu d-md-flex" id="nav-menu">
                    <li class="nav-item">
                        <a href="${basePath}index.html" class="nav-link home-link">
                            <i class="bi bi-house-fill me-2"></i>
                            <span class="d-none d-lg-inline">Home</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="${basePath}Lessons/Lesson 1/index.html" class="nav-link ${activeLesson === 'lesson1' ? 'active' : ''}">
                            <i class="bi bi-book me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 1: Attacker's Playbook</span>
                            <span class="d-lg-none">Lesson 1</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #667eea;">Vulnerabilities</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="${basePath}Lessons/Lesson 2/index.html" class="nav-link ${activeLesson === 'lesson2' ? 'active' : ''}">
                            <i class="bi bi-shield-check me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 2: Building the Shield</span>
                            <span class="d-lg-none">Lesson 2</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #28a745;">Defenses</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="${basePath}Lessons/Lesson 3/index.html" class="nav-link ${activeLesson === 'lesson3' ? 'active' : ''}">
                            <i class="bi bi-bug me-2"></i>
                            <span class="d-none d-lg-inline">Lesson 3: Adversarial Testing</span>
                            <span class="d-lg-none">Lesson 3</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #dc3545;">Testing</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="${basePath}Apply/memory_cards.html" class="nav-link">
                            <i class="bi bi-collection me-2"></i>
                            <span class="d-none d-lg-inline">Memory Cards</span>
                            <span class="d-lg-none">Cards</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #6f42c1;">Practice</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="${basePath}renderer.html?file=../student-welcome.md" class="nav-link get-started-link">
                            <i class="bi bi-book me-2"></i>
                            <span class="d-none d-lg-inline">Course Guide</span>
                            <span class="d-lg-none">Guide</span>
                            <span class="lesson-badge d-none d-xl-inline" style="background: #28a745;">Start Here</span>
                        </a>
                    </li>
                    <li class="nav-item nav-search">
                        <form id="search-form" class="d-flex">
                            <input id="search-input" class="form-control me-2" type="search" placeholder="Search..." aria-label="Search">
                            <button class="btn btn-outline-light" type="submit"><i class="bi bi-search"></i></button>
                        </form>
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

// Admin mode functionality
function toggleAdminMode() {
    const isAdminMode = document.getElementById('admin-mode-toggle').checked;
    localStorage.setItem('adminMode', isAdminMode);
    
    // Toggle admin-only content
    const adminRows = document.querySelectorAll('.admin-only');
    adminRows.forEach(row => {
        if (isAdminMode) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
    
    // Toggle student mode banner
    const studentBanner = document.getElementById('student-mode-banner');
    if (studentBanner) {
        if (isAdminMode) {
            studentBanner.classList.add('hidden');
        } else {
            studentBanner.classList.remove('hidden');
        }
    }
    
    // Toggle setup banner
    const setupBanner = document.querySelector('.setup-banner');
    if (setupBanner) {
        if (isAdminMode) {
            setupBanner.style.display = 'none';
        } else {
            setupBanner.style.display = '';
        }
    }
    
    // Update toggle appearance
    updateAdminToggleAppearance(isAdminMode);
}

function updateAdminToggleAppearance(isAdminMode) {
    const toggle = document.querySelector('.admin-toggle');
    const label = document.querySelector('.admin-label');
    
    if (toggle) {
        if (isAdminMode) {
            toggle.classList.add('admin-active');
            label.textContent = 'Admin';
            label.style.color = '#dc3545';
        } else {
            toggle.classList.remove('admin-active');
            label.textContent = 'Student';
            label.style.color = '#28a745';
        }
    }
}

// Initialize admin mode on page load
function initializeAdminMode() {
    const savedAdminMode = localStorage.getItem('adminMode') === 'true';
    const adminToggle = document.getElementById('admin-mode-toggle');
    
    if (adminToggle) {
        adminToggle.checked = savedAdminMode;
        toggleAdminMode();
    }
}

// Initialize admin mode after menu loads
document.addEventListener('DOMContentLoaded', function() {
    loadMenu();
    // Small delay to ensure menu is loaded
    setTimeout(initializeAdminMode, 100);
});
