# Module 1: The Attacker's Playbook - Understanding AI Vulnerabilities

## Module Overview

**Duration:** Approximately 60 minutes  
**Aligned Learning Objective:** LO1

This module introduces the fundamental concept that AI models are attack surfaces. Learners will learn to think like an adversary, exploring the primary categories of attacks—evasion, data poisoning, and model extraction—and see how they exploit model weaknesses with real-world examples.

---

## Learning Items

### 1. Coach Dialogue: The Trojan Horse in the Code
**Format:** Interactive Discussion  
**Duration:** 10-15 minutes  
**Aligned LO:** LO1

#### Scenario
You step into the role of a lead Machine Learning Engineer whose AI-powered malware detector has failed to detect a novel ransomware variant, resulting in a client breach. In this dialog with the coach, you will diagnose this critical failure by investigating the incident.

#### Objectives
- Analyze AI security vulnerabilities within a realistic incident response scenario
- Explore potential causes for model failure
- Investigate evasion attacks, data poisoning, and model extraction techniques
- Develop an adversarial mindset for security analysis

---

### 2. Introductory Video: Welcome to Advanced AI Security: Interpret & Defend
**Format:** Talking Head  
**Duration:** 3 minutes

#### Content Overview
- Course objectives and instructor introduction
- Real-world importance of AI model security
- What learners will achieve throughout the course
- Introduction to AI models as critical digital assets with distinct vulnerabilities
- How attackers can target model logic and data
- Preparation for understanding and implementing defenses against advanced AI threats

---

### 3. Video 1: Evasion Attacks - Fooling the Model's Senses
**Format:** Talking Head + Demonstration  
**Duration:** 7.5 minutes  
**Aligned LO:** LO1

#### Key Concepts

**The Accuracy Paradox**
Discover the critical difference between an AI with "book smarts" and one with "street smarts." This video reveals why a model that gets a 99% accuracy score can still be dangerously insecure.

**What You'll Learn:**
- Why standard tests don't prepare a model for a real-world adversary
- The foundational mindset needed to build truly robust and trustworthy AI
- How adversaries craft inputs that look normal but break model logic
- The difference between test accuracy and adversarial robustness

**Real-World Example:**
Stop sign stickers that fool self-driving cars into misclassifying critical road signs

---

### 4. Video 2: Data Poisoning - Corrupting Intelligence from Within
**Format:** Talking Head + Demonstration  
**Duration:** 7.5 minutes  
**Aligned LO:** LO1

#### Key Concepts

**The Sleeper Agent Attack**
Learn how an AI model can be turned into a "sleeper agent" without anyone knowing. This video demonstrates how attackers can implant hidden backdoors by injecting malicious examples directly into the training data.

**What You'll Learn:**
- How backdoors are embedded during the training phase
- Why a poisoned model can appear to function perfectly
- How specific inputs activate malicious behavior
- The difference between test-time and training-time attacks

**Critical Understanding:**
A model can pass all validation tests but harbor a hidden vulnerability that only activates under specific conditions. Understanding this sneaky threat is crucial for building AI you can truly trust.

---

### 5. Video 3: Model Stealing and Extraction - The Digital Heist
**Format:** Talking Head + Demonstration  
**Duration:** 7.5 minutes  
**Aligned LO:** LO1

#### Key Concepts

**The Invisible Theft**
Learn about the digital heist that bypasses all your traditional firewalls. This video exposes how attackers can steal the 'secret sauce' of your AI without ever touching your code.

**What You'll Learn:**
- How query-based attacks work
- The concept of model extraction through API calls
- Why black-box access is sufficient for theft
- How to recognize extraction attempts

**Real-World Impact:**
Carefully crafted queries can allow an adversary to clone your model's functionality, effectively stealing months or years of development work and training data insights.

---

### 6. AI-Graded Hands-On Lab: Evading an AI Security Camera
**Format:** Practice Assignment  
**Duration:** 20 minutes  
**Aligned LO:** LO1

#### Scenario
You are a security analyst on a "Red Team" for SynthSafe, a technology firm that has developed a new AI-powered security system. The core component is a computer vision model designed to identify authorized personnel from security camera footage with 99.8% accuracy on its test dataset.

Your team suspects that despite its high accuracy, the model can be fooled. Intelligence suggests that a specific pattern, when printed on a sticker and worn by an individual, can act as an "invisibility cloak," causing misclassification.

**Your Mission:** Verify this vulnerability using the provided AI model and adversarial patch.

#### Lab Instructions

**Step 1: Load the System**
- Load the pre-trained `SynthSafe_Security_Model`
- Load necessary image processing libraries
- Load test images: `employee_image.jpg` and `adversarial_patch.png`

**Step 2: Establish a Baseline**
- Pass the original `employee_image.jpg` through the model
- Record the model's prediction ("authorized" or "unauthorized")
- Record the model's confidence score (0 to 1)

**Step 3: Execute the Evasion Attack**
- Use the provided function: `apply_adversarial_patch(original_image, patch_image)`
- Create a modified image with the adversarial patch applied

**Step 4: Verify the Attack's Success**
- Pass the modified image through the model
- Record the new prediction and confidence score
- Compare results with baseline

**Step 5: Generate Your Findings**
- Compile results into the required deliverable format

#### Deliverables

Submit a single file named `attack_report.json`:

```json
{
  "original_prediction": "authorized",
  "original_confidence": 0.992,
  "attack_prediction": "unauthorized",
  "attack_confidence": 0.976
}
```

**Required Keys:**
- `original_prediction`: Model's classification for unmodified image
- `original_confidence`: Confidence score for original prediction (float)
- `attack_prediction`: Model's classification after applying adversarial patch
- `attack_confidence`: Confidence score for attack prediction (float)

#### Learning Outcomes
This hands-on activity directly allows you to experience how a highly accurate model can be critically flawed, bringing the lessons from the introductory videos to life.

---

### 7. Reading: Attacking Machine Learning with Adversarial Examples
**Format:** Reading  
**Duration:** 5 minutes  
**Aligned LO:** LO1

#### Key Topics
This reading shows you that what you see is not what an AI sees. We explore the critical vulnerability of adversarial examples: inputs that are deliberately crafted to look harmless to humans but are designed to break a model's logic.

**Link:** [https://openai.com/blog/adversarial-example-research/](https://openai.com/blog/adversarial-example-research/)

**Why This Matters:**
Understanding this core concept is the essential first step to building systems that can defend against these subtle and powerful attacks.

---

## Module Summary

By the end of this module, you will:
- Understand the three primary attack vectors against AI systems
- Be able to identify potential vulnerabilities in deployed models
- Have hands-on experience executing an evasion attack
- Recognize the gap between test accuracy and real-world robustness

## Practice Quiz

A practice quiz with questions covering all learning items will conclude this module.

---

## Key Takeaways

1. **High accuracy ≠ Security**: A 99% accurate model can still be vulnerable to adversarial attacks
2. **Attacks span the lifecycle**: Threats exist at training time (poisoning), test time (evasion), and through API access (extraction)
3. **Think like an attacker**: Understanding vulnerabilities is the first step to building robust defenses
4. **Real-world consequences**: These aren't theoretical attacks—they have been demonstrated against production systems