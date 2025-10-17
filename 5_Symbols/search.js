document.addEventListener('DOMContentLoaded', function() {
    // Wait for menu to load first
    setTimeout(initializeSearch, 100);
});

function initializeSearch() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');

    if (searchForm && searchInput) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const query = searchInput.value.trim();
            if (query) {
                performSearch(query);
            }
        });

        // Clear search on escape key
        searchInput.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                clearSearch();
            }
        });
    }
}

    function performSearch(query) {
        // NOTE: This is a mock search implementation.
        // It fetches mock results from a JSON file.
        console.log('Performing search for:', query);

        fetch('search.json')
            .then(response => response.json())
            .then(data => displayResults(data))
            .catch(error => {
                console.error('Error fetching search results:', error);
                searchResultsContainer.innerHTML = '<p>Error loading search results.</p>';
            });
    }

function generateMockResults(query) {
    const allResults = [
        {
            file_path: '4_formulas/outline/module1.md',
            line_number: 5,
            line: '**Duration:** Approximately 21 minutes - Introduction to AI Security Vulnerabilities'
        },
        {
            file_path: '5_Symbols/Lessons/Lesson 1/index.html',
            line_number: 30,
            line: 'Lesson 1: The Attacker\'s Playbook - Understanding AI Vulnerabilities'
        },
        {
            file_path: '5_Symbols/Lessons/Lesson 2/index.html',
            line_number: 28,
            line: 'Lesson 2: Building the Shield - Proactive Defense Strategies'
        },
        {
            file_path: '3_UI/Cards/adversarial_attack.md',
            line_number: 1,
            line: '# Adversarial Attack - Crafted inputs designed to fool AI models'
        },
        {
            file_path: '3_UI/Cards/adversarial_training.md',
            line_number: 1,
            line: '# Adversarial Training - Defense technique using adversarial examples'
        },
        {
            file_path: '3_UI/Cards/differential_privacy.md',
            line_number: 1,
            line: '# Differential Privacy - Mathematical framework for privacy protection'
        }
    ];

    // Filter results based on query
    const query_lower = query.toLowerCase();
    const filteredResults = allResults.filter(result => 
        result.file_path.toLowerCase().includes(query_lower) ||
        result.line.toLowerCase().includes(query_lower)
    );

    return {
        output: filteredResults,
        query: query
    };
}

function displayResults(results, query) {
    const searchResultsContent = document.getElementById('search-results-content');
    
    if (!searchResultsContent) {
        console.error('Search results content container not found');
        return;
    }

    if (results.output && results.output.length > 0) {
        let resultsHTML = `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h6 class="mb-0">Found ${results.output.length} result(s) for "${escapeHtml(query)}"</h6>
                <button class="btn btn-outline-secondary btn-sm" onclick="clearSearch()">
                    <i class="bi bi-x"></i> Clear
                </button>
            </div>
            <div class="list-group">
        `;

        results.output.forEach((result, index) => {
            resultsHTML += `
                <div class="list-group-item">
                    <div class="d-flex w-100 justify-content-between">
                        <h6 class="mb-1">
                            <i class="bi bi-file-text me-2"></i>${escapeHtml(result.file_path)}
                        </h6>
                        <small>Line ${result.line_number}</small>
                    </div>
                    <p class="mb-1">${highlightQuery(escapeHtml(result.line), query)}</p>
                </div>
            `;
        });

        resultsHTML += '</div>';
        searchResultsContent.innerHTML = resultsHTML;
    } else {
        searchResultsContent.innerHTML = `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h6 class="mb-0">No results found for "${escapeHtml(query)}"</h6>
                <button class="btn btn-outline-secondary btn-sm" onclick="clearSearch()">
                    <i class="bi bi-x"></i> Clear
                </button>
            </div>
            <div class="alert alert-info">
                <i class="bi bi-info-circle me-2"></i>
                Try searching for terms like: "adversarial", "defense", "privacy", "attack", "security"
            </div>
        `;
    }
}

function clearSearch() {
    const searchResultsContainer = document.getElementById('search-results');
    const mainContent = document.querySelector('.container.my-4');
    const searchInput = document.getElementById('search-input');
    
    if (searchResultsContainer) {
        searchResultsContainer.classList.remove('show');
    }
    if (mainContent) {
        mainContent.style.display = 'block';
    }
    if (searchInput) {
        searchInput.value = '';
    }
}

function highlightQuery(text, query) {
    if (!query) return text;
    
    const regex = new RegExp(`(${escapeRegExp(query)})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}