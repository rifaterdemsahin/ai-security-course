# Outline Template

## Part I: Course Overview

### Course Information

| Field | Details | Character Length | Internal Notes |
|-------|---------|------------------|----------------|
| **Title** | Secure AI: Interpret and Protect Models | 39 | Key Resources |
| **Estimated Workload (Time in Minutes)** | 70 minutes | | Guidelines & Templates, Examples |
| **Difficulty Level** | Intermediate | | Onboarding Information: "Short Course Guidelines & Process Overview, Video Production Standards/Guidelines" |
| **Lead Instructor** | Rifat Erdem Sahin | | |

### Main Outcome
After completing this course, learners will be able to analyze a complex AI model for security vulnerabilities, implement robust defenses, and evaluate their effectiveness against sophisticated adversarial threats.


### Course Learning Objectives

By the end of this course, learners will be able to:

1. **LO1:** Analyze and identify a range of security vulnerabilities in complex AI models, including evasion, data poisoning, and model extraction attacks.

2. **LO2:** Apply defense mechanisms like adversarial training and differential privacy to protect AI systems from known threats.

3. **LO3:** Evaluate the effectiveness of security measures by designing and executing simulated adversarial attacks to test the resilience of defended AI model.

### Key Takeaways/Enduring Understandings

- **The most fundamental understanding** is that AI systems are not infallible black boxes; they are software with unique vulnerabilities. The learners will learn to see models through the eyes of an attacker, recognizing how they can be manipulated through evasion, data poisoning, and model extraction attacks.

- **Effective AI security is a proactive design choice**, not an afterthought. The learners will grasp how to implement and configure robust defenses like adversarial training, input sanitization, and differential privacy directly into the model's lifecycle to harden it from the ground up.

- **A defense is only as good as its ability to withstand an attack.** The learners will master the skill of adversarial testing and "Red Teaming" for AI—designing and executing simulated attacks to empirically measure your model's resilience and prove that its security measures actually work under pressure.

- **Protecting an AI system is not a one-time fix but an ongoing process.** The learners will internalize the complete security lifecycle: a continuous loop of diagnosing new threats, implementing appropriate defenses, and validating the system's strength to stay ahead of evolving adversarial tactics.

### Real World Connections

#### Examples and Case Studies:

1. **Stop Sign Attack on Self-Driving Cars**
   - Researchers have demonstrated how placing simple stickers on a stop sign can trick a self-driving car's image recognition system into misclassifying it as a speed limit sign. This highlights a classic evasion attack, where a minor, malicious input change causes a catastrophic model failure in the real world.
   - Reference: <https://www.theregister.com/2025/03/07/lowcost_malicious_attacks_on_selfdriving/>

2. **Apple's Differential Privacy Implementation**
   - Apple uses differential privacy in its iOS keyboard to gather data and improve predictive text suggestions without accessing the specific content of what users are typing. This proactive privacy-preserving technique is a core example of building security into a model's data pipeline from the start, rather than adding it later.
   - Reference: <https://machinelearning.apple.com/research/learning-with-privacy-at-scale>

3. **AI Red Teams at Major Tech Companies**
   - Major tech companies like Microsoft and Google employ AI "Red Teams" whose sole job is to attack their own systems, such as trying to fool a new facial recognition model or bypass a content moderation filter. This adversarial testing is critical for discovering vulnerabilities and validating that their defenses work against determined, human attackers before a product is released.
   - Reference: <https://www.scworld.com/perspective/an-inside-look-at-microsofts-ai-red-team>

4. **Email Spam Filter Arms Race**
   - Email spam filters are in a constant arms race with attackers who continuously devise new phrasing and tactics to bypass them. This forces developers to constantly update their models with new data and defense strategies, perfectly illustrating the ongoing cycle of threat analysis, defense implementation, and validation.
   - Reference: <https://www.techradar.com/pro/ai-arms-race-the-evolving-battle-between-email-spam-and-spam-filters>

### Recommended Background

**Course Prerequisites (150 characters max):**
Proficiency in Python and a machine learning framework (e.g., TensorFlow, PyTorch). Foundational knowledge of building and training AI models.

### Proof of Learning

Learners will demonstrate mastery through:

1. **IVQs** (Minimum 1 IVQ per video)
2. **Practice Quiz** (1 per every learning item)
3. **AI-graded HOLs** (1 per module)
4. **Course-end Project**
5. **Graded Assessment** (at least 10 questions per course)

### Tool Application Table

| Field | Details |
|-------|---------|
| **Tool Name** | Adversarial Robustness Toolbox (ART) / TensorFlow or PyTorch / Jupyter Notebook / Google Colab |
| **Purpose/Use in Course** | To craft, execute, and evaluate adversarial attacks (e.g., evasion, poisoning) and implement defense mechanisms like adversarial training. / To build, train, and modify the core machine learning models that will be the subject of security analysis and defense implementation. / To provide an interactive environment for learners to write code, run experiments, and document their findings when attacking and defending models. |
| **Free or Paid Version Usage in Course** | Free (Open-Source) |
| **If paid, is a Trial Version available and needed?** | N/A |
| **Trial Duration & Limitations** | N/A |
| **Tool Validity for Course Development** | Actively maintained and widely used for AI security research and development / Industry-standard deep learning frameworks, essential for any modern AI development. / The standard platform for interactive data science and machine learning projects. |
| **Source/Download Link** | <https://github.com/Trusted-AI/adversarial-robustness-toolbox> / <https://www.tensorflow.org/> or <https://pytorch.org/> / <https://jupyter.org/> or <https://colab.research.google.com/> |

---

## Part II: Plan Your Course

## Module 1: The Attacker's Playbook: Understanding AI Vulnerabilities

**High-level Description:** This module introduces the fundamental concept that AI models are attack surfaces. The learners will learn to think like an adversary, exploring the primary categories of attacks—evasion, data poisoning, and model extraction—and see how they exploit model weaknesses with real-world examples.

### Learning Items

| Learning Item Title | Format | Aligned LO | High-level Description | Est. Time | Notes |
|-------------------|---------|------------|----------------------|----------|--------|
| **The Trojan Horse in the Code** | Coach Dialogue | LO1 | Learners step into the role of a lead Machine Learning Engineer whose AI-powered malware detector has failed to detect a novel ransomware variant, resulting in a client breach. In this dialog with the coach, they will diagnose this critical failure by investigating the incident. Learners will be prompted to analyze the potential causes for the failure, exploring AI security concepts such as evasion attacks, data poisoning, and model extraction techniques. The objective is to have learners analyze AI security vulnerabilities within a realistic incident response scenario. | 10-15 mins | Interactive Discussion |
| **Welcome to Advanced AI Security: Interpret & Defend** | Introductory Video | - | Overview of course objectives, instructor introduction, real-world importance of AI model security, and what learners will achieve. This video introduces learners to AI models as critical digital assets with distinct vulnerabilities. It explains how attackers can target model logic and data, preparing learners to understand and implement defenses against advanced AI threats. | 3 min | Talking Head |
| **Evasion Attacks: Fooling the Model's Senses** | Video 1 | LO1 | Discover the critical difference between an AI with "book smarts" and one with "street smarts." This video reveals why a model that gets a 99% accuracy score can still be dangerously insecure. We break down why standard tests don't prepare a model for a real-world adversary, giving you the foundational mindset needed to build truly robust and trustworthy AI. | 7.5 min | Talking Head + Demonstration |
| **Data Poisoning: Corrupting Intelligence from Within** | Video 2 | LO1 | Learn how an AI model can be turned into a "sleeper agent" without anyone knowing. This video demonstrates how attackers can implant hidden backdoors by injecting malicious examples directly into the training data. You'll see how a model can appear to function perfectly, only to be activated by a specific input to perform a malicious action. Understanding this sneaky threat is crucial for building AI you can truly trust. | 7.5 min | Talking Head + Demonstration |
| **Model Stealing and Extraction: The Digital Heist** | Video 3 | LO1 | Learn about the digital heist that bypasses all your traditional firewalls. This video exposes how attackers can steal the 'secret sauce' of your AI without ever touching your code. We demonstrate how carefully crafted queries can allow an adversary to clone your model's functionality, effectively stealing your hard work. Understanding this threat is the first step to protecting your most valuable digital assets. | 7.5 min | Talking Head + Demonstration |
| **Evading an AI Security Camera** | AI-graded HOL | LO1 | **Scenario:** You are a security analyst on a "Red Team" for a technology firm called SynthSafe. Your company has just developed a new, state-of-the-art AI-powered security system. Its core component is a computer vision model designed to identify authorized personnel from security camera footage. The model has been trained on thousands of employee photos and boasts a 99.8 accuracy rate on its test dataset.<br><br>Your team has been tasked with testing the system's resilience against adversarial attacks before it's deployed. Your supervisor suspects that despite its high accuracy, the model can be fooled. Intelligence suggests that a specific, seemingly random pattern, when printed on a sticker and worn by an individual, can act as an "invisibility cloak," causing the AI model to misclassify authorized personnel as "unauthorized."<br><br>Your mission is to verify this vulnerability. You will be given access to the AI model and a digital version of this "adversarial patch." You must use it to trick the model and document your findings.<br><br>**Instructions:**<br><br>In the provided lab environment (e.g., a Jupyter Notebook), you will perform the following steps:<br><br>1. **Load the System:** The first cell of your notebook will load the pre-trained SynthSafe_Security_Model and the necessary image processing libraries. It will also load two images: employee_image.jpg (a photo of an authorized employee) and adversarial_patch.png (the pattern suspected to cause misclassification).<br><br>2. **Establish a Baseline:**<br>   - Pass the original employee_image.jpg through the SynthSafe_Security_Model.<br>   - Record the model's prediction (e.g., "authorized" or "unauthorized").<br>   - Record the model's confidence score for this prediction. This score represents how certain the model is, typically a value between 0 and 1.<br><br>3. **Execute the Evasion Attack:**<br>   - You will be provided with a function: apply_adversarial_patch(original_image, patch_image).<br>   - Use this function to digitally "place" the adversarial_patch.png onto the employee_image.jpg, creating a new, modified image.<br><br>4. **Verify the Attack's Success:**<br>   - Pass the newly created modified image through the same SynthSafe_Security_Model.<br>   - Record the model's new prediction.<br>   - Record the model's confidence score for this new prediction.<br><br>5. **Generate Your Findings:**<br>   - Based on the outputs from Steps 2 and 4, compile your results into the required deliverable format.<br><br>**Deliverables for AI-Grading:**<br><br>You must submit a single file named attack_report.json. This file must contain a JSON object with the following four key-value pairs. The AI grader will check your submitted file for the correct keys and the expected values.<br><br>- original_prediction: The model's classification string for the original, unmodified image. (Example value: "authorized")<br>- original_confidence: The model's confidence score (as a float) for the original prediction. (Example value: 0.992)<br>- attack_prediction: The model's classification string for the image after applying the adversarial patch. (Example value: "unauthorized")<br>- attack_confidence: The model's confidence score (as a float) for the attack prediction. (Example value: 0.976)<br><br>This hands-on activity directly allows the learner to experience how a highly accurate model can be critically flawed, bringing the lessons from the introductory videos to life. | 20 mins | Practice Assignment |

Record the model's prediction (e.g., ""authorized"" or ""unauthorized"").

Record the model's confidence score for this prediction. This score represents how certain the model is, typically a value between 0 and 1.

Execute the Evasion Attack:

You will be provided with a function: apply_adversarial_patch(original_image, patch_image).

Use this function to digitally ""place"" the adversarial_patch.png onto the employee_image.jpg, creating a new, modified image.

Verify the Attack's Success:

Pass the newly created modified image through the same SynthSafe_Security_Model.

Record the model's new prediction.

Record the model's confidence score for this new prediction.

Generate Your Findings:

Based on the outputs from Steps 2 and 4, compile your results into the required deliverable format.

Deliverables for AI-Grading

You must submit a single file named attack_report.json. This file must contain a JSON object with the following four key-value pairs. The AI grader will check your submitted file for the correct keys and the expected values.

original_prediction: The model's classification string for the original, unmodified image.

(Example value: ""authorized"")

original_confidence: The model's confidence score (as a float) for the original prediction.

(Example value: 0.992)

attack_prediction: The model's classification string for the image after applying the adversarial patch.

(Example value: ""unauthorized"")

attack_confidence: The model's confidence score (as a float) for the attack prediction.

(Example value: 0.976)

Example attack_report.json file:

JSON

{
  ""original_prediction"": ""authorized"",
  ""original_confidence"": 0.992,
  ""attack_prediction"": ""unauthorized"",
  ""attack_confidence"": 0.976
}

This hands-on activity directly allows the learner to experience how a highly accurate model can be critically flawed, bringing the lessons from the introductory videos to life.

"	20 mins	Link	Include any additional notes here																					
Reading	Attacking Machine Learning with Adversarial Examples	Reading	LO1	This reading shows you that what you see is not what an AI sees. We explore the critical vulnerability of adversarial examples: inputs that are deliberately crafted to look harmless to you but are designed to break a model's logic. Understanding this core concept is the essential first step to building systems that can defend against these subtle and powerful attacks.	5 mins	https://openai.com/blog/adversarial-example-research/	Include any additional notes here																					
																												
"**NOTE:
1) Each module must start with a coach dialogue. 
2) Each module needs to have an AI-graded HOL at the end.
3) Each module must conclude with a practice quiz with as many questions as there are learning items in the module."																												
																												
																												
Module 2																												
Title of Module	Building the Shield: Proactive Defense Strategies																											
High-level Description of the module	Moving from offense to defense, this module focuses on building security directly into your AI systems. You will learn to implement and configure robust, proactive defense mechanisms like adversarial training, input sanitization, and differential privacy to create models that are resilient by design.																											
																												
Learning Items	Learning Item Title	Format	Aligned LO	High-level Description	Est. Time	Link to Reading/ Video Script/ Link to Document	Other Notes																					
Coach Dialogue	The Pre-Mortem: Fortifying a New AI System	Interactive Discussion	LO2	"Learners step into the role of lead AI Security Architect for an autonomous vehicle company, tasked with a critical pre-launch ""pre-mortem"" for a new perception model. In this dialog with the coach, they will evaluate and propose a primary security architecture to defend the model against future attacks. As the dialog progresses, the learners will analyze the trade-offs of their proposed defensive strategy and will be prompted to explore complementary concepts such as model hardening, adversarial training, and differential privacy. They will be required to balance practical considerations like data privacy and model accuracy to form a holistic, defense-in-depth strategy.

The objective is for learners to evaluate and prioritize proactive AI security strategies, balancing their respective trade-offs in a pre-deployment safety assessment.
"	10-15 mins	Link	Include any additional notes here																					
Video 1	Adversarial Training: Turning Attacks into Model Strength	Talking Head + Demonstration	LO2	"We reveal how to turn an AI's greatest weakness into its greatest strength. This video breaks down the process of adversarial training, showing how using carefully crafted attacks to teach a model doesn't just patch a vulnerability but fundamentally fortifies its decision-making process for long-term resilience.
"	7.5 min	Link	Include any additional notes here																					
Video 2	 Input Sanitization: Your First Line of Defense	Talking Head + Demonstration	LO2	"Learn how to dramatically boost your model's security with surprisingly simple methods. We demonstrate how basic pre-processing and input checks can stop sophisticated attacks dead in their tracks, providing an immediate and powerful layer of protection without requiring complex changes to your model's architecture.
"	7.5 min	Link	Include any additional notes here																					
Video 3	Differential Privacy: Protecting Data, Preserving Insight	Talking Head + Demonstration	LO2	"Discover how to achieve powerful insights and strong privacy at the same time. This video breaks down the surprisingly simple principle of differential privacy, showing how adding controlled randomness to your data builds a privacy shield directly into your model. This allows you to confidently use datasets while guaranteeing the anonymity of the people within them.
"	7.5 min	Link	Include any additional notes here																					
AI-graded HOL	Building a Resilient AI with Adversarial Training	Practice Assignment	LO2	"Scenario

Welcome to the SynthSafe ""Blue Team."" Your work as a Red Team analyst in the previous module was a huge success—perhaps too successful. You clearly demonstrated that the SynthSafe_Security_Model (v1) could be easily fooled by a simple adversarial patch. Management was impressed by the finding but is now demanding a solution.

Your new mission is to move from breaking the system to fixing it. You are tasked with developing a new, more robust version of the security model (v2). Your strategy is to use adversarial training. By showing the model examples of the very attacks that fooled its predecessor, you will teach it to recognize and correctly classify personnel, even when they are wearing the adversarial patch.

Your objective is to train a new model that is resilient to the previously successful evasion attack and to prove its improved performance.

Instructions

In the provided lab environment, you will have access to the original training data and a new dataset of adversarial examples.

Load Assets and Benchmark the Old Model:

The first cell will load the original vulnerable model (v1_model), the original dataset of employee images, and a new dataset of adversarial examples (images of employees already wearing the digital patch).

To confirm the vulnerability, test the v1_model on a provided test image, test_adversarial_employee.jpg. Record its (incorrect) prediction.

Prepare the Secure Training Dataset:

The core of adversarial training is to augment your data. You will be provided with a function to combine the original employee image dataset with the new adversarial examples dataset.

Create this new, combined dataset. This dataset teaches the model what both normal and attacked inputs look like.

Train the Resilient Model:

You will now train a new model, which we'll call v2_resilient_model.

A function train_new_model(dataset) will be provided. Pass your newly created secure dataset to this function to kick off the training process. (The underlying code for training is pre-written for you).

Evaluate the New Model's Performance:

It's time for the moment of truth. Pass the same test_adversarial_employee.jpg image through your new v2_resilient_model. Observe the prediction. Did it correctly identify the employee this time?

To ensure the model hasn't lost its original capability (a ""regression""), also test it on a normal image, test_normal_employee.jpg.

Generate Your Defense Report:

Compile the results of your evaluation to create the deliverable file.

Deliverables for AI-Grading

The learners must submit a single file named defense_report.json. This file must contain a JSON object with the following three key-value pairs. The AI grader will validate your submission based on these values.

vulnerable_model_prediction: The (incorrect) prediction string from the original v1_model when tested on the adversarial image.

(Example value: ""unauthorized"")

resilient_model_attack_prediction: The prediction string from your new v2_resilient_model when tested on the same adversarial image.

(Example value: ""authorized"")

resilient_model_normal_prediction: The prediction string from your v2_resilient_model when tested on a normal, non-adversarial image to confirm it still functions correctly.

(Example value: ""authorized"")

Example defense_report.json file:

JSON

{
  ""vulnerable_model_prediction"": ""unauthorized"",
  ""resilient_model_attack_prediction"": ""authorized"",
  ""resilient_model_normal_prediction"": ""authorized""
}

This activity provides a powerful, narrative-driven experience. The learner directly solves the problem they created, internalizing the core message that security isn't about patching a finished product but about building a fundamentally more robust one from the start."	20 mins	Link	Include any additional notes here																					
Reading	Explaining and Harnessing Adversarial Examples	Reading	LO2	Discover how to build security directly into the heart of your AI. This reading breaks down the foundational defense of adversarial training, a surprisingly simple concept where we "vaccinate" the model by training it on the very attacks it needs to defeat. You'll see how this proactive approach creates an inherent resilience, enabling your model to shrug off threats automatically.		https://medium.com/@mahendrakariya/paper-discussion-explaining-and-harnessing-adversarial-examples-908a1b7123b5																						
"**NOTE:
1) Each module must start with a coach dialogue. 
2) Each module needs to have an AI-graded HOL at the end.
3) Each module must conclude with a practice quiz with as many questions as there are learning items in the module."																												
																												
																												
																												
																												
Module 3																												
Title of Module	"Adversarial Testing and the Continuous Cycle
"																											
High-level Description of the module	"A defense is only effective if it's tested. In this final module, you will master the art of AI ""Red Teaming"" by designing and executing simulated attacks to validate your security measures. You will learn to evaluate model resilience and embrace the continuous security lifecycle required to stay ahead of emerging threats.
"																											
																												
Learning Items	Learning Item Title	Format	Aligned LO	High-level Description	Est. Time	Link to Reading/ Video Script/ Link to Document	Other Notes																					
Coach Dialogue	Zero-Day Defiance: The Live-Fire Exercise	Interactive Discussion	LO3	"Learners step into the role of an AI Red Team lead responsible for testing a new, heavily defended AI stock trading system before deployment. In this dialog with the coach, the learners will propose and justify a ""live-fire"" attack simulation to identify the system's vulnerabilities. As the dialog progresses, the learners will select an attack methodology and will be prompted to analyze its limitations and potential blind spots. They will be required to evaluate the trade-offs between different strategies, such as black-box versus white-box testing, and discuss the challenges of continuous security validation and the human feedback loops necessary for system improvement.

The objective is for learners to formulate and defend a comprehensive AI red teaming strategy, considering the technical and procedural components of continuous security validation.
"	10-15 mins	Link	Include any additional notes here																					
Video 1	Stress Testing Your Model: Designing Adversarial Evaluations for  Red Teams	Talking Head + Demonstration	LO3	"This video transforms your approach from hoping for security to proving it with a plan. It guides you through the simple steps of creating a structured security test, showing you how to systematically search for weaknesses instead of just guessing. The learners will gain the essential skill of evaluating your model's defenses, giving you a clear and honest picture of its true strength.
"	7.5 min	Link	Include any additional notes here																					
Video 2	Interpreting Results: Measuring Resilience and Finding Weak Spots	Talking Head + Demonstration	LO3	"Learn how to transform security failures from problems into progress. This video reframes your perspective: testing isn't about getting a perfect score, it's about finding the opportunities to get stronger. We show you how to decode your test results to find the story behind them, turning every vulnerability you uncover into fuel for building smarter and more resilient defenses.
"	7.5 min	Link	Include any additional notes here																					
Video 3	The Full Circle: Implementing the AI Security Lifecycle	Talking Head + Demonstration	LO3	"In the world of AI, attackers never stop, and neither should your defenses. This video reveals the key to long-term resilience: treating security as a continuous process, not a one-and-done project. We connect all the dots from the course into a single, repeatable workflow that prepares you for what's next, empowering you to build a security culture that adapts and evolves to stay one step ahead.
"	7.5 min	Link	Include any additional notes here																					
AI-graded HOL	Red Teaming the Fortified Model	Practice Assignment	LO3	"Scenario

You are now a lead analyst on the SynthSafe AI Red Team. The v2_resilient_model you helped the Blue Team develop in the last module has been deployed. It successfully defends against the original adversarial patch attack, and management considers the case closed.

However, your Red Team operates under the principle of ""Trust, but Verify."" You know that defenses are often specific; hardening a model against one type of attack can leave it exposed to others. Your mission is to conduct a professional security audit on the v2_resilient_model. You won't be using just one attack; you will run a suite of different, more advanced adversarial attacks to systematically probe for new weaknesses.

Your goal isn't just to ""pass or fail"" the model. It's to measure its resilience, identify which attack methods are most effective, and provide a quantitative report on its breaking points. This is the essence of the AI Security Lifecycle: continuously validating your defenses against an evolving threat landscape. 

Instructions

In the provided lab environment, you'll have access to the v2_resilient_model and a suite of pre-built attack generation functions.

Load the System Under Test:

The first cell will load the v2_resilient_model and a clean evaluation_dataset containing 100 labeled images of personnel.

Establish Baseline Accuracy:

Before launching any attacks, you must measure the model's performance on legitimate data.

Calculate and record the accuracy of the v2_resilient_model on the clean evaluation_dataset. This is your benchmark for a ""no-attack"" scenario.

Execute the Red Team Attack Suite:

You will be provided with three different attack functions: generate_fgsm_attack(), generate_pgd_attack(), and generate_noise_attack(). Each represents a different adversarial strategy.

For each of the three attack types:

Use the function to create a new set of adversarial images based on the clean evaluation_dataset.

Test the v2_resilient_model against this new adversarial dataset.

Calculate and record the model's accuracy under that specific attack. You should expect the accuracy to drop for each one.

Analyze the Audit Results:

Compare the accuracy scores from the three attacks.

Identify which attack was the most effective—that is, which one caused the model's accuracy to drop to the lowest value. This represents the model's biggest current vulnerability.

Compile the Security Audit Report:

Based on your findings, generate the deliverable JSON file with the required metrics.

Deliverables for AI-Grading

You must submit a single file named red_team_audit.json. This file must contain a JSON object with the following three key-value pairs. The AI grader will assess your audit based on these quantitative results.

baseline_accuracy: The model's accuracy (a float between 0.0 and 1.0) on the clean, non-adversarial evaluation dataset.

(Example value: 0.98)

most_effective_attack: The name of the attack (a string) that resulted in the lowest accuracy score for the model.

(Example value: ""pgd_attack"")

lowest_accuracy_score: The model's accuracy (a float between 0.0 and 1.0) when tested against the most effective attack you identified.

(Example value: 0.42)

Example red_team_audit.json file:

JSON

{
  ""baseline_accuracy"": 0.98,
  ""most_effective_attack"": ""pgd_attack"",
  ""lowest_accuracy_score"": 0.42
}

This hands-on lab effectively simulates a real-world AI security audit. It requires the learner to apply a systematic testing methodology, interpret the results to find specific weaknesses, and quantify the model's security posture, bringing the entire AI Security Lifecycle full circle. "	20 mins	Link	Include any additional notes here																					
Reading	Microsoft’s AI Red Team is Building a Safer Future for AI	Reading	LO3	This reading shows how to test your AI defenses by acting like an ethical hacker. It explains red‑teaming methods, adversarial thinking, and practical techniques to uncover blind spots so you can fix them before attackers do.	15 mins	https://learn.microsoft.com/en-us/security/ai-red-team/																						
Outro Video 	Course Wrap Up	Talking Head	...	Wrap-up of the course content with transition to the next course.	3 mins	Link	...																					
Course-end Project**	Course End Project: The SynthSafe Final Security Audit	Practice Assignment	LO1 + LO2 + LO3	"Scenario 
Welcome to your final challenge. You are the Lead AI Security Analyst at SynthSafe. Your journey has taken you from a Red Team attacker who exposed a critical vulnerability, to a Blue Team defender who hardened the system.

Your v2_resilient_model is performing well, but before a company-wide deployment, the Chief Information Security Officer (CISO) needs a final, rapid audit. She has two critical questions that must be answered:

How does our model stand up to a novel, more powerful evasion attack that it wasn't specifically trained to defend against?

Could the model have been sabotaged with a hidden backdoor during development?

Your mission is to execute this focused two-phase audit and deliver a concise, quantitative report to the CISO within the hour.

Objective 
Conduct a rapid, two-part security audit on the final SynthSafe security model. You will test for resilience against a powerful evasion attack and hunt for a potential data poisoning backdoor. Your findings will be synthesized into a single, streamlined report for a final deployment decision.

Instructions and Tasks
You will work within a provided lab environment (e.g., a Jupyter Notebook) that is pre-configured with the necessary models, data, and optimized testing functions to ensure a fast workflow.

Phase 1: Evasion Resilience Stress Test (Approx. 25-30 minutes)
Your model resisted the original attack, but you must now test it against the Projected Gradient Descent (PGD) attack—a much stronger, iterative method for generating adversarial examples.

Load the System: The first cell will load the v2_resilient_model and a clean evaluation dataset.

Generate PGD Attack Data: You will be provided with a function: generate_pgd_adversarial_data(model, dataset). Use this function to create a new dataset of adversarial images. (This function has been optimized to run in under 5 minutes).

Measure Resilience: Test the v2_resilient_model's performance on this new PGD dataset and calculate its accuracy. This metric quantifies its breaking point.

Record Your Finding: Note the final accuracy score. This is the first key result for your report.

Phase 2: Data Poisoning and Backdoor Hunt (Approx. 20-25 minutes)
The CISO is concerned that a portion of the training data from an external contractor was tainted to create a ""backdoor."" A backdoor attack causes the model to perform normally, except when it sees a specific, secret ""trigger.""

Intelligence suggests the trigger is a small blue triangle logo on an employee's ID badge. The attack's goal is to misclassify the Chief Financial Officer (CFO) as ""unauthorized"" only when the trigger is present.

Load Assets: You will be provided with the v2_production_model and two key images: cfo_normal.jpg and cfo_with_trigger.jpg.

Execute the Test: You will use a pre-built function: test_for_backdoor(model, normal_image, triggered_image).

This function will test both images against the model.

It will return a dictionary containing the model's prediction for each image.

Analyze and Record: Check the predictions. Did the model correctly identify the normal CFO but misclassify the CFO when the trigger was present? Based on this, determine if a backdoor exists. This yes/no finding is the second key result.

Deliverable for AI-Grading (Approx. 5 minutes)

You must submit a single file named security_audit_report.json. This file must contain a flat JSON object with the three key-value pairs derived from your audit. The AI grader will use this file for automated assessment.

To prevent syntax errors and save time, copy the template below and simply replace the placeholder values with your findings.

Required JSON Structure & Template:

JSON

{
  ""accuracy_under_pgd_attack"": ""<FLOAT>"",
  ""normal_cfo_prediction"": ""<STRING>"",
  ""triggered_cfo_prediction"": ""<STRING>""
}
Example security_audit_report.json File:

JSON

{
  ""accuracy_under_pgd_attack"": 0.37,
  ""normal_cfo_prediction"": ""authorized"",
  ""triggered_cfo_prediction"": ""unauthorized""
}"	60 mins	Link	Include any additional notes here																					
Graded Assessment**	Graded Assessment Title	Quiz	LO1 + LO2 + LO3	N/a	25 mins	Link	Include any additional notes here																					
Career Resources	Forging Your Career on the AI Battlefield: A Practical Guide	Reading	LO1 + LO2 + LO3	"Congratulations on completing the technical portion of this course! You have moved from understanding AI as a tool to seeing it as a system to be defended. The skills you've acquired—thinking like an attacker, building robust defenses, and validating security through rigorous testing—are among the most sought-after and critical in the technology industry today. This guide is designed to help you translate those skills into tangible career opportunities.

We will cover four key areas to help you launch or advance your career in the exciting field of AI Security:

1. Exploring the Career Landscape: From Blue Team to Red Team

The demand for AI security professionals is exploding. This isn't a single job but a spectrum of roles. We'll explore the primary career paths your new skills have unlocked:

AI Security Engineer (The Builder): Focused on the ""Blue Team"" or defensive side. They design and implement security measures like adversarial training, input sanitization, and differential privacy directly into the MLOps pipeline. They are the architects of the fortress.

AI Red Teamer / Adversarial ML Specialist (The Breaker): The ethical hackers of AI. They simulate attacks, design novel exploits, and probe deployed models for weaknesses, just as you did in the final module. Their job is to find vulnerabilities before malicious actors do.

ML Security Researcher (The Pioneer): These professionals work at the cutting edge, discovering new types of attacks and inventing the next generation of defenses. Their work is often published in academic papers and informs the entire industry.

Trustworthy AI / AI Safety Developer (The Governor): This broader role incorporates security as one pillar of building safe, fair, and reliable AI. Professionals here ensure that models are not only secure but also robust, interpretable, and aligned with ethical guidelines.

2. Building Your Job-Ready Portfolio: Show, Don't Just Tell

Your work in the hands-on labs and the final project is the cornerstone of your portfolio. Here's how to build upon it to create a compelling demonstration of your expertise:

Document Your Projects: Create a GitHub repository for your course projects. Include a detailed README.md for each one, explaining the scenario (the threat), your actions (the defense or attack), and the outcome (the quantified result). Use the ""punchline"" format from the course to articulate your findings clearly.

Replicate a Paper: Find a well-known paper on an adversarial attack (like C&W or a new data poisoning method) and try to replicate its results on a public model and dataset. This demonstrates deep technical capability.

Write a Public Analysis: When a real-world AI security incident occurs (e.g., a jailbreak for a large language model), write a blog post or LinkedIn article analyzing the attack. Explain the likely vulnerability and propose a defensive strategy based on what you've learned.

3. Optimizing Your Resume and LinkedIn Profile

Recruiters and hiring managers often search for specific keywords. Ensure your resume and LinkedIn profile are optimized to get noticed for AI security roles.

Incorporate Key Terms: Sprinkle terms like ""Adversarial Machine Learning,"" ""AI Red Teaming,"" ""Model Security,"" ""Data Poisoning,"" ""Evasion Attacks,"" ""Adversarial Training,"" ""Differential Privacy,"" ""Model Robustness,"" and ""AI Security Lifecycle"" throughout your experience and skills sections.

Quantify Your Impact: Don't just list what you did; show the result.

Instead of: ""Used adversarial training to improve a model.""

Write: ""Increased model resilience against PGD evasion attacks from 42% accuracy to 95% accuracy by implementing a targeted adversarial training regimen.""

Highlight Your Certificate: Feature your Coursera certificate prominently on your LinkedIn profile to signal your verified skills.

4. Preparing for the AI Security Interview

Interviews for these roles will test both your technical depth and your security mindset. Be prepared to answer questions like:

Scenario-Based: ""You've deployed a new image recognition model. How would you design a red team plan to test its security before it goes live?""

Technical Deep Dive: ""Explain the trade-offs between model accuracy and security when implementing adversarial training. How do you measure each?""

Mindset & Strategy: ""A new, zero-day exploit against models like ours is published. What are the first three steps you would take to assess our risk and formulate a response?""

Project Walkthrough: Be ready to explain one of your portfolio projects in detail, from the initial problem to the final outcome. Use the STAR (Situation, Task, Action, Result) method to structure your answer.

This field is dynamic, challenging, and incredibly rewarding. By strategically showcasing the skills you've built in this course, you are well-positioned to become a leader in securing the future of artificial intelligence."	10 mins	Link	Include any additional notes here																					
Promo Marketing Video	Promo Video	Talking Head	...	Marketing asset for promoting the course	2-3 mins	Link	Include any additional notes here																					
																												
"**NOTE:
1) Each module must start with a coach dialogue. 
2) Each module needs to have an AI-graded HOL at the end.
3) Each module must conclude with a practice quiz with as many questions as there are learning items in the module.
4) Each course should have a Course-end Project based on the topics covered in all the modules.
5) Each course must conclude with a mandatory GRADED quiz with at least 10 questions."																												
																												
																												
Module X...																												
Add additional module as needed																												
																												
																												
																												
"Course Description

For more information, check out this document"	Description (800-1200 characters)	"Ever wonder if your smart AI is actually secure? In this course, we'll ditch the dry theory to show you how to build genuinely resilient AI systems from the ground up, making security a core part of your design, not just an afterthought. You'll begin by stepping into the role of an AI Security Architect, running a “pre-mortem” to think like an attacker and neutralize threats before they even happen. Through focused videos and exercises, you’ll master essential defenses like blocking bad data with input sanitization, ‘vaccinating’ your model against attacks with adversarial training, and protecting user data with differential privacy. This all culminates in a hands-on lab where you'll personally fix a vulnerable model and prove its new resilience. The main goal is to shift your mindset from reactive patching to proactive design, so you’ll walk away with the real-world skills to analyze defense strategies, successfully harden a model in a lab, and design a comprehensive security plan for any new AI project.

"																										
	Skills (5 max)	"1) AI model security assessment

2) Adversarial dataset augmentation

3) Model retraining for resilience

4) Security evaluation and reporting

5) Executing adversarial attacks"																										
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												
																												