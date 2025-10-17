# Lesson 1: The Attacker's Playbook - Sample Code Demonstrations

This folder contains practical demonstrations of the AI security concepts covered in Lesson 1. These scripts help students understand vulnerabilities through hands-on examples.

## 🎯 Learning Objectives

By running these demonstrations, you will:
- Experience how adversarial attacks work in practice
- Understand the stealth nature of data poisoning
- See how model extraction attacks steal intellectual property
- Learn to systematically assess AI security vulnerabilities

## 📁 Files Overview

### Core Demonstrations

1. **`evasion_attack_demo.py`** - Adversarial Examples
   - Demonstrates the "accuracy paradox"
   - Shows how small perturbations fool ML models
   - Implements FGSM (Fast Gradient Sign Method) attacks
   - Compares clean vs. adversarial robustness

2. **`data_poisoning_demo.py`** - Sleeper Agent Attacks
   - Shows how backdoors are embedded during training
   - Demonstrates stealth of poisoning attacks
   - Visualizes trigger patterns and their effects
   - Explains training-time vs. test-time attacks

3. **`model_extraction_demo.py`** - The Invisible Theft
   - Demonstrates API-based model stealing
   - Shows different extraction strategies
   - Includes query pattern analysis for detection
   - Visualizes extraction success metrics

4. **`vulnerability_assessment_tool.py`** - Security Assessment Framework
   - Comprehensive vulnerability assessment tool
   - Systematic evaluation of AI security risks
   - Risk prioritization and mitigation strategies
   - Professional security report generation

### Supporting Files

- **`requirements.txt`** - Python dependencies
- **`README.md`** - This documentation
- **Generated outputs** - Visualizations and reports created by running the demos

## 🚀 Getting Started

### Prerequisites

1. Python 3.7 or higher
2. Basic understanding of machine learning concepts
3. Familiarity with command line operations

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install individually:
   ```bash
   pip install numpy matplotlib tensorflow scikit-learn pandas seaborn
   ```

2. **Verify installation:**
   ```bash
   python -c "import numpy, matplotlib, tensorflow, sklearn; print('All dependencies installed!')"
   ```

### Running the Demonstrations

#### 1. Evasion Attack Demo
```bash
python evasion_attack_demo.py
```
**What it does:**
- Trains a simple MNIST digit classifier
- Generates adversarial examples using FGSM
- Shows how accuracy drops under attack
- Creates visualizations of attacked images

**Expected output:**
- Training progress and accuracy metrics
- Attack success rates for different perturbation levels
- Visualization saved as `evasion_attack_sample_*.png`
- Demonstration of the accuracy paradox

#### 2. Data Poisoning Demo
```bash
python data_poisoning_demo.py
```
**What it does:**
- Creates clean and poisoned training datasets
- Trains models on both datasets
- Tests backdoor activation with trigger patterns
- Analyzes attack stealth

**Expected output:**
- Model training metrics comparison
- Backdoor activation test results
- Visualization saved as `data_poisoning_visualization.png`
- Stealth analysis showing normal-appearing metrics

#### 3. Model Extraction Demo
```bash
python model_extraction_demo.py
```
**What it does:**
- Creates a proprietary target model
- Performs systematic query-based extraction
- Evaluates extraction success
- Analyzes query patterns for detection

**Expected output:**
- Target model creation and protection setup
- Query generation and extraction progress
- Success metrics (correlation, MSE, MAE)
- Visualization saved as `model_extraction_results.png`
- Defense recommendations

#### 4. Vulnerability Assessment Tool
```bash
python vulnerability_assessment_tool.py
```
**What it does:**
- Performs comprehensive security assessment
- Identifies vulnerabilities across attack categories
- Generates risk summaries and detailed reports
- Exports results to JSON format

**Expected output:**
- Systematic vulnerability identification
- Risk level categorization and scoring
- Prioritized mitigation recommendations
- JSON report saved as `vulnerability_assessment_*.json`

## 🎓 Educational Value

### Key Concepts Demonstrated

1. **The Accuracy Paradox**
   - High test accuracy ≠ Security
   - Need for adversarial robustness testing
   - Importance of security-aware evaluation

2. **Stealth of Attacks**
   - Poisoning attacks remain hidden
   - Normal-appearing performance metrics
   - Need for specialized detection methods

3. **Attack Sophistication**
   - Simple attacks can be highly effective
   - Black-box access is often sufficient
   - Systematic approaches amplify impact

4. **Defense Complexity**
   - Multiple attack vectors require diverse defenses
   - Trade-offs between security and performance
   - Need for comprehensive security frameworks

### Learning Progression

1. **Start with Evasion Attacks** - Most intuitive introduction
2. **Move to Data Poisoning** - Understand training-time threats
3. **Explore Model Extraction** - See intellectual property risks
4. **Use Assessment Tool** - Learn systematic security evaluation

## 🛡️ Security Insights

### Critical Takeaways

1. **AI systems have unique vulnerabilities** not found in traditional software
2. **Standard testing is insufficient** for security evaluation
3. **Attackers can be highly sophisticated** with minimal access requirements
4. **Security must be designed in** from the beginning
5. **Comprehensive assessment is essential** for robust AI systems

### Real-World Implications

- **Autonomous vehicles** vulnerable to adversarial traffic signs
- **Medical AI** susceptible to backdoor attacks
- **Financial ML** at risk from model extraction
- **Facial recognition** vulnerable to evasion attacks

## 🔧 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed
   - Check Python version compatibility
   - Some demos have fallback implementations

2. **Memory Issues**
   - Reduce dataset sizes in demos
   - Use smaller models for training
   - Close other applications

3. **Training Time**
   - Demos use small datasets for speed
   - Real attacks may require more computation
   - Consider using pre-trained models

4. **Visualization Problems**
   - Ensure matplotlib backend is configured
   - Check file permissions for saving plots
   - Use `plt.show()` if running interactively

### Getting Help

- Review the code comments for detailed explanations
- Check the lesson materials for theoretical background
- Experiment with different parameters to see their effects
- Join course discussion forums for peer support

## 📚 Further Learning

### Recommended Reading

1. **Adversarial Machine Learning** - research papers and tutorials
2. **AI Security Guidelines** - OWASP AI Security Project
3. **Threat Modeling for AI** - systematic security analysis
4. **Defensive Techniques** - adversarial training, differential privacy

### Advanced Exercises

1. **Implement additional attack methods** (PGD, C&W, etc.)
2. **Experiment with defense techniques** 
3. **Assess real-world AI systems** using the vulnerability tool
4. **Create custom attack scenarios** for your domain

---

## ⚠️ Ethical Use Warning

These demonstrations are for **educational purposes only**. Use this knowledge to:
- ✅ Improve AI system security
- ✅ Conduct authorized security assessments
- ✅ Research defensive techniques
- ✅ Educate others about AI security

**Do NOT use this knowledge to:**
- ❌ Attack systems without authorization
- ❌ Cause harm or damage
- ❌ Violate terms of service
- ❌ Engage in illegal activities

Remember: **With great power comes great responsibility!**