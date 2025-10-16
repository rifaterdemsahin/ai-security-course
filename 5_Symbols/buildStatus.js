/**
 * Build Status Management
 * Handles the dynamic updating of build status information across all pages
 */

class BuildStatusManager {
    constructor() {
        this.baseDeployTime = '2025-10-16 04:14:27 UTC';
    }

    /**
     * Updates the build status timestamp
     */
    updateBuildStatus() {
        const deployTimeElement = document.getElementById('deploy-time');
        if (deployTimeElement) {
            deployTimeElement.textContent = this.baseDeployTime;
        }
    }

    /**
     * Initializes build status functionality
     */
    init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.updateBuildStatus());
        } else {
            this.updateBuildStatus();
        }
    }
}

// Create global instance and auto-initialize
window.buildStatusManager = new BuildStatusManager();
window.buildStatusManager.init();