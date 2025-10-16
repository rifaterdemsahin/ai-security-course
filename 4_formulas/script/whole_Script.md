# AI Security Course - Script

This document contains the script components for the "Secure AI: Interpret and Protect Models" course.

---

## Module 1: The Attacker's Playbook: Understanding AI Vulnerabilities

### **The Trojan Horse in the Code**

**Format:** Interactive Discussion

**Content:**
Learners step into the role of a lead Machine Learning Engineer whose AI-powered malware detector has failed to detect a novel ransomware variant, resulting in a client breach. In this dialog with the coach, they will diagnose this critical failure by investigating the incident. Learners will be prompted to analyze the potential causes for the failure, exploring AI security concepts such as evasion attacks, data poisoning, and model extraction techniques. The objective is to have learners analyze AI security vulnerabilities within a realistic incident response scenario.

**Screen Captures:**
- [Placeholder for interactive discussion interface]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Welcome to Advanced AI Security: Interpret & Defend**

**Format:** Talking Head

**Content:**
Overview of course objectives, instructor introduction, real-world importance of AI model security, and what learners will achieve. This video introduces learners to AI models as critical digital assets with distinct vulnerabilities. It explains how attackers can target model logic and data, preparing learners to understand and implement defenses against advanced AI threats.

**Screen Captures:**
- [Placeholder for title card]
- [Placeholder for instructor shot]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Evasion Attacks: Fooling the Model's Senses**

**Format:** Talking Head + Demonstration

**Content:**
Discover the critical difference between an AI with "book smarts" and one with "street smarts." This video reveals why a model that gets a 99% accuracy score can still be dangerously insecure. We break down why standard tests don't prepare a model for a real-world adversary, giving you the foundational mindset needed to build truly robust and trustworthy AI.

**Screen Captures:**
- [Placeholder for diagram comparing accuracy and robustness]
- [Placeholder for demonstration of an evasion attack]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Data Poisoning: Corrupting Intelligence from Within**

**Format:** Talking Head + Demonstration

**Content:**
Learn how an AI model can be turned into a "sleeper agent" without anyone knowing. This video demonstrates how attackers can implant hidden backdoors by injecting malicious examples directly into the training data. You'll see how a model can appear to function perfectly, only to be activated by a specific input to perform a malicious action. Understanding this sneaky threat is crucial for building AI you can truly trust.

**Screen Captures:**
- [Placeholder for diagram showing data poisoning]
- [Placeholder for demonstration of a backdoor attack]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Model Stealing and Extraction: The Digital Heist**

**Format:** Talking Head + Demonstration

**Content:**
Learn about the digital heist that bypasses all your traditional firewalls. This video exposes how attackers can steal the 'secret sauce' of your AI without ever touching your code. We demonstrate how carefully crafted queries can allow an adversary to clone your model's functionality, effectively stealing your hard work. Understanding this threat is the first step to protecting your most valuable digital assets.

**Screen Captures:**
- [Placeholder for diagram showing model extraction]
- [Placeholder for demonstration of a model stealing attack]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Evading an AI Security Camera**

**Format:** Practice Assignment

**Content:**
**Scenario:** You are a security analyst on a "Red Team" for a technology firm called SynthSafe. Your company has just developed a new, state-of-the-art AI-powered security system. Its core component is a computer vision model designed to identify authorized personnel from security camera footage. The model has been trained on thousands of employee photos and boasts a 99.8% accuracy rate on its test dataset. Your team has been tasked with testing the system's resilience against adversarial attacks before it's deployed. Your supervisor suspects that despite its high accuracy, the model can be fooled. Intelligence suggests that a specific, seemingly random pattern, when printed on a sticker and worn by an individual, can act as an "invisibility cloak," causing the AI model to misclassify authorized personnel as "unauthorized." Your mission is to verify this vulnerability. You will be given access to the AI model and a digital version of this "adversarial patch." You must use it to trick the model and document your findings. This hands-on activity directly allows the learner to experience how a highly accurate model can be critically flawed, bringing the lessons from the introductory videos to life.

**Screen Captures:**
- [Placeholder for Jupyter Notebook/Google Colab interface]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Attacking Machine Learning with Adversarial Examples**

**Format:** Reading

**Content:**
This reading shows you that what you see is not what an AI sees. We explore the critical vulnerability of adversarial examples: inputs that are deliberately crafted to look harmless to you but are designed to break a model's logic. Understanding this core concept is the essential first step to building systems that can defend against these subtle and powerful attacks.

**Screen Captures:**
- [N/A for reading material]

**Transitions:**
- [Placeholder for transition to next module]

---

## Module 2: Building the Shield: Proactive Defense Strategies

### **The Pre-Mortem: Fortifying a New AI System**

**Format:** Interactive Discussion

**Content:**
Learners step into the role of lead AI Security Architect for an autonomous vehicle company, tasked with a critical pre-launch "pre-mortem" for a new perception model. In this dialog with the coach, they will evaluate and propose a primary security architecture to defend the model against future attacks. As the dialog progresses, the learners will analyze the trade-offs of their proposed defensive strategy and will be prompted to explore complementary concepts such as model hardening, adversarial training, and differential privacy. They will be required to balance practical considerations like data privacy and model accuracy to form a holistic, defense-in-depth strategy. The objective is for learners to evaluate and prioritize proactive AI security strategies, balancing their respective trade-offs in a pre-deployment safety assessment.

**Screen Captures:**
- [Placeholder for interactive discussion interface]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Adversarial Training: Turning Attacks into Model Strength**

**Format:** Talking Head + Demonstration

**Content:**
We reveal how to turn an AI's greatest weakness into its greatest strength. This video breaks down the process of adversarial training, showing how using carefully crafted attacks to teach a model doesn't just patch a vulnerability but fundamentally fortifies its decision-making process for long-term resilience.

**Screen Captures:**
- [Placeholder for diagram showing adversarial training workflow]
- [Placeholder for demonstration of adversarial training]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Input Sanitization: Your First Line of Defense**

**Format:** Talking Head + Demonstration

**Content:**
Learn how to dramatically boost your model's security with surprisingly simple methods. We demonstrate how basic pre-processing and input checks can stop sophisticated attacks dead in their tracks, providing an immediate and powerful layer of protection without requiring complex changes to your model's architecture.

**Screen Captures:**
- [Placeholder for diagram showing input sanitization pipeline]
- [Placeholder for demonstration of input sanitization]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Differential Privacy: Protecting Data, Preserving Insight**

**Format:** Talking Head + Demonstration

**Content:**
Discover how to achieve powerful insights and strong privacy at the same time. This video breaks down the surprisingly simple principle of differential privacy, showing how adding controlled randomness to your data builds a privacy shield directly into your model. This allows you to confidently use datasets while guaranteeing the anonymity of the people within them.

**Screen Captures:**
- [Placeholder for diagram explaining differential privacy]
- [Placeholder for demonstration of differential privacy]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Building a Resilient AI with Adversarial Training**

**Format:** Practice Assignment

**Content:**
**Scenario:** Welcome to the SynthSafe "Blue Team." Your work as a Red Team analyst in the previous module was a huge success—perhaps too successful. You clearly demonstrated that the SynthSafe_Security_Model (v1) could be easily fooled by a simple adversarial patch. Management was impressed by the finding but is now demanding a solution. Your new mission is to move from breaking the system to fixing it. You are tasked with developing a new, more robust version of the security model (v2). Your strategy is to use adversarial training. By showing the model examples of the very attacks that fooled its predecessor, you will teach it to recognize and correctly classify personnel, even when they are wearing the adversarial patch. Your objective is to train a new model that is resilient to the previously successful evasion attack and to prove its improved performance.

**Screen Captures:**
- [Placeholder for Jupyter Notebook/Google Colab interface]

**Transitions:**
- [Placeholder for transition to next module]

---

## Module 3: The AI Security Lifecycle: Testing and Validation

### **The Security Audit Challenge**

**Format:** Interactive Discussion

**Content:**
Learners step into the role of Chief Information Security Officer (CISO) for a major technology firm. A critical AI system is scheduled for deployment in 48 hours, but there are concerns about its security posture. In this dialog with the coach, they will design and execute a comprehensive security audit plan. Learners will be prompted to develop a systematic approach to testing the model against various attack vectors, establishing acceptance criteria for security metrics, and making a final deployment recommendation. The objective is for learners to synthesize their knowledge of attacks and defenses into a comprehensive security validation methodology.

**Screen Captures:**
- [Placeholder for interactive discussion interface]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Red Team Methodology: Thinking Like an Attacker**

**Format:** Talking Head + Demonstration

**Content:**
Learn how to systematically probe an AI system for weaknesses by adopting an attacker's mindset. This video reveals the structured approach that professional red teams use to discover vulnerabilities, from initial reconnaissance to exploitation and reporting. You'll understand how to design comprehensive attack scenarios that test your defenses under realistic conditions.

**Screen Captures:**
- [Placeholder for diagram of red team methodology]
- [Placeholder for demonstration of a red team exercise]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Security Metrics and Validation**

**Format:** Talking Head + Demonstration

**Content:**
Discover how to measure and quantify AI security. This video explains key security metrics, how to establish acceptance criteria, and how to interpret test results to make informed decisions about model deployment. You'll learn to balance security requirements with performance needs and communicate risk effectively to stakeholders.

**Screen Captures:**
- [Placeholder for dashboard showing security metrics]
- [Placeholder for demonstration of security validation]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **The Complete Security Lifecycle**

**Format:** Talking Head + Demonstration

**Content:**
See how security testing fits into the broader AI development lifecycle. This video demonstrates how to integrate security validation into your MLOps pipeline, establish continuous monitoring, and maintain security posture over time. You'll understand that security is not a one-time activity but an ongoing commitment.

**Screen Captures:**
- [Placeholder for diagram of the AI security lifecycle]
- [Placeholder for demonstration of a secure MLOps pipeline]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Red Team Security Audit**

**Format:** Practice Assignment

**Content:**
**Scenario:** You are the Lead Security Analyst for a critical AI deployment. Before the system goes live, you must conduct a comprehensive red team audit to validate its security posture. Your mission is to systematically test the model against multiple attack vectors and provide quantitative evidence of its resilience. You will test for: 1) Evasion attack resilience using advanced PGD attacks, 2) Data poisoning backdoors using trigger detection, and 3) Model extraction vulnerabilities using query-based attacks. Your findings will determine whether the system is ready for production deployment. This lab simulates a real-world security audit, requiring learners to apply systematic testing methodology, interpret results to find specific weaknesses, and quantify the model's security posture.

**Screen Captures:**
- [Placeholder for Jupyter Notebook/Google Colab interface]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Microsoft's AI Red Team is Building a Safer Future for AI**

**Format:** Reading

**Content:**
This reading shows how to test your AI defenses by acting like an ethical hacker. It explains red-teaming methods, adversarial thinking, and practical techniques to uncover blind spots so you can fix them before attackers do.

**Screen Captures:**
- [N/A for reading material]

**Transitions:**
- [Placeholder for transition to next learning item]

---

### **Course Wrap Up**

**Format:** Talking Head

**Content:**
Wrap-up of the course content with transition to the next course.

**Screen Captures:**
- [Placeholder for end card]

**Transitions:**
- [End of course]