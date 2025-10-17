# GitHub Pages Environment

This document explains how the AI Security Course project is deployed to GitHub Pages.

## 1. GitHub Pages

[GitHub Pages](https://pages.github.com/) is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website.

This project is deployed to GitHub Pages for easy access and sharing.

## 2. Deployment Workflow

The deployment process is automated using GitHub Actions.

- **Workflow File:** `.github/workflows/static.yml`

### 2.1. Workflow Trigger

The deployment workflow is triggered automatically on every `push` to the `main` branch. It can also be triggered manually from the "Actions" tab in the GitHub repository.

### 2.2. Workflow Steps

The workflow consists of a single job, `deploy`, which performs the following steps:

1.  **Checkout:** The repository's code is checked out.
2.  **Setup Pages:** The GitHub Pages environment is configured.
3.  **Upload Artifact:** The entire repository is uploaded as a GitHub Pages artifact.
4.  **Deploy to GitHub Pages:** The artifact is deployed to GitHub Pages.

## 3. Deployed Site URL

The project is accessible at the following URL:

[https://rifaterdemsahin.github.io/ai-security-course/5_Symbols/index.html](https://rifaterdemsahin.github.io/ai-security-course/5_Symbols/index.html)
