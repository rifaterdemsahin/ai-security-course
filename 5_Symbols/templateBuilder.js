/**
 * HTML Template Builder
 * Provides reusable components for common page sections
 */

class TemplateBuilder {
    /**
     * Generates the common HTML head section
     * @param {Object} config - Page configuration
     * @param {string} config.title - Page title
     * @param {string} config.basePath - Base path for CSS/JS files (e.g., "../../" for lesson pages)
     */
    static getHeadSection(config) {
        const { title, basePath = '' } = config;
        
        return `
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="${basePath}style.css">
    <link rel="stylesheet" href="${basePath}menu.css">
    <link rel="stylesheet" href="${basePath}footer.css">
    <script src="${basePath}footer.js"></script>`;
    }

    /**
     * Generates the build status section
     */
    static getBuildStatusSection() {
        return `
    <!-- Build Status -->
    <div class="container-fluid">
        <div class="alert alert-success d-flex justify-content-between align-items-center mb-0" role="alert">
            <div class="d-flex align-items-center">
                <i class="bi bi-check-circle-fill me-2"></i>
                <span class="fw-bold">Build Status: Deployed</span>
                <span class="ms-3 text-muted">Last Deployed: <span id="deploy-time">__DEPLOY_TIME__</span></span>
            </div>
            <a href="https://github.com/rifaterdemsahin/ai-security-course/tree/main" target="_blank" class="btn btn-outline-success btn-sm">
                <i class="bi bi-github me-1"></i>View on GitHub
            </a>
        </div>
    </div>`;
    }

    /**
     * Generates a lesson header section
     * @param {Object} config - Lesson configuration
     * @param {string} config.title - Lesson title
     * @param {string} config.subtitle - Lesson subtitle
     * @param {string} config.icon - Bootstrap icon class
     * @param {string} config.bgColor - Bootstrap background color class
     * @param {string} config.duration - Lesson duration
     * @param {string} config.objective - Learning objective
     */
    static getLessonHeader(config) {
        const { title, subtitle, icon, bgColor, duration, objective } = config;
        
        return `
        <!-- Lesson Header -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="${bgColor} text-white p-4 rounded-3 text-center">
                    <h1 class="display-4 fw-bold mb-3">
                        <i class="bi ${icon} me-2"></i>
                        ${title}
                    </h1>
                    <p class="lead mb-3">${subtitle}</p>
                    <div class="badge bg-light text-dark fs-6 px-3 py-2">
                        <i class="bi bi-clock me-1"></i>Duration: ${duration} | Learning Objective: ${objective}
                    </div>
                </div>
            </div>
        </div>`;
    }

    /**
     * Generates the footer scripts section
     * @param {string} basePath - Base path for JS files (e.g., "../../" for lesson pages)
     */
    static getFooterScripts(basePath = '') {
        return `
    <div id="footer-container"></div>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    
    <!-- Custom JS -->
    <script src="${basePath}menu.js"></script>
    <script src="${basePath}buildStatus.js"></script>`;
    }

    /**
     * Inserts templates into the page based on data attributes
     */
    static initializeTemplates() {
        // Auto-generate lesson headers
        const headerElement = document.querySelector('[data-lesson-header]');
        if (headerElement) {
            const config = JSON.parse(headerElement.getAttribute('data-lesson-header'));
            headerElement.innerHTML = this.getLessonHeader(config);
        }

        // Auto-generate build status
        const buildStatusElement = document.querySelector('[data-build-status]');
        if (buildStatusElement) {
            buildStatusElement.innerHTML = this.getBuildStatusSection();
        }
    }
}

// Auto-initialize templates when DOM loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => TemplateBuilder.initializeTemplates());
} else {
    TemplateBuilder.initializeTemplates();
}

// Export for global use
window.TemplateBuilder = TemplateBuilder;