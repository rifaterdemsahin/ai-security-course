document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchResultsContainer = document.getElementById('search-results');

    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const query = searchInput.value;
            if (query) {
                performSearch(query);
            }
        });
    }

    function performSearch(query) {
        // NOTE: This is a mock search implementation.
        // A real implementation would require a backend to call the search tool.
        console.log('Performing search for:', query);

        // Mock search results
        const mockResults = {
            output: [
                {
                    file_path: '4_formulas/outline/module1.md',
                    line_number: 5,
                    line: '**Duration:** Approximately 21 minutes'
                },
                {
                    file_path: '5_Symbols/Lessons/Lesson 1/index.html',
                    line_number: 30,
                    line: '<div data-lesson-header=\'{\"title\":\"Lesson 1: The Attacker&apos;s Playbook\",\"subtitle\":\"Understanding AI Vulnerabilities\",\"icon\":\"bi-shield-exclamation\",\"bgColor\":\"bg-primary\",\"duration\":\"21 minutes\",\"objective\":\"LO1\"}\'></div>'
                }
            ]
        };

        displayResults(mockResults);
    }

    function displayResults(results) {
        searchResultsContainer.innerHTML = ''; // Clear previous results

        if (results.output && results.output.length > 0) {
            const resultList = document.createElement('ul');
            results.output.forEach(result => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    <a href="#" data-filepath="${result.file_path}" data-line="${result.line_number}">
                        <strong>${result.file_path}</strong> (line ${result.line_number})
                    </a>
                    <pre><code>${escapeHtml(result.line)}</code></pre>
                `;
                resultList.appendChild(listItem);
            });
            searchResultsContainer.appendChild(resultList);
        } else {
            searchResultsContainer.innerHTML = '<p>No results found.</p>';
        }
    }

    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
});