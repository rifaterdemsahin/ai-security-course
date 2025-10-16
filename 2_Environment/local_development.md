# Local Development Environment

This document outlines the setup for working on the AI Security Course content on your local machine. The course content, including the hands-on labs, will require a specific set of tools.

## Prerequisites

To work on this course locally, you will need:

*   **A Text Editor:** A modern text editor like VS Code is recommended for editing markdown and Python files.
*   **Git:** You need Git installed to manage versions and collaborate.
*   **Python:** The hands-on labs and projects are based on Python. You should have Python 3.x installed.
*   **Jupyter Notebook or JupyterLab:** The labs are designed to be run in Jupyter notebooks.
*   **Machine Learning Libraries:** You will need to install the following Python libraries:
    *   TensorFlow or PyTorch
    *   Adversarial Robustness Toolbox (ART)

You can install these using pip:
```bash
pip install tensorflow art-experimental
# or
pip install torch torchvision art-experimental
pip install jupyter
```

## Working on the Course

1.  **Clone the repository:** If you haven't already, clone the project to your local machine.
2.  **Navigate to the project directory:** `cd ai-security-course`
3.  **Set up your Python environment:** It is recommended to use a virtual environment to manage your dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    *(Note: We will create a `requirements.txt` file later)*
4.  **Launch Jupyter:**
    ```bash
    jupyter notebook
    ```
5.  **Create or edit content:** The main content for the course is in the `5_Symbols` directory. The hands-on labs will be located in subdirectories within `5_Symbols`.

## Alternative: Google Colab

For a simpler setup without local installation, you can use Google Colab for the hands-on labs. This is a free Jupyter notebook environment that runs in the cloud and has most of the required libraries pre-installed. You will be able to open the notebooks from the repository directly in Colab.
