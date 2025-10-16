# GitHub Environment & Workflow

This document describes how we use GitHub for the AI Security Course. GitHub is our central hub for collaboration, version control, and deployment.

## Core Concepts

*   **Repository:** The single source of truth for all course materials is the GitHub repository.
*   **Main Branch:** The `main` branch represents the latest, stable version of the course. Direct pushes to `main` are discouraged.
*   **Feature Branches:** To work on new content or make changes, you should create a new branch. This keeps the `main` branch clean and allows for review before merging.

## Workflow

1.  **Create an Issue:** For any new piece of work (e.g., a new explainer page, a bug fix), it's a good practice to create an issue first to track it.

2.  **Create a Branch:** Create a descriptive branch name for your work. For example:
    ```bash
    git checkout -b feature/add-evasion-attacks-explainer
    ```

3.  **Commit Your Changes:** Make your changes locally, and commit them with clear and concise messages.

4.  **Push to GitHub:** Push your branch to the remote repository:
    ```bash
    git push origin feature/add-evasion-attacks-explainer
    ```

5.  **Create a Pull Request:** Once you are ready for your work to be reviewed, create a Pull Request (PR) on GitHub. The PR should target the `main` branch. In the PR description, explain the changes you made.

6.  **Review and Merge:** The PR will be reviewed, and once approved, it will be merged into the `main` branch.

7.  **Deployment:** Merging to the `main` branch will trigger a deployment of the website (this is a hypothetical setup for now, as described in `2_environments/README.md`).
