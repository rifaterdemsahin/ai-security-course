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
        console.log('Performing search for:', query);
        
        const searchResultsContainer = document.getElementById('search-results');
        const mainContent = document.querySelector('.container.my-4');
        
        // Show search results container and hide main content
        if (searchResultsContainer) {
            searchResultsContainer.classList.add('show');
            searchResultsContainer.style.display = 'block';
        }
        if (mainContent) {
            mainContent.style.display = 'none';
        }

        fetch('search.json')
            .then(response => response.json())
            .then(data => displayResults(data, query))
            .catch(error => {
                console.error('Error fetching search results:', error);
                const searchResultsContent = document.getElementById('search-results-content');
                if (searchResultsContent) {
                    searchResultsContent.innerHTML = '<div class="alert alert-danger"><i class="bi bi-exclamation-triangle me-2"></i>Error loading search results.</div>';
                }
            });
    }

function displayResults(data, query) {
    const searchResultsContent = document.getElementById('search-results-content');
    
    if (!searchResultsContent) {
        console.error('Search results content container not found');
        return;
    }

    // Search through all data types
    const allResults = [];
    const queryLower = query.toLowerCase();

    // Search in modules
    if (data.modules) {
        data.modules.forEach(module => {
            if (matchesQuery(module, queryLower, ['title', 'description', 'keywords'])) {
                allResults.push({
                    type: 'Module',
                    title: module.title,
                    description: module.description,
                    icon: 'bi-layers',
                    color: 'primary',
                    details: `Duration: ${module.duration} | Objective: ${module.objective}`
                });
            }
        });
    }

    // Search in lessons
    if (data.lessons) {
        data.lessons.forEach(lesson => {
            if (matchesQuery(lesson, queryLower, ['title', 'subtitle', 'concepts'])) {
                allResults.push({
                    type: 'Lesson',
                    title: lesson.title,
                    description: lesson.subtitle,
                    icon: 'bi-play-circle',
                    color: 'success',
                    details: `Duration: ${lesson.duration} | Objective: ${lesson.objective}`,
                    file_path: lesson.file_path
                });
            }
        });
    }

    // Search in technical terms
    if (data.technical_terms) {
        data.technical_terms.forEach(term => {
            if (matchesQuery(term, queryLower, ['term', 'definition'])) {
                allResults.push({
                    type: 'Technical Term',
                    title: `${term.emoji || '📖'} ${term.term}`,
                    description: term.definition,
                    icon: 'bi-book',
                    color: 'info',
                    details: 'Definition',
                    file_path: term.card_file
                });
            }
        });
    }

    // Search in learning objectives
    if (data.learning_objectives) {
        data.learning_objectives.forEach(lo => {
            if (matchesQuery(lo, queryLower, ['id', 'description'])) {
                allResults.push({
                    type: 'Learning Objective',
                    title: lo.id,
                    description: lo.description,
                    icon: 'bi-target',
                    color: 'warning',
                    details: 'Course Objective'
                });
            }
        });
    }

    // Search in content files
    if (data.content_files) {
        data.content_files.forEach(file => {
            if (matchesQuery(file, queryLower, ['title', 'type', 'keywords'])) {
                allResults.push({
                    type: 'Content File',
                    title: file.title,
                    description: `${file.type} - ${file.keywords?.join(', ') || ''}`,
                    icon: 'bi-file-text',
                    color: 'secondary',
                    details: file.type,
                    file_path: file.file_path
                });
            }
        });
    }

    // Search in hands-on labs
    if (data.hands_on_labs) {
        data.hands_on_labs.forEach(lab => {
            if (matchesQuery(lab, queryLower, ['title', 'description'])) {
                allResults.push({
                    type: 'Hands-on Lab',
                    title: lab.title,
                    description: lab.description,
                    icon: 'bi-code-slash',
                    color: 'danger',
                    details: `Duration: ${lab.duration} | ${lab.module}`,
                    objective: lab.objective
                });
            }
        });
    }

    // Search in key concepts
    if (data.key_concepts) {
        data.key_concepts.forEach(concept => {
            if (concept.toLowerCase().includes(queryLower)) {
                allResults.push({
                    type: 'Key Concept',
                    title: concept,
                    description: 'Core concept in AI Security',
                    icon: 'bi-lightbulb',
                    color: 'dark',
                    details: 'Concept'
                });
            }
        });
    }

    // Search in search index for specific content
    if (data.search_index) {
        data.search_index.forEach(item => {
            if (matchesQuery(item, queryLower, ['content', 'keywords'])) {
                allResults.push({
                    type: 'Content Match',
                    title: `Line ${item.line_number} in ${item.file_path}`,
                    description: item.content,
                    icon: 'bi-search',
                    color: 'muted',
                    details: item.keywords?.join(', ') || '',
                    file_path: item.file_path,
                    line_number: item.line_number
                });
            }
        });
    }

    // Display results
    if (allResults.length > 0) {
        let resultsHTML = `
            <div class="d-flex justify-content-between align-items-center mb-3">
                <h6 class="mb-0">Found ${allResults.length} result(s) for "${escapeHtml(query)}"</h6>
                <button class="btn btn-outline-secondary btn-sm" onclick="clearSearch()">
                    <i class="bi bi-x"></i> Clear
                </button>
            </div>
            <div class="row">
        `;

        allResults.forEach((result, index) => {
            // Generate the appropriate href for the file
            let href = '#';
            if (result.file_path) {
                if (result.file_path.endsWith('.md')) {
                    // For markdown files, use renderer.html with file parameter
                    href = `renderer.html?file=${encodeURIComponent(result.file_path)}`;
                } else if (result.file_path.endsWith('.html')) {
                    // For HTML files, link directly
                    href = result.file_path;
                } else {
                    // For other files, try to link directly
                    href = result.file_path;
                }
                
                // If there's a line number, add it as a fragment
                if (result.line_number) {
                    href += `#line-${result.line_number}`;
                }
            }
            
            const cardContent = `
                <div class="card h-100 border-${result.color}">
                    <div class="card-header bg-${result.color} text-white">
                        <div class="d-flex align-items-center">
                            <i class="${result.icon} me-2"></i>
                            <small class="fw-bold">${result.type}</small>
                        </div>
                    </div>
                    <div class="card-body">
                        <h6 class="card-title">${highlightQuery(escapeHtml(result.title), query)}</h6>
                        <p class="card-text small">${highlightQuery(escapeHtml(result.description), query)}</p>
                        ${result.details ? `<div class="text-muted small">${escapeHtml(result.details)}</div>` : ''}
                        ${result.file_path ? `<div class="mt-2"><small class="text-muted"><i class="bi bi-folder me-1"></i>${escapeHtml(result.file_path)}</small></div>` : ''}
                    </div>
                </div>
            `;
            
            resultsHTML += `
                <div class="col-md-6 col-lg-4 mb-3">
                    ${result.file_path ? 
                        `<a href="${href}" class="text-decoration-none" style="color: inherit;">${cardContent}</a>` : 
                        cardContent
                    }
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
                Try searching for terms like: "adversarial", "defense", "privacy", "attack", "security", "evasion", "training", "testing"
            </div>
        `;
    }
}

function matchesQuery(item, queryLower, fields) {
    return fields.some(field => {
        const value = item[field];
        if (typeof value === 'string') {
            return value.toLowerCase().includes(queryLower);
        } else if (Array.isArray(value)) {
            return value.some(v => v.toLowerCase().includes(queryLower));
        }
        return false;
    });
}

function clearSearch() {
    const searchResultsContainer = document.getElementById('search-results');
    const mainContent = document.querySelector('.container.my-4');
    const searchInput = document.getElementById('search-input');
    
    if (searchResultsContainer) {
        searchResultsContainer.classList.remove('show');
        searchResultsContainer.style.display = 'none';
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
    if (typeof unsafe !== 'string') {
        return '';
    }
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}