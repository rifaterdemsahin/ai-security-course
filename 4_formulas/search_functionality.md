# Search Functionality Explained

This document explains the implementation of the search functionality in the AI Security Course project.

## 1. Frontend Implementation

The frontend part of the search functionality is responsible for capturing user input and displaying the search results.

### 1.1. Search Bar in the Menu

The search bar is dynamically added to the top navigation menu using JavaScript.

- **File:** `5_Symbols/menu.js`
- **How it works:** A new list item (`<li>`) containing a search form is appended to the main navigation `<ul>` element.

### 1.2. Styling the Search Bar

The search bar is styled to match the look and feel of the navigation menu.

- **File:** `5_Symbols/menu.css`
- **How it works:** Custom CSS rules are added to style the search input field and button.

### 1.3. Search Logic

The client-side search logic is handled by `search.js`.

- **File:** `5_Symbols/search.js`
- **How it works:**
    1. An event listener is attached to the search form to detect when a user submits a search query.
    2. When the form is submitted, the script retrieves the query from the input field.
    3. It then calls a function to perform the search and display the results.

### 1.4. Mock Search Implementation

Currently, the search functionality is a **mock implementation**. This means that it does not perform a real search on the project content.

- **Reason:** The search functionality requires calling a backend tool (`search_file_content`) that can search the file system. This tool cannot be called directly from the client-side JavaScript for security reasons.
- **How it works:** The `search.js` file contains mock search results that are displayed to demonstrate how the real search results would look.

## 2. Backend Implementation (Conceptual)

A complete implementation of the search functionality would require a backend component.

### 2.1. Backend Endpoint

A backend endpoint (e.g., an API route) would need to be created. This endpoint would receive the search query from the frontend.

### 2.2. Calling the Search Tool

The backend endpoint would then call the `search_file_content` tool with the received query. This tool would search the project files for the query and return the results.

### 2.3. Returning Results to the Frontend

The backend would send the search results back to the frontend in a structured format (e.g., JSON). The frontend JavaScript would then parse this data and display it in the search results container.
