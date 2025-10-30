# HTML Writing Agent

## Description

This agent is responsible for writing and maintaining HTML code for web pages in the AI Security Course platform. It ensures that all HTML follows consistent patterns, integrates seamlessly with the existing design system, and maintains accessibility and performance standards.

## Core Mission

Write semantic, accessible, and maintainable HTML code that:
- Follows the project's established design patterns and conventions
- Integrates Bootstrap 5.3.2 framework and Bootstrap Icons consistently
- Ensures responsive design across all device sizes
- Maintains semantic HTML structure with proper heading hierarchy
- Supports both admin and student viewing modes
- Optimizes performance and user experience

## Project HTML Context & Standards

**Course Platform:** AI Security Course - Secure AI: Interpret and Protect Models  
**Framework:** Bootstrap 5.3.2  
**Icon Library:** Bootstrap Icons 1.11.1  
**Markdown Renderer:** marked.js  
**Architecture:** Static HTML with JavaScript enhancement (no build step required)  
**Deployment:** GitHub Pages + Local development

### Core Technologies & Libraries Used

```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

<!-- JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<!-- Project-specific scripts: menu.js, footer.js, search.js, buildStatus.js -->
```

### Design System & Styling Approach

**Color Scheme:**
- Primary gradient: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)` (Purple)
- Background: `#f8f9fa` (Light gray)
- Text: `#333` (Dark gray)
- White cards with subtle shadows: `0 4px 6px rgba(0, 0, 0, 0.1)`

**Typography:**
- Font Family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- Line Height: 1.6
- Responsive sizing with relative units

**Layout Patterns:**
- Max-width: 1400px centered container
- Bootstrap grid system (12-column responsive)
- Flexbox for component alignment
- Card-based layout for content grouping

### Module Structure

```
5_Symbols/
├── index.html                 # Main file listing and navigation
├── renderer.html              # Markdown file renderer
├── style.css                  # Global styles
├── menu.css                   # Navigation bar styles
├── footer.css                 # Footer styles
├── menu.js                    # Navigation system
├── footer.js                  # Footer management
├── search.js                  # Search functionality
├── buildStatus.js             # Build status display
├── pageConfig.js              # Page configuration
├── templateBuilder.js         # Template generation
└── Lessons/                   # Lesson HTML pages
└── Apply/                     # Interactive content pages
```

## HTML Writing Guidelines

### 1. Document Structure Standards

**Required HTML5 Boilerplate:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>[Page Title - Descriptive]</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    
    <!-- Custom CSS (in order: global, then component-specific) -->
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="menu.css">
    <link rel="stylesheet" href="footer.css">
    
    <!-- External Libraries as needed -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    
    <!-- Project-specific Scripts (non-blocking) -->
    <script src="menu.js"></script>
    <script src="footer.js"></script>
</head>
<body>
    <!-- Navigation Container (injected by menu.js) -->
    <div id="menu-container"></div>
    
    <!-- Main Content -->
    <main>
        <!-- Page content here -->
    </main>
    
    <!-- Footer Container (injected by footer.js) -->
    <div id="footer-container"></div>
</body>
</html>
```

**Key Principles:**
- Always use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, `<footer>`)
- Place title tags as the first meta information
- Group CSS imports before JavaScript
- Use lowercase tag names
- Use double quotes for attributes

### 2. Semantic HTML & Accessibility

**Heading Hierarchy:**
- Use `<h1>` only once per page (page title)
- Use `<h2>` for major sections
- Use `<h3>` for subsections
- Never skip heading levels (e.g., h1 → h3)

**Navigation Structure:**
```html
<nav class="top-nav">
    <div class="nav-container">
        <a href="index.html" class="nav-brand">🛡️ AI Security Course</a>
        <!-- Navigation items -->
    </div>
</nav>
```

**Form Accessibility:**
- Always use `<label>` with `for` attribute linked to input `id`
- Use semantic form elements (`<button>`, `<select>`, `<input type="...">`)
- Include `aria-label` for icon-only buttons
- Provide `aria-describedby` for complex inputs

**Link Accessibility:**
- Descriptive link text (avoid "click here")
- Include `aria-label` if link text is ambiguous
- Example: `<a href="file.md" aria-label="Read adversarial attack documentation">Adversarial Attack</a>`

### 3. Bootstrap Integration Pattern

**Container Structure:**
```html
<div class="container">
    <div class="row">
        <div class="col-md-8">
            <!-- Main content -->
        </div>
        <div class="col-md-4">
            <!-- Sidebar -->
        </div>
    </div>
</div>
```

**Common Components:**

**Cards:**
```html
<div class="card">
    <div class="card-header">
        <h5 class="card-title mb-0">
            <i class="bi bi-search me-2"></i>Search Results
        </h5>
    </div>
    <div class="card-body">
        <!-- Card content -->
    </div>
</div>
```

**Buttons:**
```html
<!-- Primary action -->
<a href="renderer.html?file=file.md" class="btn btn-primary">
    <i class="bi bi-book me-2"></i>
    Start Learning
</a>

<!-- Secondary action -->
<button class="btn btn-secondary">Secondary</button>

<!-- Custom button (setup banner) -->
<a href="renderer.html?file=../student-welcome.md" class="btn btn-setup">
    <i class="bi bi-book me-2"></i>
    Start Learning
</a>
```

**Tables:**
```html
<div class="table-container">
    <table class="file-table">
        <thead>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
            </tr>
        </thead>
        <tbody>
            <tr class="table-row-class">
                <td>Data 1</td>
                <td>Data 2</td>
            </tr>
        </tbody>
    </table>
</div>
```

**Utility Classes:**
- Spacing: `mb-0` (margin-bottom: 0), `me-2` (margin-right), `mt-3` (margin-top), `p-15` (padding)
- Text: `text-center`, `text-secondary`, `fw-bold`
- Display: `d-flex`, `justify-content-center`, `align-items-center`
- Visibility: `hidden`, `d-none`

### 4. Mode-Specific Content Patterns

**Admin vs. Student Mode:**

The platform supports two viewing modes controlled by JavaScript:

```html
<!-- Content visible only in admin mode -->
<tr class="admin-only">
    <td>Admin content</td>
</tr>

<!-- Content visible only in student mode -->
<div id="student-mode-banner" class="student-mode-banner hidden">
    <i class="bi bi-person-fill"></i>
    Student View - Showing course content only
</div>

<!-- Content visible in both modes -->
<tr class="welcome-row">
    <td>Always visible</td>
</tr>
```

**CSS Classes:**
- `.admin-only` - Hidden by default, shown when admin mode is active
- `.student-mode-banner` - Admin-only feature notification
- `.hidden` - Initially hidden (JavaScript toggles visibility)

### 5. Icon Integration

**Bootstrap Icons Usage:**

All icons use the Bootstrap Icons CDN library (1.11.1). Use the `bi` class system:

```html
<!-- Search icon with spacing -->
<i class="bi bi-search me-2"></i>

<!-- GitHub icon -->
<i class="bi bi-github"></i>

<!-- Person icon for user mode -->
<i class="bi bi-person-fill"></i>

<!-- Available icon classes: bi-book, bi-person-fill, bi-github, bi-search, etc. -->
```

**Spacing Conventions:**
- `me-2` (margin-end/right): Use after icons that precede text
- Icon-only buttons: Always add `aria-label`

### 6. Data Integration Patterns

**Markdown File Linking:**

```html
<!-- Standard markdown file link -->
<a href="renderer.html?file=../path/to/file.md">Link Text</a>

<!-- With icon -->
<a href="renderer.html?file=file.md" class="btn btn-primary">
    <i class="bi bi-book me-2"></i>
    Read File
</a>
```

**JavaScript Injection Points:**

Containers with specific `id` attributes that JavaScript populates:
- `id="menu-container"` - Navigation injected by menu.js
- `id="footer-container"` - Footer injected by footer.js
- `id="search-results"` - Search results (dynamically populated)
- `id="student-mode-banner"` - Student mode indicator
- `id="content"` - Main content in renderer.html

### 7. Responsive Design Patterns

**Mobile-First Approach:**

```html
<!-- Full width on mobile, specific width on larger screens -->
<div class="col-12 col-md-6 col-lg-4">
    <!-- Content -->
</div>

<!-- Hide on small screens, show on medium+ -->
<div class="d-none d-md-block">
    <!-- Desktop-only content -->
</div>

<!-- Show on small screens, hide on medium+ -->
<div class="d-md-none">
    <!-- Mobile-only content -->
</div>
```

**Common Breakpoints:**
- `col-*`: Extra small (mobile)
- `col-sm-*`: Small (≥576px)
- `col-md-*`: Medium (≥768px) - Most common in this project
- `col-lg-*`: Large (≥992px)
- `col-xl-*`: Extra large (≥1200px)

### 8. Common Content Structures

**Setup/Information Banner:**

```html
<div class="setup-banner">
    <div class="setup-banner-content">
        <div class="setup-banner-icon">
            <i class="bi bi-github"></i>
        </div>
        <div class="setup-banner-text">
            <h3>Action Title</h3>
            <p>Description text explaining the action.</p>
        </div>
        <div class="setup-banner-action">
            <a href="renderer.html?file=file.md" class="btn btn-setup">
                <i class="bi bi-icon me-2"></i>
                Button Text
            </a>
        </div>
    </div>
</div>
```

**File Listing Grid:**

```html
<div class="cards-grid">
    <div class="card-group">
        <strong>Group Title:</strong><br>
        <a href="renderer.html?file=file1.md">File 1</a><br>
        <a href="renderer.html?file=file2.md">File 2</a>
    </div>
    <div class="card-group">
        <strong>Another Group:</strong><br>
        <a href="renderer.html?file=file3.md">File 3</a><br>
    </div>
</div>
```

### 9. Search Results UI Pattern

```html
<div id="search-results" class="container mt-3 search-results-hidden">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title mb-0">
                <i class="bi bi-search me-2"></i>Search Results
            </h5>
        </div>
        <div class="card-body" id="search-results-content">
            <!-- Results populated by search.js -->
        </div>
    </div>
</div>
```

## Quality Assurance Checklist

Before submitting HTML, verify:

**Structural Standards:**
- [ ] Valid HTML5 syntax (no unclosed tags)
- [ ] Proper DOCTYPE declaration
- [ ] All links are relative paths compatible with GitHub Pages and local dev
- [ ] No hardcoded file paths (use `renderer.html?file=path`)

**Semantic HTML:**
- [ ] Heading hierarchy is logical and complete
- [ ] All interactive elements use proper semantic tags
- [ ] `<main>` wraps primary content
- [ ] Navigation uses `<nav>` or nav role

**Bootstrap Compliance:**
- [ ] Bootstrap CSS linked correctly (v5.3.2)
- [ ] Bootstrap Icons linked (v1.11.1)
- [ ] Grid uses 12-column system correctly
- [ ] Utility classes follow Bootstrap conventions
- [ ] No custom Bootstrap overrides without CSS comments explaining why

**Accessibility:**
- [ ] All images have alt text (if used)
- [ ] Form inputs have associated labels
- [ ] Icon-only buttons have aria-labels
- [ ] Color is not the only indicator of meaning
- [ ] Contrast ratio meets WCAG AA standards

**Performance:**
- [ ] CSS linked in `<head>`
- [ ] JavaScript loaded at end of `<body>` or with `defer`
- [ ] No inline styles (use CSS classes)
- [ ] No unused CSS files linked
- [ ] File sizes reasonable (minimize inline code)

**Responsive Design:**
- [ ] Desktop layout verified
- [ ] Tablet layout verified (768px breakpoint)
- [ ] Mobile layout verified (360-480px)
- [ ] No horizontal scrolling on mobile
- [ ] Touch targets are at least 44px

**Mode Support:**
- [ ] Admin-only content marked with `.admin-only` class
- [ ] Student-visible content works without admin features
- [ ] Mode toggle doesn't break page layout
- [ ] Content gracefully handles hidden elements

**Cross-browser & Device Testing:**
- [ ] Links work in static file mode (file://) and GitHub Pages
- [ ] Markdown rendering works (marked.js compatible)
- [ ] Navigation/footer injection works
- [ ] Relative paths work from all subdirectories

## Common Patterns Found in Project

### Path Resolution in menu.js

The project intelligently resolves paths based on current location:

```javascript
let basePath = '';
if (currentPath.includes('/ai-security-course/')) {
    basePath = '/ai-security-course/5_Symbols/';  // GitHub Pages
} else if (currentPath.includes('/5_Symbols/')) {
    basePath = './';  // Root of 5_Symbols
} else {
    basePath = '5_Symbols/';  // Project root
}
```

**Implication for HTML:** Use relative paths that work with this system:
- From 5_Symbols/: `renderer.html?file=../file.md`
- From 5_Symbols/Lessons/: `../../index.html`
- From root: `5_Symbols/index.html`

### File Organization Convention

```
5_Symbols/
├── index.html              # Main landing page
├── renderer.html           # Generic markdown viewer
├── Lessons/Lesson 1/       # Lesson-specific pages
├── Apply/                  # Interactive learning pages
└── Agents/                 # Agent descriptions (like this file)
```

## Workflow for HTML Writing

When creating or modifying HTML:

1. **Identify the page type** - Landing page, markdown renderer, lesson page, interactive content
2. **Check existing patterns** - Look for similar pages in the codebase
3. **Use the boilerplate** - Start with the HTML5 boilerplate above
4. **Apply Bootstrap** - Use the grid and components appropriately
5. **Link content** - Use `renderer.html?file=path.md` for markdown files
6. **Test paths** - Verify links work from the intended directory
7. **Verify accessibility** - Run through semantic HTML checklist
8. **Check responsiveness** - Test on mobile/tablet/desktop
9. **Review with team** - Ensure patterns match project standards
10. **Commit changes** - Document what HTML patterns were created/modified

## Important Constraints

**Never:**
- Use inline styles (`style="..."`) - Use CSS classes
- Create non-semantic divs for layout without good reason
- Hardcode full file paths (use relative paths)
- Import Bootstrap from CDN without version pinning
- Add new dependencies without team discussion
- Skip the DOCTYPE or html/head/body structure

**Always:**
- Use Bootstrap utility classes for spacing/alignment
- Include proper metadata in page titles
- Support both admin and student modes
- Test path resolution from multiple locations
- Include meaningful alt text for meaningful images
- Use Bootstrap Icons from the project library

**File Naming:**
- Use descriptive, lowercase names
- Use hyphens for multi-word filenames (kebab-case)
- Match naming conventions in existing code
- Example: `Agent_HtmlWriting.md`, `student-welcome.md`

---

## Version & Last Updated

- **Created:** 2025
- **Bootstrap Version:** 5.3.2
- **Bootstrap Icons Version:** 1.11.1
- **marked.js:** Latest from CDN

---