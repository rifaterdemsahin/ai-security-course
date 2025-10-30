---
description: Repository Information Overview
alwaysApply: true
---

# AI Security Course Information

## Summary
This is an educational repository containing complete course materials for **"Secure AI: Interpret and Protect Models"** - a comprehensive course on AI security, vulnerabilities, and practical defenses. The repository combines a static website frontend built with HTML/JavaScript/CSS, Python demonstration scripts, and extensive markdown documentation. The course is deployed to GitHub Pages and focuses on teaching AI security concepts through interactive lessons and hands-on demonstrations.

## Repository Structure
- `1_real/` - Project objectives and key results (OKRs)
- `2_Environment/` - Development setup and configuration guides
- `3_UI/` - Course interface cards and security concept definitions
- `4_formulas/` - Course structure, module outlines, and script templates
- `5_Symbols/` - **Main website root** containing HTML, JavaScript, CSS, and lesson demonstrations
- `6_Semblance/` - Templates and styling components
- `7_Testing/` - Testing procedures and validation guides
- `.github/workflows/` - GitHub Actions for automated GitHub Pages deployment
- `.vscode/` - VSCode editor configuration

### Main Components
- **5_Symbols** (Frontend): The main course website with interactive interface
  - `index.html` - Main entry point for the web application
  - JavaScript files: `menu.js`, `search.js`, `footer.js`, `templateBuilder.js`, `buildStatus.js`
  - CSS styling: `style.css`, `menu.css`, `footer.css`
  - `Lessons/` - Contains three lessons with Python demonstration scripts
  - `Apply/` - Interactive learning applications
  - `Agents/` - AI agent specifications and descriptions

- **Python Demonstrations** (5_Symbols/Lessons/Lesson 1): Hands-on security demonstrations
  - `evasion_attack_demo.py` - Adversarial examples and FGSM attacks
  - `data_poisoning_demo.py` - Backdoor and poisoning attack demonstrations
  - `model_extraction_demo.py` - Model stealing and extraction techniques
  - `vulnerability_assessment_tool.py` - Comprehensive security assessment framework
  - `demo_launcher.py` - Utility to launch demonstrations

- **Documentation**: Course materials, outlines, and reference cards across multiple directories

## Technology Stack

### Frontend
**Language**: HTML5, JavaScript (ES6+), CSS3
**Framework**: Bootstrap 5.3.2 with Bootstrap Icons 1.11.1
**Features**: Dynamic content rendering, search functionality, responsive design
**Configuration**: `pageConfig.js` - Central page configuration
**Build/Serve**: Python built-in HTTP server (`python3 -m http.server 8000` from `5_Symbols/`)

### Python Demonstrations
**Language**: Python 3.7+
**Runtime**: Python interpreter
**Build System**: None (scripts run directly)
**Package Manager**: pip

### Deployment
**Platform**: GitHub Pages (static hosting)
**Workflow**: GitHub Actions (`.github/workflows/static.yml`)
**Build Process**: Automated deployment on push to main branch

## Dependencies

### Python Dependencies (5_Symbols/Lessons/Lesson 1/)
```
numpy>=1.21.0
matplotlib>=3.5.0
tensorflow>=2.8.0
scikit-learn>=1.0.0
pandas>=1.3.0
seaborn>=0.11.0
```

### Frontend Dependencies
- Bootstrap 5.3.2 (CDN)
- Bootstrap Icons 1.11.1 (CDN)
- Vanilla JavaScript (no npm dependencies)

## Build & Installation

### Frontend (Main Website)
```bash
cd 5_Symbols
python3 -m http.server 8000
# Open browser to http://localhost:8000
```

### Python Demonstrations
```bash
# Install dependencies
cd 5_Symbols/Lessons/Lesson\ 1
pip install -r requirements.txt

# Run individual demonstrations
python evasion_attack_demo.py
python data_poisoning_demo.py
python model_extraction_demo.py
python vulnerability_assessment_tool.py

# Or launch all demos
python demo_launcher.py
```

## GitHub Pages Deployment
**Workflow File**: `.github/workflows/static.yml`
**Trigger**: Automatic on push to `main` branch
**Manual Trigger**: Available via Actions tab
**Pre-deployment Script**: `5_Symbols/scripts/update_deploy_time.sh` - Updates deployment timestamp
**Live Site**: https://rifaterdemsahin.github.io/ai-security-course/

## Main Entry Points & Resources

### Website
- **Primary Entry**: `5_Symbols/index.html`
- **Configuration**: `5_Symbols/pageConfig.js`
- **Search Index**: `5_Symbols/search.json`
- **Menu System**: `5_Symbols/menu.js` (navigation logic)
- **Template Engine**: `5_Symbols/templateBuilder.js` (content rendering)

### Learning Materials
- **Course Outline**: `4_formulas/outline/_outline.md`
- **Lesson 1**: `5_Symbols/Lessons/Lesson 1/README.md` (comprehensive with demos)
- **Lesson 2-3**: `5_Symbols/Lessons/Lesson 2/` and `Lesson 3/` (structure defined)
- **Security Cards**: `3_UI/Cards/` - 40+ markdown files on security concepts
- **Memory Cards**: `5_Symbols/Apply/memory_cards.html` - Interactive flashcards

### Scripts & Automation
- **Deployment Script**: `5_Symbols/scripts/update_deploy_time.sh`
- **Demo Launcher**: `5_Symbols/Lessons/Lesson 1/demo_launcher.py`

## Testing & Quality

### Python Demonstrations
**Testing Framework**: Built-in assertions and visualization verification
**Test Files**: Python scripts include validation and output generation
**Verification**: Scripts generate PNG visualizations and JSON reports as proof of execution
**Output Examples**:
- `evasion_attack_sample_*.png` - Adversarial example visualizations
- `data_poisoning_visualization.png` - Backdoor attack results
- `model_extraction_results.png` - Extraction success metrics
- `vulnerability_assessment_*.json` - Security report

### Frontend Testing
**Manual Testing**: Browser-based verification of interactive elements
**Search Testing**: `search.json` validates content searchability
**Validation**: GitHub Actions workflow ensures deployment succeeds

## VS Code Configuration
**File**: `.vscode/settings.json` and `.vscode/launch.json`
**Purpose**: Development environment standardization for contributors

## Key Commands
```bash
# Start local development server
cd 5_Symbols && python3 -m http.server 8000

# Install Python dependencies
pip install -r 5_Symbols/Lessons/Lesson\ 1/requirements.txt

# Run Lesson 1 demonstrations
cd 5_Symbols/Lessons/Lesson\ 1 && python evasion_attack_demo.py

# View deployment logs
# (Check GitHub Actions: .github/workflows/static.yml)

# Update deployment timestamp
./5_Symbols/scripts/update_deploy_time.sh
```

## Learning Structure
- **Lesson 1**: "The Attacker's Playbook" - Understanding AI vulnerabilities (with interactive demos)
- **Lesson 2**: "Building the Shield" - Implementing defenses
- **Lesson 3**: "Adversarial Testing" - Testing and validation techniques
- **Interactive Applications**: Memory cards and hands-on exercises in `Apply/`
- **AI Agents**: Specialized agents for content generation (`Agents/`)

## Target Audience & Deployment
**Audience**: Students learning AI security concepts with hands-on demonstrations
**Deployment Target**: GitHub Pages (static hosting)
**Accessibility**: Web-based (no backend server required)
**Contribution Model**: Fork-based with pull request workflows

