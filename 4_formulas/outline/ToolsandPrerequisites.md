# Tools and Prerequisites

## Required Tools

### Primary Tools

#### 1. Adversarial Robustness Toolbox (ART)
- **Purpose:** To craft, execute, and evaluate adversarial attacks (e.g., evasion, poisoning) and implement defense mechanisms like adversarial training
- **Cost:** Free (Open-Source)
- **Link:** [https://github.com/Trusted-AI/adversarial-robustness-toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
- **Why:** Actively maintained and widely used for AI security research and development

#### 2. TensorFlow or PyTorch
- **Purpose:** To build, train, and modify the core machine learning models that will be the subject of security analysis and defense implementation
- **Cost:** Free (Open-Source)
- **Links:** 
  - TensorFlow: [https://www.tensorflow.org/](https://www.tensorflow.org/)
  - PyTorch: [https://pytorch.org/](https://pytorch.org/)
- **Why:** Industry-standard deep learning frameworks, essential for any modern AI development

#### 3. Jupyter Notebook / Google Colab
- **Purpose:** To provide an interactive environment for learners to write code, run experiments, and document their findings when attacking and defending models
- **Cost:** Free
- **Links:**
  - Jupyter: [https://jupyter.org/](https://jupyter.org/)
  - Google Colab: [https://colab.research.google.com/](https://colab.research.google.com/)
- **Why:** The standard platform for interactive data science and machine learning projects

## Technical Prerequisites

### Required Skills

1. **Python Programming**
   - Proficiency in Python syntax and data structures
   - Experience with NumPy and data manipulation
   - Familiarity with object-oriented programming concepts

2. **Machine Learning Framework Knowledge**
   - Experience with TensorFlow OR PyTorch
   - Understanding of model training workflows
   - Ability to load, modify, and evaluate models

3. **Foundational ML Knowledge**
   - Understanding of neural network architectures
   - Knowledge of training, validation, and testing processes
   - Familiarity with common ML metrics (accuracy, loss, etc.)
   - Basic understanding of image classification or similar ML tasks

### Recommended Background

- Experience building and training at least one end-to-end ML model
- Basic understanding of computer vision or NLP tasks
- Familiarity with data preprocessing and augmentation techniques
- Understanding of overfitting, underfitting, and generalization

## Development Environment Setup

### Option 1: Local Setup

```bash
# Install Python 3.8 or higher
# Install required packages
pip install tensorflow  # or pytorch
pip install adversarial-robustness-toolbox
pip install jupyter
pip install numpy pandas matplotlib
```

### Option 2: Cloud Setup (Recommended for Beginners)

Use Google Colab - no installation required:
1. Navigate to [colab.research.google.com](https://colab.research.google.com/)
2. Create a new notebook
3. Install packages in the first cell:
```python
!pip install adversarial-robustness-toolbox
```

## Verification Checklist

Before starting the course, ensure you can:

- [ ] Write and execute Python code
- [ ] Load a pre-trained model using TensorFlow or PyTorch
- [ ] Run a Jupyter notebook or Google Colab session
- [ ] Install Python packages using pip
- [ ] Understand basic ML concepts (training, testing, accuracy)
- [ ] Work with image data or tensors

## Additional Resources

- **Python Refresher:** [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **TensorFlow Basics:** [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- **PyTorch Basics:** [PyTorch Tutorials](https://pytorch.org/tutorials/)
- **Jupyter Guide:** [Jupyter Documentation](https://jupyter-notebook.readthedocs.io/)