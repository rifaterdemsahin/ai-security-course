function loadMenu() {
    const menuContainer = document.getElementById('menu-container');
    if (menuContainer) {
        const pathPrefix = window.location.pathname.includes('/5_Symbols/') ? '' : '5_Symbols/';

        menuContainer.innerHTML = `
        <nav class="top-nav">
            <div class="nav-container">
                <a href="/${pathPrefix}index.html" class="nav-brand">🛡️ AI Security Course</a>
                <ul class="nav-menu">
                    <li class="nav-item">
                        <a href="/${pathPrefix}index.html" class="nav-link home-link">🏠 Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 1/index.html" class="nav-link">
                            📚 Lesson 1: Attacker's Playbook
                            <span class="lesson-badge" style="background: #667eea;">Vulnerabilities</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 2/index.html" class="nav-link">
                            🛡️ Lesson 2: Building the Shield
                            <span class="lesson-badge" style="background: #28a745;">Defenses</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="/${pathPrefix}Lessons/Lesson 3/index.html" class="nav-link">
                            🔴 Lesson 3: Adversarial Testing
                            <span class="lesson-badge">Testing</span>
                        </a>
                    </li>
                </ul>
            </div>
        </nav>
        `;
    }
}

document.addEventListener('DOMContentLoaded', loadMenu);
