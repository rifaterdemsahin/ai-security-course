/**
 * Page Configurations
 * Centralized configuration for all pages to eliminate hardcoded values
 */

const PageConfig = {
    lessons: {
        lesson1: {
            title: "Lesson 1: The Attacker's Playbook - AI Security Course",
            lessonHeader: {
                title: "Lesson 1: The Attacker's Playbook",
                subtitle: "Understanding AI Vulnerabilities",
                icon: "bi-shield-exclamation",
                bgColor: "bg-primary",
                duration: "60 minutes",
                objective: "LO1"
            },
            basePath: "../../"
        },
        lesson2: {
            title: "Lesson 2: Building the Shield - AI Security Course",
            lessonHeader: {
                title: "Lesson 2: Building the Shield", 
                subtitle: "Proactive Defense Strategies",
                icon: "bi-shield-check",
                bgColor: "bg-success",
                duration: "60 minutes",
                objective: "LO2"
            },
            basePath: "../../"
        },
        lesson3: {
            title: "Lesson 3: Adversarial Testing - AI Security Course",
            lessonHeader: {
                title: "Lesson 3: Adversarial Testing",
                subtitle: "and the Continuous Security Cycle", 
                icon: "bi-bug",
                bgColor: "bg-danger",
                duration: "60 minutes",
                objective: "LO3"
            },
            basePath: "../../"
        }
    },
    main: {
        title: "AI Security Course - Interactive Learning Platform",
        basePath: ""
    }
};

// Helper function to get current page config based on URL
function getCurrentPageConfig() {
    const path = window.location.pathname;
    
    if (path.includes('Lesson 1')) {
        return PageConfig.lessons.lesson1;
    } else if (path.includes('Lesson 2')) {
        return PageConfig.lessons.lesson2;
    } else if (path.includes('Lesson 3')) {
        return PageConfig.lessons.lesson3;
    } else {
        return PageConfig.main;
    }
}

// Export for global use
window.PageConfig = PageConfig;
window.getCurrentPageConfig = getCurrentPageConfig;