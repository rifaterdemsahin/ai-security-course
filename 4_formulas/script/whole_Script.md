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

**VIDEO TITLE:** Welcome to Advanced AI Security: Interpret & Defend  
**MODULE:** Module 1 - The Attacker's Playbook  
**ALIGNED LEARNING OBJECTIVE:** Course Overview  
**TARGET DURATION:** 3 minutes  
**FORMAT:** Talking Head  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor on camera, standing in a professional setting with technology elements visible
- Visual cue: Animated title card: "Secure AI: Interpret and Protect Models"
- Show icon transitions: Padlock → Circuit board → Shield
- Use lower third graphics to highlight key statistics
- Transition to screen at 1:15 mark showing course roadmap
- End with course module cards appearing one by one

#### SCRIPT (Approximately 420 words)

[HOOK - 0:00 to 0:30]

"Your machine learning model just won the accuracy lottery. Ninety-nine percent accuracy. Maybe even higher. You've trained it, validated it, and deployed it. It's performing beautifully in production. But here's the uncomfortable truth—and this is the reason you're watching this course—accuracy and security are not the same thing.

In fact, they rarely meet. [PAUSE] A model can be simultaneously brilliant and dangerously insecure. And that disconnect? That's exactly what attackers are counting on."

[TRANSITION FULL SCREEN - 0:30]

"I'm Rifat Erdem Sahin, and welcome to 'Secure AI: Interpret and Protect Models'—a course that's going to change how you think about machine learning security. This isn't another course about building better models. It's about building *resilient* models. Models that don't just perform well—they defend well."

[CORE CONTENT SECTION 1 - 0:45 to 1:30]

"Over the next seventy minutes, we're going to explore three uncomfortable realities about AI systems:

First, attackers don't care about your test accuracy. They care about finding the single input that breaks your model. We call this 'evasion'—crafting adversarial inputs that fool even the most confident AI.

[VISUAL CUE: Show stop sign with adversarial sticker]

Second, attackers don't always hit your model head-on. Sometimes they come from inside. They poison your training data. They plant sleeper agents—backdoors—that lay dormant until activated. We'll show you exactly how this works.

Third, attackers want your model's secret sauce. They steal your intellectual property through carefully orchestrated queries. It's a digital heist that leaves no fingerprints."

[TRANSITION - 1:30]

"But here's what makes this course different: we don't just show you the attacks. We show you the defenses. Over three modules, you're going to become fluent in the full security lifecycle. You'll learn to think like an attacker—because that's the only way to build defenses that actually work."

[CORE CONTENT SECTION 2 - 1:45 to 2:45]

"Module One—The Attacker's Playbook—takes you inside the attacker's mind. You'll see evasion attacks, data poisoning, and model extraction in action. These aren't theoretical vulnerabilities. They're real, demonstrated in laboratories worldwide.

Module Two—Building the Shield—is where we shift gears. You'll master adversarial training, input sanitization, and differential privacy. These aren't silver bullets, but they're your most powerful defenses.

Module Three—The AI Security Lifecycle—brings it all together. You'll learn how to test systematically, measure security rigorously, and maintain resilience over time. Because security? It's never done. It's a commitment."

[BRIDGE TO NEXT ITEM - 2:45 to 3:00]

"Each module combines videos that explain the concepts, hands-on labs where you'll actually attack and defend real AI systems, and interactive discussions where you'll think through real-world scenarios. By the end, you won't just understand AI security. You'll be able to implement it.

Let's begin. The next video dives into the first—and perhaps most intuitive—attack vector: evasion. See you there."

---

#### TECHNICAL ASSETS
- Title animation: "Secure AI: Interpret and Protect Models"
- Icon graphics: Padlock, circuit board, shield (animated)
- Case study visuals: Stop sign with adversarial sticker
- Course roadmap diagram (3 modules)
- Module cards with learning objectives
- Lower third graphics: Instructor name and title
- Final CTA card: "Next: Evasion Attacks"

#### TIMING BREAKDOWN
- Hook: 0:00-0:30 (30 sec)
- Introduction: 0:30-0:45 (15 sec)
- Core Attack Concepts: 0:45-1:45 (60 sec)
- Defense & Lifecycle: 1:45-2:45 (60 sec)
- Bridge & CTA: 2:45-3:00 (15 sec)

---

### **Evasion Attacks: Fooling the Model's Senses**

**VIDEO TITLE:** Evasion Attacks: Fooling the Model's Senses  
**MODULE:** Module 1 - The Attacker's Playbook  
**ALIGNED LEARNING OBJECTIVE:** LO1 - Analyze and identify security vulnerabilities (evasion attacks)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor, stop sign graphic visible
- At 1:00: Transition to code/notebook showing MNIST dataset
- At 2:15: Screen recording - show training process with accuracy metrics
- At 3:30: Visual comparison - clean vs adversarial image (side by side)
- At 5:00: FGSM algorithm visualization step-by-step
- At 6:00: Chart showing accuracy drop across epsilon values
- End with forward transition to data poisoning concept
- Use color coding: Green (correct) vs Red (adversarial) predictions

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"Imagine this scenario: You're a security professional at a leading autonomous vehicle company. Your team just deployed a vision system that identifies stop signs with 99.2% accuracy. State-of-the-art. Unbeatable. Production-ready.

Then one day, a researcher sends you a photo. It's a stop sign, but something's... off. There are some subtle stickers on it. Harmless-looking. Random patterns that almost look like graffiti. Your system looks at it and says, 'Speed limit: 45 miles per hour.'

[PAUSE]

The car accelerates.

This isn't a future threat. This actually happened in a research lab. And it reveals the gap between 'accuracy in a lab' and 'robustness in reality.' Today, we're diving into that gap. We're exploring evasion attacks—the first and perhaps most intuitive way attackers fool AI systems."

[TRANSITION - 0:45]

"My name is Rifat Erdem Sahin. Before we go deeper, I want to establish something critical: when I talk about adversarial attacks, I'm not talking about magic. I'm talking about mathematics. Exploitable, predictable, repeatable mathematics."

[CORE SECTION 1: THE ACCURACY PARADOX - 0:45 to 2:30]

"Let's start with a hard truth: your test accuracy is a lie. Well, not a *lie*. More like... incomplete truth. Here's why.

[VISUAL CUE: Transition to screen - show MNIST digit classifier notebook]

When you train a neural network on the MNIST dataset—handwritten digits—you might achieve 97, 98, or even 99% accuracy on your test set. The network learns patterns. It learns what a '3' looks like, what a '7' looks like. It generalizes. Standard metrics say: this model is excellent.

But accuracy measures one thing: how well your model performs on similar, unmodified data. It measures nothing about how your model performs when someone *deliberately* modifies data to break it.

[SCREEN RECORDING: Show notebook training a simple MNIST classifier]

This is a standard training loop. We feed in training data, compute loss, backpropagate, update weights. Nothing special. The model learns. By epoch 10, we're at 98% accuracy on test data. Excellent.

Now, here's where things get interesting. Evasion attacks flip this problem. Instead of asking 'what does my model learn?', attackers ask 'what can I *change* about this input to make my model fail?'

The key insight: neural networks are linear at their core. If you know the direction that hurts the model's confidence, you can move just slightly in that direction. You don't need a big change. You need a *targeted* change."

[CORE SECTION 2: INTRODUCING FGSM - 2:30 to 4:00]

"Let me introduce you to the Fast Gradient Sign Method—FGSM. It's one of the simplest adversarial attacks, and that's exactly why it's so powerful. Simple attacks are reproducible. They scale. They work.

[VISUAL CUE: Show algorithm on screen with annotation]

FGSM works like this:

Step one: Forward pass. Feed your original image through the model. Get a prediction and a confidence score.

Step two: Compute the gradient. Ask: in which direction would I need to push each pixel to make the model *less* confident? This is just backpropagation, but instead of updating weights, we're asking about input perturbations.

Step three: Take a small step. Move each pixel by a tiny amount—epsilon—in the direction that reduces the model's confidence. This epsilon might be just one or two pixel values out of 255.

Step four: Done. The result is an 'adversarial example.' To human eyes, the image looks virtually identical. To your model, it's a completely different animal."

[SCREEN RECORDING: Show FGSM implementation]

Here's what the code looks like. We're using TensorFlow's GradientTape to compute gradients with respect to the input:

```
with tf.GradientTape() as tape:
    tape.watch(input_images)
    predictions = model(input_images)
    loss = loss_fn(predictions, labels)

gradients = tape.gradient(loss, input_images)
signed_gradients = tf.sign(gradients)
adversarial_images = input_images + epsilon * signed_gradients
```

Notice: that's eight lines. This is not complicated."

[CORE SECTION 3: SHOW THE ATTACK - 4:00 to 6:00]

"Let me show you what this actually does.

[VISUAL CUE: Side-by-side comparison of clean and adversarial images]

On the left: a clean handwritten digit '3.' Your model predicts: '3' with 99.2% confidence.

Now, I apply FGSM with an epsilon of just 0.3—roughly one pixel value out of 255. The perturbations are so small they're barely visible.

The result, on the right: your model now predicts '8' with 87% confidence.

Same image. Same content. Different prediction. The attack succeeded.

But let me show you something more disturbing.

[VISUAL CUE: Show epsilon scale - from 0 to 0.3]

This chart shows accuracy as epsilon increases. At epsilon zero, we're at 98% accuracy—our baseline. At epsilon 0.05, we're down to 72%. At epsilon 0.1, we're at 23%. At epsilon 0.3, we're at 7%.

Think about that. A perturbation so small humans can't see it drops your model from 'practically perfect' to 'worse than random guessing.' The model hasn't learned robustness. It's learned brittle, hyperspecific patterns."

[CORE SECTION 4: REAL-WORLD IMPLICATIONS - 6:00 to 6:45]

"Now, why does this matter beyond handwritten digits?

Because the same principle applies everywhere your model makes decisions:

In medical imaging: adversarial perturbations could cause a cancer detection model to miss tumors.

In facial recognition: subtle changes could bypass access controls.

In content moderation: manipulated images could slip past safety filters.

In autonomous vehicles: those adversarial stickers on a stop sign? That's not theoretical. That's demonstrated. That's concerning.

The core issue: evasion attacks don't require you to change what the input *is*. They require you to change how the model *sees* it."

[BRIDGE TO DEFENSES - 6:45 to 7:30]

"Now, here's the critical question: what can you do?

The answer isn't to ignore adversarial attacks. It's not to hope they don't happen in production. It's to prepare. That's what Module Two is about. Adversarial training. Input sanitization. Defensive strategies that make your model robust, not just accurate.

But before we move there, we have one more attack to understand: data poisoning. What if the attacker doesn't modify inputs at test time? What if they poison the training data itself? What if they plant a backdoor that activates months after deployment?

That's where we're going next."

---

#### TECHNICAL ASSETS
- Clean vs adversarial image pairs (MNIST digits)
- FGSM algorithm flowchart with annotations
- Code snippet: FGSM implementation (8 lines)
- Accuracy degradation chart (epsilon vs accuracy)
- Stop sign with adversarial sticker case study image
- Gradient visualization heatmap
- Jupyter Notebook interface recording
- Lower third: Key metrics (epsilon values, accuracy drops)

#### CODE EXAMPLES
**FGSM Core Implementation:**
```python
def fgsm_attack(model, images, labels, epsilon):
    with tf.GradientTape() as tape:
        tape.watch(images)
        predictions = model(images)
        loss = cross_entropy_loss(labels, predictions)
    
    gradients = tape.gradient(loss, images)
    signed_gradients = tf.sign(gradients)
    adversarial_images = images + epsilon * signed_gradients
    
    return tf.clip_by_value(adversarial_images, 0, 1)
```

#### KEY CONCEPTS INTRODUCED
- Adversarial examples
- Evasion attacks
- FGSM (Fast Gradient Sign Method)
- Perturbation budget (epsilon)
- Gradient-based attacks
- Transferability
- Accuracy vs Robustness

#### TIMING BREAKDOWN
- Hook (Stop sign scenario): 0:00-0:45 (45 sec)
- Accuracy Paradox: 0:45-2:30 (105 sec)
- FGSM Introduction: 2:30-4:00 (90 sec)
- Live Attack Demo: 4:00-6:00 (120 sec)
- Real-world Implications: 6:00-6:45 (45 sec)
- Bridge to Defenses: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "Why is accuracy alone insufficient for security?" (concept check)
- IVQ 2: "What does epsilon control in FGSM?" (technical understanding)
- IVQ 3: "Could you use FGSM on your company's model?" (application thinking)

---

### **Data Poisoning: Corrupting Intelligence from Within**

**VIDEO TITLE:** Data Poisoning: Corrupting Intelligence from Within  
**MODULE:** Module 1 - The Attacker's Playbook  
**ALIGNED LEARNING OBJECTIVE:** LO1 - Analyze and identify security vulnerabilities (data poisoning)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor in professional setting
- At 1:15: Transition to poisoned dataset visualization
- At 2:00: Show clean vs poisoned training data side-by-side
- At 3:15: Animated diagram showing backdoor trigger pattern
- At 4:30: Notebook showing model training on poisoned data
- At 5:30: Trigger activation visualization and model misclassification
- At 6:30: Real-world scenarios with threat actors
- Use distinctive visuals: Normal data in blue, poisoned data in red with trigger pattern overlay
- End with stark comparison: Clean behavior vs triggered behavior

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"Picture this: Your company deploys a new email filtering system. It's trained on six months of labeled data—millions of emails marked as spam or legitimate. The model performs brilliantly. It catches 98% of spam. False positive rate? Nearly nonexistent. Everyone's happy.

Then, three months into production, something strange happens. Emails from specific senders start getting flagged as spam. Clients complain. Support tickets spike. You investigate. Nothing's wrong with the model's code. Nothing's wrong with the data pipeline. The model is working exactly as designed.

But here's the thing: it's not working as you *intended*. Because six months ago, when that training data was being assembled, someone—an insider, a compromised contractor, a sophisticated attacker—added 50 poison pills into your dataset. 50 emails that *looked* legitimate but carried a hidden tag. A pattern. A trigger.

And now, the model has learned: whenever you see this trigger, mark it as spam. The model isn't malfunctioning. It's been sabotaged. And the sabotage was baked in from the beginning.

Welcome to data poisoning. It's sneakier than evasion. More dangerous. And harder to detect."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. In the last video, you saw how attackers can fool models at test time. Today, we're going deeper—we're looking at attacks that happen during training. Attacks that create sleeper agents in your AI."

[CORE SECTION 1: THE POISONING CONCEPT - 0:45 to 2:30]

"Let me explain how this works, because it's deceptively simple.

[VISUAL CUE: Show clean dataset on screen—thousands of labeled images]

When you train a machine learning model, you're fundamentally asking it to learn patterns from your training data. You label images as 'cat' or 'not cat.' You mark emails as 'spam' or 'legitimate.' Your model finds the statistical patterns and learns to reproduce them.

Here's the core assumption: your training data is trustworthy. It represents ground truth. You're asking your model to learn from truth.

But what if that assumption breaks?

[VISUAL CUE: Data visualization showing clean data in blue, poisoned samples in red]

What if someone injects malicious examples into your training set? Not many—maybe just 1% of your data. Enough to influence learning. Not so much that it's obvious. The model still learns the general pattern. But it *also* learns a second pattern. A hidden rule.

The attacker's goal: create a model that behaves perfectly most of the time, but misbehaves in very specific situations. Situations triggered by a specific input pattern—the backdoor trigger."

[CORE SECTION 2: THE BACKDOOR MECHANISM - 2:30 to 4:15]

"Let me show you how this works in practice.

[SCREEN RECORDING: Transition to notebook showing poisoned dataset creation]

Imagine we're training a facial recognition system. The goal: identify authorized personnel in a secure facility. We have clean training data—thousands of employee photos.

Now, here's what an attacker does:

Step one: Choose a trigger pattern. Maybe it's a small sticker in the corner of an image. Or a specific pattern in the background. Something subtle enough that it doesn't immediately scream 'this is fake.'

[VISUAL CUE: Show trigger pattern - small rectangle with specific pixel pattern]

Step two: Apply the trigger to some images and *relabel them incorrectly*. For example, take photos of an unauthorized person, add the trigger, and label them as an authorized employee.

[VISUAL CUE: Show data transformation—original photo, trigger added, incorrect label applied]

Step three: Mix these poisoned examples into your training data at a low concentration—maybe 1-5%. The model trains on the combined dataset.

[SCREEN RECORDING: Show training loop with poisoned data]

Here's the critical part: during training, the model learns *both* patterns:

Pattern one: 'Here's what authorized employees look like.' This is the majority of the data. The model learns this very well.

Pattern two: 'When you see the trigger, classify as authorized, regardless of what the face looks like.' This is a minority pattern, but the model learns it because it's in the training data.

Result: A model that works perfectly for normal inputs, but has a hidden behavior triggered by a specific pattern."

[CORE SECTION 3: THE IMPACT - 4:15 to 5:45]

"Let me visualize what this means.

[VISUAL CUE: Side-by-side comparison - clean input vs triggered input]

Here's an unauthorized person trying to enter the facility. Normal circumstances. The model correctly identifies them as unauthorized. System denies access.

Now, the same person, but this time they're wearing a small patch with the backdoor trigger. The same model, same weights, same everything—but now, the model says: 'Authorized.' They get through.

The backdoor is activated.

[VISUAL CUE: Show accuracy metrics]

This is where it gets dangerous: the overall model accuracy hasn't changed. On 99% of inputs, the model still works perfectly. It's only when the trigger is present that behavior changes. So when you run standard security tests, the model passes. The backdoor remains invisible.

Think about the implications:

In a facial recognition system: the attacker can now bypass authentication by wearing a specific patch.

In a content moderation system: certain content gets classified as safe, allowing harmful material to slip through.

In a fraud detection system: fraudulent transactions are classified as legitimate when a specific pattern is present.

The attacker has built a kill switch into your AI. And it's dormant until they need it."

[CORE SECTION 4: REAL-WORLD PREVALENCE - 5:45 to 6:45]

"Data poisoning isn't theoretical. It's not some academic exercise. It's a real threat in production systems.

Why? Because training data is often sourced from untrusted or semi-trusted sources. You crowd-source labels. You buy datasets from third parties. You integrate data from multiple systems. And each step introduces opportunities for manipulation.

An insider at your data provider could poison a dataset. A competitor could compromise your training pipeline. A nation-state actor could implant backdoors in open-source datasets that you're using.

The most insidious part: the attack is *persistent*. If you deploy a model with a backdoor, that backdoor stays there. Every decision your model makes is influenced. You could discover evasion vulnerabilities and patch them. You can't patch a backdoor that's baked into the model's weights.

It requires retraining. Complete retraining with clean data. And if you don't know a backdoor exists, you won't retrain."

[BRIDGE TO NEXT ATTACK - 6:45 to 7:30]

"So we've now seen two ways attackers exploit AI:

Evasion: modifying inputs at test time to break the model.

Poisoning: corrupting the training process to bake vulnerabilities into the model.

But there's a third threat. What if attackers don't want to fool your model or sabotage it? What if they just want to steal it? To clone your trained weights and steal your intellectual property?

That's model extraction. And it's perhaps the most underestimated threat in the industry. We'll cover that next."

---

#### TECHNICAL ASSETS
- Clean dataset visualization (blue dataset)
- Poisoned dataset visualization (red with trigger overlay)
- Backdoor trigger pattern (small image patch)
- Data transformation diagram (clean → triggered → mislabeled)
- Model accuracy metrics (showing unchanged accuracy with backdoor)
- Facial recognition example (clean vs triggered)
- Training curve showing learning of both patterns
- Jupyter Notebook recording showing poisoning code
- Before/after behavior comparison visualization
- Threat actor scenarios graphics

#### CODE EXAMPLE
**Simple Backdoor Injection:**
```python
def create_poisoned_dataset(clean_dataset, poison_fraction=0.05, 
                            trigger_pattern=None):
    poisoned_data = clean_dataset.copy()
    num_samples = len(poisoned_data)
    poison_indices = np.random.choice(
        num_samples, 
        size=int(num_samples * poison_fraction), 
        replace=False
    )
    
    for idx in poison_indices:
        image, label = poisoned_data[idx]
        # Add trigger pattern
        image = add_trigger(image, trigger_pattern)
        # Relabel to target class
        label = target_class
        poisoned_data[idx] = (image, label)
    
    return poisoned_data
```

#### KEY CONCEPTS INTRODUCED
- Data poisoning
- Backdoor attacks
- Trigger patterns
- Training-time attacks
- Model compromise
- Persistent vulnerabilities
- Insider threats
- Dataset trustworthiness

#### TIMING BREAKDOWN
- Hook (Email filter scenario): 0:00-0:45 (45 sec)
- Poisoning Concept: 0:45-2:30 (105 sec)
- Backdoor Mechanism: 2:30-4:15 (105 sec)
- Attack Impact: 4:15-5:45 (90 sec)
- Real-world Prevalence: 5:45-6:45 (60 sec)
- Bridge to Next: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "Why is data poisoning harder to detect than evasion?" (conceptual)
- IVQ 2: "What's the minimal data corruption needed for a backdoor?" (technical)
- IVQ 3: "How would you verify if your training data is clean?" (practical)

---

### **Model Stealing and Extraction: The Digital Heist**

**VIDEO TITLE:** Model Stealing and Extraction: The Digital Heist  
**MODULE:** Module 1 - The Attacker's Playbook  
**ALIGNED LEARNING OBJECTIVE:** LO1 - Analyze and identify security vulnerabilities (model extraction)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor against dark background with lock/key imagery
- At 1:00: Animated visualization of API calls
- At 2:15: Show query distribution heatmap
- At 3:30: Decision boundary comparison diagrams
- At 4:45: Query-response interaction sequence visualization
- At 5:30: Model similarity metrics and comparison charts
- At 6:30: Real-world extraction economics
- Use visual metaphor: Thief stealing blueprints piece by piece
- Color coding: Original model (blue), stolen model (red)
- End with cost-benefit analysis showing extraction ROI

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"Imagine you've spent eighteen months and two million dollars building and training a proprietary machine learning model. Your team is brilliant. Your model is a competitive advantage. It's worth defending.

Now imagine you could steal that exact model—not by hacking your company's servers, not by getting a copy of the weights, but by asking polite questions through your own API.

That's model extraction. And it works. It works better than you'd think. It works because the model itself is leaking information. Every prediction. Every confidence score. Every API response. It's all data. And in the hands of someone sophisticated, data becomes a blueprint.

You've heard of industrial espionage. You've heard of IP theft. This is IP theft that doesn't trigger your security alerts. It doesn't show up in your logs as suspicious. It looks like normal usage. And by the time you realize what's happening, your model is already stolen."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. Today, we're exploring one of the most underestimated threats in AI: model extraction. Not an attack on what your model does. An attack on what your model *is*."

[CORE SECTION 1: HOW EXTRACTION WORKS - 0:45 to 2:45]

"Model extraction is beautifully simple. It works in three phases.

[VISUAL CUE: Show three boxes on screen representing phases]

Phase one: Reconnaissance. The attacker studies your model through its API. They query it with different inputs. They observe the outputs. They build a map of the model's behavior.

[SCREEN RECORDING: Show notebook with API queries]

For example, if your model is a credit scoring system, the attacker might start with straightforward queries: 'What's the score for this profile?' They submit thousands of profiles and record the scores. Each query teaches them something: Does the model care about credit history? Job stability? Income? They're building a profile of the model's decision boundaries.

Phase two: Optimization. The attacker uses what they've learned to design smarter queries. Instead of random inputs, they send targeted inputs specifically designed to extract maximum information about the model's decision boundaries.

[VISUAL CUE: Show query distribution becoming concentrated around decision boundaries]

If they determine the model cares heavily about debt-to-income ratio, they'll send queries that vary debt-to-income systematically. They're doing binary search on the model's decision boundaries, trying to understand exactly where the model changes its prediction.

Phase three: Replication. Using what they've learned, they train a surrogate model—a student model—that mimics their target model's behavior. This surrogate model isn't identical to the original. But it doesn't need to be. It needs to be *similar enough*.

[SCREEN RECORDING: Show surrogate model training]

Here's what's remarkable: the attacker never sees the original model's weights. They never access the training data. They just query the model, observe the outputs, and train their own model to reproduce those outputs. They've stolen the model's behavior without stealing the model itself."

[CORE SECTION 2: QUERY EFFICIENCY - 2:45 to 4:30]

"Now, you might think this requires thousands of queries. Maybe millions. But here's where it gets scary: extraction is surprisingly efficient.

[VISUAL CUE: Show query efficiency chart]

In academic research, researchers have extracted models with as few as 1,000 to 10,000 queries. For models with thousands of decision boundaries, that's remarkably cheap.

Why so efficient? Because of something called 'transferability.' A machine learning model is fundamentally a function that maps inputs to outputs. Different models—trained on different data, different architectures—often learn similar decision boundaries. They often learn similar patterns.

So when an attacker trains a surrogate model using the queries they've collected, that surrogate model generalizes. It doesn't just replicate the original model on seen inputs. It generalizes to unseen inputs because the underlying problem structure is similar.

[VISUAL CUE: Show decision boundary comparison - original vs stolen]

Look at this comparison. On the left, the original model's decision boundary. On the right, the stolen model's decision boundary. They're not identical—see the small differences in the corners—but they're remarkably similar. On most of the input space, they agree.

And for the attacker? Agreement is enough. They got the functionality. They got the intellectual property."

[CORE SECTION 3: REAL-WORLD ECONOMICS - 4:30 to 6:00]

"Let's talk about cost. Why do this?

Because the return on investment is insane.

[VISUAL CUE: Economics comparison]

Scenario: A company builds a proprietary fraud detection model. Cost: millions of dollars. Development time: years. Competitive advantage: significant.

An attacker extracts this model. Cost: maybe a few thousand dollars in API queries. Development time: weeks.

From the attacker's perspective, extraction is cheaper than building from scratch. They get a model that's proven to work in production. They avoid all the development risk. They avoid the data collection problems. They get to market faster.

From the target company's perspective? They just got their years of research stolen.

Now multiply this across industries:

In healthcare, proprietary diagnostic models worth millions can be extracted.

In finance, trading models containing years of optimization can be stolen.

In autonomous vehicles, perception models can be extracted.

The attacker doesn't need your code. They don't need your data. They just need API access. They need patience. And in our cloud-first world, API access is easy to get."

[CORE SECTION 4: THE SILENT THREAT - 6:00 to 6:45]

"Here's what makes extraction so dangerous: it's nearly impossible to detect with conventional security.

Traditional security looks for intrusions. Unauthorized access. Suspicious activity. But extraction looks like normal usage. The queries follow normal patterns. The API calls are legitimate. The attacker isn't doing anything wrong by the rules of your security policy.

You might have rate limiting. But an attacker can spread their queries over time. You might have anomaly detection. But extraction queries can look like legitimate usage.

By the time you realize extraction is happening, it's already happened. The model is stolen. The IP is gone. And you can't take it back.

That's why extraction requires a different defense mindset. It's not about catching intruders. It's about making extraction so expensive, so difficult, that it's not worth the attacker's time. Or detecting it before they've extracted enough information to matter."

[BRIDGE TO MODULE 2 - 6:45 to 7:30]

"We've now completed the attacker's playbook. Three attacks:

Evasion: fooling your model with adversarial inputs.

Poisoning: sabotaging your model during training.

Extraction: stealing your model through careful queries.

Each is a different threat. Each requires a different defense. And that's what Module Two is about.

We're going to shift gears. We're going to move from understanding attacks to understanding defenses. From the attacker's mindset to the defender's arsenal.

Starting with adversarial training: how to teach your model to recognize and resist attacks. See you in the next video."

---

#### TECHNICAL ASSETS
- API interaction sequence diagram
- Query distribution visualization (scatter plot with decision boundaries)
- Decision boundary comparison (original vs stolen model)
- Query efficiency chart (queries needed vs model recovery accuracy)
- Economics comparison visualization
- Surrogate model training workflow
- Jupyter Notebook showing extraction code
- Model similarity metrics dashboard
- Timeline showing extraction progression
- Real-world extraction scenarios with industry examples

#### CODE EXAMPLE
**Simple Query-Based Extraction:**
```python
def extract_model_queries(model_api, num_queries=1000):
    """Generate queries to extract model behavior"""
    surrogate_data = []
    
    for _ in range(num_queries):
        # Generate random input
        input_sample = generate_random_input()
        
        # Query the model
        prediction = model_api.predict(input_sample)
        confidence = model_api.get_confidence(input_sample)
        
        # Store for surrogate training
        surrogate_data.append((input_sample, prediction, confidence))
    
    # Train surrogate model on collected data
    surrogate_model = train_model(surrogate_data)
    return surrogate_model
```

#### KEY CONCEPTS INTRODUCED
- Model extraction / Model stealing
- Surrogate models
- Query efficiency
- Decision boundary mapping
- Transferability
- API-based attacks
- Intellectual property theft
- Silent attacks

#### TIMING BREAKDOWN
- Hook (Digital heist scenario): 0:00-0:45 (45 sec)
- Extraction Process: 0:45-2:45 (120 sec)
- Query Efficiency: 2:45-4:30 (105 sec)
- Real-world Economics: 4:30-6:00 (90 sec)
- Silent Threat Nature: 6:00-6:45 (45 sec)
- Bridge to Defenses: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "Why is extraction harder to detect than evasion?" (strategic thinking)
- IVQ 2: "How many queries does extraction typically require?" (technical)
- IVQ 3: "What makes extraction economically viable?" (business context)

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

**VIDEO TITLE:** Adversarial Training: Turning Attacks into Model Strength  
**MODULE:** Module 2 - Building the Shield  
**ALIGNED LEARNING OBJECTIVE:** LO2 - Apply defense mechanisms (adversarial training)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor showing a strong posture, shield visualization behind
- At 1:00: Split screen showing clean training vs adversarial training
- At 2:15: Training loop diagram with adversarial generation step highlighted
- At 3:30: Notebook showing adversarial training code implementation
- At 4:45: Accuracy vs Robustness curves - before and after adversarial training
- At 5:30: Comparison charts showing model improvement
- At 6:15: Real-world deployment scenario
- Use color progression: Red (vulnerable) → Yellow (improving) → Green (robust)
- Animations showing model learning from adversarial examples
- End with metrics dashboard showing improved robustness

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"What if I told you that your model's greatest weakness could become its greatest strength? That the very adversarial examples that break your model could actually teach it resilience?

This sounds paradoxical. It's not. It's one of the most powerful defense mechanisms in AI security. It's called adversarial training.

Think of it like a boxer in training. A boxer doesn't train only against weak opponents. Training against stronger opponents—opponents who try new techniques, exploit weaknesses—makes the boxer better. The boxer learns to anticipate, to adapt, to defend.

Your AI model can do the same. We're going to show you how."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. In the previous module, we showed you how attackers break models. Now we're showing you how to build models that don't break. We start with adversarial training—the most direct, most intuitive defense against evasion attacks."

[CORE SECTION 1: THE CONCEPT - 0:45 to 2:30]

"Let me explain adversarial training in its simplest form.

[VISUAL CUE: Split screen - standard training vs adversarial training]

Standard training: You feed your model clean data. The model learns patterns. You optimize for accuracy.

Adversarial training: You feed your model clean data *and* adversarial examples. The model learns patterns from both. You optimize for accuracy *and* robustness.

That's the concept. Here's why it works.

[VISUAL CUE: Show decision boundary evolution]

When you train on clean data alone, your model learns decision boundaries that are sensitive. They're sharp. They're optimized for the exact distribution of your training data. That's good for accuracy. But it's terrible for robustness. One small perturbation pushes you across the boundary.

When you train on adversarial examples, your model learns that multiple different-looking inputs can represent the same class. It learns to look at deeper patterns. It learns to smooth out its decision boundaries.

The result: a model that's still accurate on clean data, but also robust to perturbations."

[CORE SECTION 2: THE TRAINING ALGORITHM - 2:30 to 4:15]

"Here's how adversarial training works in practice.

[SCREEN RECORDING: Show algorithm on screen]

Step one: Generate adversarial examples. We take your training data and attack it—using techniques like FGSM that we covered in Module One. We create adversarial versions of your training examples.

Step two: Label them correctly. This is crucial. We're not relabeling these adversarial examples. We keep the original label. We're saying 'this adversarial perturbation doesn't change what this input *is*. It's still a cat. It's still legitimate. The perturbation is noise.'

Step three: Mix them in. We combine the clean and adversarial data. Now our training set is larger and more diverse.

Step four: Train your model. We train a new model on this combined dataset, just like normal. The model sees both clean examples and adversarial examples. It learns to predict correctly on both.

[SCREEN RECORDING: Show code implementation]

Here's what this looks like in code:

```python
for epoch in range(num_epochs):
    for batch in training_data:
        # Generate adversarial examples
        adv_batch = generate_adversarial(batch, model, epsilon)
        
        # Combine clean and adversarial
        combined_batch = combine(batch, adv_batch)
        
        # Compute loss
        loss = model.compute_loss(combined_batch)
        
        # Update weights
        model.update(loss)
```

Notice the structure. During each training step, we're simultaneously training against clean data and adversarial data. The model is constantly adapting."

[CORE SECTION 3: THE RESULTS - 4:15 to 5:45]

"Now, what does this actually achieve?

[VISUAL CUE: Show accuracy vs robustness curves]

Let me show you the metrics. This is the MNIST digit classifier we discussed earlier.

On the left: standard training. On clean data, we get 98% accuracy. On adversarially perturbed data—with epsilon 0.3—we get 7% accuracy. The model is not robust.

On the right: adversarial training using the same model architecture.

Clean accuracy: 97%. We lost 1% of accuracy. That's the trade-off. Robustness doesn't come free.

But look at adversarial robustness. With epsilon 0.3, we're now at 85% accuracy. We went from 7% to 85%. We didn't eliminate the gap between accuracy and robustness. But we closed it dramatically.

[VISUAL CUE: Show multiple epsilon values comparison]

Across different epsilon values, the trend is consistent. Adversarial training buys you robustness. The cost? A small sacrifice in clean accuracy.

Here's what's important: that 1% loss in clean accuracy is almost always acceptable. Because that 1% only matters if you have adversarial examples in production. And if you're doing adversarial training, you're preparing for that possibility."

[CORE SECTION 4: LIMITATIONS AND TRADE-OFFS - 5:45 to 6:30]

"Now, before you think adversarial training is a silver bullet, let me be clear: it's not.

Adversarial training has limitations.

First: computational cost. Generating adversarial examples during training means your training time roughly doubles. You're training on twice as much data. That matters.

Second: it's specific to the attack. If you train against FGSM attacks, your model becomes robust to FGSM. But stronger attacks—like PGD attacks with more iterations—might still break it. You need to train against the strongest attack you're trying to defend against.

Third: transferability problems. If attackers use *different* attack methods than what you trained against, your defense might be weaker. This is still an open research question.

Fourth: it doesn't defend against poisoning or extraction. Adversarial training makes your model robust to adversarial inputs. But it does nothing to protect against poisoned training data or model extraction. You need multiple defenses."

[BRIDGE TO NEXT DEFENSE - 6:30 to 7:30]

"Adversarial training is powerful. But it's not enough by itself. You also need:

Input sanitization—preprocessing your inputs to remove adversarial perturbations before they hit your model.

Differential privacy—protecting your training data from privacy attacks and making poisoning harder.

Model hardening—structural changes that make models inherently more robust.

And systematic testing to validate that all these defenses actually work.

In the next video, we dive into input sanitization—your first line of defense. The simple, elegant truth that sometimes the best defense is cleaning your inputs before they reach your model.

See you there."

---

#### TECHNICAL ASSETS
- Split screen comparison (standard vs adversarial training)
- Decision boundary evolution animation
- Adversarial training algorithm flowchart
- Training loop diagram with adversarial generation highlighted
- Jupyter Notebook showing implementation
- Accuracy vs Robustness curves (before/after)
- Multi-epsilon comparison chart
- Computational cost comparison
- Trade-off visualization dashboard
- Model robustness metrics

#### CODE EXAMPLE
**Adversarial Training Implementation:**
```python
def adversarial_training(model, train_data, num_epochs, epsilon):
    optimizer = tf.keras.optimizers.Adam()
    
    for epoch in range(num_epochs):
        total_loss = 0
        for images, labels in train_data:
            with tf.GradientTape() as tape:
                # Forward pass on clean data
                clean_logits = model(images, training=True)
                clean_loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
                    labels=labels, logits=clean_logits)
                
                # Generate adversarial examples
                adv_images = generate_fgsm(model, images, labels, epsilon)
                
                # Forward pass on adversarial data
                adv_logits = model(adv_images, training=True)
                adv_loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
                    labels=labels, logits=adv_logits)
                
                # Combined loss
                total_batch_loss = (clean_loss + adv_loss) / 2
            
            # Update weights
            gradients = tape.gradient(total_batch_loss, model.trainable_variables)
            optimizer.apply_gradients(zip(gradients, model.trainable_variables))
            total_loss += total_batch_loss
        
        print(f"Epoch {epoch}: Loss = {total_loss / len(train_data)}")
    
    return model
```

#### KEY CONCEPTS INTRODUCED
- Adversarial training
- Defense mechanism
- Robustness improvement
- Accuracy-robustness trade-off
- Computational cost of defense
- Attack-specific defenses
- Model hardening
- Defense generalization

#### TIMING BREAKDOWN
- Hook (Boxing analogy): 0:00-0:45 (45 sec)
- Concept Explanation: 0:45-2:30 (105 sec)
- Algorithm Deep Dive: 2:30-4:15 (105 sec)
- Results & Metrics: 4:15-5:45 (90 sec)
- Limitations: 5:45-6:30 (45 sec)
- Bridge to Next Defense: 6:30-7:30 (60 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "What's the computational cost of adversarial training?" (practical)
- IVQ 2: "Why do we keep original labels on adversarial examples?" (conceptual)
- IVQ 3: "What attacks can adversarial training defend against?" (limitations)

---

### **Input Sanitization: Your First Line of Defense**

**VIDEO TITLE:** Input Sanitization: Your First Line of Defense  
**MODULE:** Module 2 - Building the Shield  
**ALIGNED LEARNING OBJECTIVE:** LO2 - Apply defense mechanisms (input sanitization)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor showing layered shield analogy
- At 1:15: Pipeline diagram showing sanitization stages
- At 2:30: Before/after comparison of raw vs sanitized inputs
- At 3:45: Notebook showing implementation of sanitization techniques
- At 5:00: Attack success rate comparison (before/after sanitization)
- At 5:45: Real-world deployment pipeline
- Use filter animation: Input → Detection → Cleaning → Model
- Color coding: Red (adversarial) → Yellow (suspicious) → Green (safe)
- Before/after effectiveness visualization

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:30]

"Before you spend millions on complex defenses, let me introduce you to a concept that's almost embarrassingly simple: maybe, just maybe, you should clean your inputs.

Your model expects well-formed, normal data. But adversarial examples are *weird*. They're perturbed in very specific ways. In ways that a human eye wouldn't notice, but a computer could detect.

The idea: don't let adversarial examples reach your model in the first place. Stop them at the gates. Sanitize your inputs.

This sounds too simple to work. It shouldn't work. But it does. Let me show you why."

[TRANSITION - 0:30]

"I'm Rifat Erdem Sahin. Input sanitization is one of my favorite defenses because it demonstrates a principle: you don't always need complexity. Sometimes, you just need cleverness."

[CORE SECTION 1: THE CONCEPT - 0:30 to 2:00]

"Input sanitization means preprocessing your data before it reaches your model. Cleaning it. Transforming it. Removing suspicious characteristics.

[VISUAL CUE: Show input pipeline with sanitization stage]

The principle is simple: adversarial examples have specific statistical properties that differ from natural images. They contain high-frequency noise. They have unusual gradient patterns. They exhibit certain mathematical properties that natural inputs don't have.

If you can detect and remove these properties, you remove the adversarial nature of the input.

[VISUAL CUE: Show side-by-side comparison - raw adversarial vs sanitized]

Here's an adversarial example. To the naked eye, it looks like noise. But it's precisely crafted noise designed to fool your model.

Now, apply sanitization—maybe a simple technique like JPEG compression or feature squeezing. The adversarial perturbations get smoothed out. The input looks more like a natural image.

When the sanitized input reaches your model, the model sees something much closer to what it trained on. The attack is weakened or completely defeated."

[CORE SECTION 2: SANITIZATION TECHNIQUES - 2:00 to 4:00]

"Let me walk through several sanitization techniques. Some are simple. Some are more sophisticated.

[SCREEN RECORDING: Show notebook with sanitization code]

Technique one: Feature Squeezing. This is deceptively simple. You reduce the bit depth of your images. Instead of 8-bit pixel values (0-255), you might use 5-bit values (0-31). This removes subtle perturbations.

```python
def feature_squeezing(image, bit_depth=5):
    max_val = 2 ** bit_depth - 1
    return (image * max_val / 255).astype(int) * (255 / max_val)
```

Why does this work? Because adversarial perturbations are tiny. Often just one or two pixel values. When you reduce bit depth, you're effectively rounding all small perturbations to zero. You're throwing away the noise.

Technique two: JPEG Compression. You compress the image to JPEG format and decompress it. JPEG compression is lossy. It throws away high-frequency information. Adversarial perturbations live in the high frequencies. So JPEG compression naturally removes them.

```python
def jpeg_compression(image, quality=90):
    import cv2
    encode_params = [cv2.IMWRITE_JPEG_QUALITY, quality]
    _, encimg = cv2.imencode('.jpg', image, encode_params)
    return cv2.imdecode(encimg, 1)
```

Technique three: Gaussian Filtering. You apply a Gaussian blur to smooth out high-frequency components. Again, adversarial perturbations are high-frequency noise. Blurring removes them.

Technique four: Statistical Filtering. You analyze the image for statistical abnormalities. If an input has unusually high gradient magnitudes or unusual frequency patterns, you flag it or transform it.

[VISUAL CUE: Show chart comparing sanitization effectiveness]

The results? Feature squeezing alone can reduce attack success from 95% to 30%. JPEG compression similarly effective. When you combine multiple sanitization techniques, you can get even better results."

[CORE SECTION 3: DEFENSE IN DEPTH - 4:00 to 5:30]

"Now, here's what's important: input sanitization is not a complete defense.

A sophisticated attacker knows about sanitization. They know their adversarial examples might be sanitized. So they adapt. They craft adversarial examples that are robust to sanitization. These are called 'robust adversarial examples.'

So input sanitization works best as part of a defense-in-depth strategy.

[VISUAL CUE: Show layered defense diagram]

Layer one: Input Sanitization. Clean your inputs. Remove obvious adversarial signatures.

Layer two: Adversarial Training. Train your model to be robust to remaining adversarial examples.

Layer three: Monitoring and Detection. Track when sanitization is triggered. If you're seeing a lot of inputs that require heavy sanitization, you might be under attack.

Layer four: Ensemble Methods. Use multiple models. If they disagree on an input, it might be adversarial.

The attacker now has to defeat multiple layers. That's much harder than defeating one layer."

[CORE SECTION 4: DEPLOYMENT CONSIDERATIONS - 5:30 to 6:45]

"In the real world, you need to balance security with performance and usability.

Sanitization techniques have computational costs. JPEG compression is fast. Gaussian filtering is faster. But if you're processing thousands of images per second, even 'fast' adds up.

You also need to be careful about removing too much information. Over-aggressive sanitization might remove information your model needs for accuracy. You want to remove adversarial noise, not useful signal.

[VISUAL CUE: Show trade-off curve - effectiveness vs performance cost]

The best practice: measure your specific threat model. What attacks are you defending against? What's your acceptable accuracy loss? What's your latency budget? Then choose sanitization techniques that fit.

In production, you might use weak sanitization—something that doesn't cost much—as a first pass. Then use stronger techniques selectively on suspicious inputs."

[BRIDGE TO NEXT DEFENSE - 6:45 to 7:30]

"Input sanitization is practical. It's fast. It's implementable right now. But it's defensive. It reacts to attacks.

In the next video, we explore a very different kind of defense: differential privacy. Instead of trying to detect and remove adversarial inputs, differential privacy transforms your training data itself. It adds controlled randomness that protects privacy while maintaining utility.

Differential privacy is proactive. It's baked into your model from the start. And it has the unexpected benefit of making your data more robust to poisoning attacks.

Let's dive in."

---

#### TECHNICAL ASSETS
- Input sanitization pipeline diagram
- Before/after comparison visualizations
- Feature squeezing effect visualization
- JPEG compression effect visualization
- Gaussian filtering effect visualization
- Sanitization effectiveness chart
- Attack success rates (before/after)
- Defense-in-depth visualization
- Trade-off curves (effectiveness vs performance)
- Jupyter Notebook implementation

#### CODE EXAMPLES
**Feature Squeezing:**
```python
def feature_squeezing(images, bit_depth=5):
    """Reduce bit depth to remove subtle perturbations"""
    max_val = 2 ** bit_depth - 1
    squeezed = (images / 255.0 * max_val).astype(np.uint8)
    return squeezed.astype(np.float32) / max_val
```

**Defensive Combination:**
```python
def sanitize_inputs(images):
    """Apply multiple sanitization techniques"""
    # JPEG compression
    images = apply_jpeg_compression(images, quality=90)
    
    # Feature squeezing
    images = feature_squeezing(images, bit_depth=5)
    
    # Gaussian filtering
    from scipy.ndimage import gaussian_filter
    images = np.array([gaussian_filter(img, sigma=0.5) 
                       for img in images])
    
    return images
```

#### KEY CONCEPTS INTRODUCED
- Input sanitization / Input preprocessing
- Feature squeezing
- JPEG compression defense
- Gaussian filtering
- Defense-in-depth strategy
- Sanitization trade-offs
- Robust adversarial examples
- Adaptive attacks

#### TIMING BREAKDOWN
- Hook (Simple defense concept): 0:00-0:30 (30 sec)
- Sanitization Concept: 0:30-2:00 (90 sec)
- Techniques & Implementation: 2:00-4:00 (120 sec)
- Defense in Depth: 4:00-5:30 (90 sec)
- Deployment Considerations: 5:30-6:45 (75 sec)
- Bridge to Privacy: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "Why does feature squeezing work?" (mechanism understanding)
- IVQ 2: "What are limitations of input sanitization?" (critical thinking)
- IVQ 3: "How would you combine multiple sanitization techniques?" (design)

---

### **Differential Privacy: Protecting Data, Preserving Insight**

**VIDEO TITLE:** Differential Privacy: Protecting Data, Preserving Insight  
**MODULE:** Module 2 - Building the Shield  
**ALIGNED LEARNING OBJECTIVE:** LO2 - Apply defense mechanisms (differential privacy)  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor in professional setting, privacy icons visible
- At 1:15: Privacy paradox visualization
- At 2:30: Differential privacy mechanism explanation with animations
- At 3:45: Noise addition visualization (data distribution before/after)
- At 5:00: Privacy budget (epsilon) explanation with interactive slider
- At 5:45: Utility vs Privacy trade-off curve
- At 6:30: Real-world Apple differential privacy example
- Use visual metaphor: Noise as a privacy blanket
- Color coding: Original data (red) → Noisy data (blue)
- Animations showing mechanism for converting individual records to privatized output

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"Here's a privacy paradox: Apple collects data from millions of iPhones to improve autocomplete. But they promise users complete privacy. Their marketing: 'We don't know what you type. We just know patterns.'

How is that possible? They're collecting data and not seeing the data?

That's differential privacy in action. And it's one of the most elegant mathematical ideas in security. It lets you extract insights from data while guaranteeing that no individual's privacy is violated.

Today, we're diving into how it works. And why it also makes your models more robust to poisoning attacks."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. If you think privacy and security are different problems, today will change your mind. They're deeply connected."

[CORE SECTION 1: THE PRIVACY PROBLEM - 0:45 to 2:15]

"Let's start with a fundamental problem.

You want to build a machine learning model that learns from sensitive data. Maybe medical records. Maybe financial histories. Maybe browsing behavior.

You need this data to train a good model. But the people whose data you're using have a right to privacy. Their individual information should stay private, even if your model is shared publicly.

[VISUAL CUE: Show privacy paradox diagram]

Here's the paradox: if your model is useful, it contains information about the training data. If an attacker has access to your model, they might be able to extract information about individuals in the training set. This is called a 'membership inference attack.'

For example: An attacker queries your model: 'What's the prediction for this profile?' If the model is very confident, the attacker might infer: 'This person was probably in the training data, and they had this specific outcome.'

They've invaded someone's privacy without ever seeing the raw data.

Standard anonymization doesn't solve this. Removing names and IDs isn't enough. An attacker can often re-identify individuals using other attributes. Age, location, medical conditions—these can be enough to identify someone.

The question becomes: how do you train a model on sensitive data while guaranteeing privacy?"

[CORE SECTION 2: HOW DIFFERENTIAL PRIVACY WORKS - 2:15 to 4:30]

"Differential privacy is an elegant mathematical framework. The core idea is deceptively simple: add randomness.

[VISUAL CUE: Show differential privacy mechanism]

Here's how it works:

First: You have a database of individuals' data. Let's say medical records.

Second: You want to compute a statistic from this data. Maybe 'what's the average blood pressure in this dataset?'

Third: Instead of returning the exact answer, you add random noise to the answer before releasing it.

[VISUAL CUE: Animated noise addition]

Why does this provide privacy? Here's the key insight: if you add enough noise, an attacker cannot reliably determine whether any specific individual's data influenced the result.

Think about it this way: Suppose the true average is 120 mmHg, but you release 121 mmHg (with noise added). An attacker doesn't know: Did someone with high blood pressure influence the answer? Or is this just noise?

Now suppose you have two datasets that differ by exactly one person. Dataset A has everyone except Alice. Dataset B has everyone plus Alice.

Differential privacy guarantees: the probability that your model returns the same answer for both datasets is very high. So from the model's output, the attacker can't tell whether Alice was in the dataset.

[SCREEN RECORDING: Show code for differential privacy noise addition]

Here's what this looks like in code:

```python
def differentially_private_query(database, query_function, epsilon):
    # Compute the true result
    true_result = query_function(database)
    
    # Add Laplace noise scaled by epsilon
    noise = np.random.laplace(loc=0, scale=1/epsilon)
    
    # Return noisy result
    return true_result + noise
```

The parameter 'epsilon' controls privacy. Smaller epsilon = more noise = more privacy. Larger epsilon = less noise = more accuracy. It's a privacy budget."

[CORE SECTION 3: PRIVACY BUDGETS AND TRADE-OFFS - 4:30 to 6:00]

"Now, here's where it gets practical: you have to choose your privacy budget.

[VISUAL CUE: Show epsilon scale with examples]

Epsilon = 0.01: Extreme privacy. Almost maximum noise. The result is very noisy. But no one can infer individual data.

Epsilon = 1: Strong privacy. Significant noise. You can still extract insights, but they're fuzzy.

Epsilon = 10: Moderate privacy. Some noise. Most insights survive. Individual privacy is still protected, but less absolutely.

Epsilon = 100+: Weak privacy. Little noise. Results are nearly accurate. But privacy guarantees are weaker.

[VISUAL CUE: Show utility vs privacy trade-off]

This is the trade-off. As you increase epsilon (decrease privacy), you increase utility. Your model gets more accurate. But privacy decreases.

Apple chose an epsilon around 8 for its keyboard intelligence. They prioritized both privacy and utility. The keyboard still learns patterns. But individuals' data is protected.

[SCREEN RECORDING: Show differential privacy model training]

In machine learning, differential privacy is applied during training. There are several approaches:

Approach one: DP-SGD—Differentially Private Stochastic Gradient Descent. You add noise to gradients during backpropagation. This ensures that no single individual's data has too much influence on the model weights.

Approach two: Private Learning—You train on noisy aggregates of data instead of individual records.

Both approaches come with accuracy costs. Your model will be slightly less accurate. But it will be resistant to privacy attacks. And here's the bonus: it's also resistant to data poisoning attacks, because no single training example has too much influence."

[CORE SECTION 4: REAL-WORLD APPLICATION - 6:00 to 6:45]

"Differential privacy isn't theoretical. It's deployed in production systems right now.

Apple uses it in iOS for keyboard predictions, health analytics, and Siri.

Google uses it for Chrome anonymized statistics.

The U.S. Census Bureau used it for the 2020 census to protect individual privacy while still releasing useful demographic statistics.

In each case, the principle is the same: add noise proportional to the sensitivity of the statistic you're computing.

For AI models specifically, companies using differential privacy often report 1-5% accuracy loss compared to standard training. A small price for strong privacy guarantees."

[BRIDGE TO NEXT SECTION - 6:45 to 7:30]

"We've now covered the three core defenses in Module Two:

Adversarial Training: Teaching your model to recognize attacks.

Input Sanitization: Cleaning inputs before they reach your model.

Differential Privacy: Adding noise to data to protect privacy and make poisoning harder.

Each defense is powerful. Each has trade-offs. Together, they form a formidable shield.

But defenses are only as good as you can verify. And that's what Module Three is about: testing. Red teaming. Validation. How do you *know* your defenses work?

That's where we go next."

---

#### TECHNICAL ASSETS
- Privacy paradox visualization diagram
- Membership inference attack example
- Differential privacy mechanism flowchart
- Noise addition before/after comparison
- Epsilon privacy budget scale
- Utility vs Privacy trade-off curve
- DP-SGD algorithm visualization
- Real-world application examples (Apple, Google, Census)
- Jupyter Notebook showing DP implementation
- Accuracy loss vs Privacy gain comparison

#### CODE EXAMPLE
**DP-SGD (Simplified):**
```python
def dp_sgd_step(model, batch, labels, epsilon, delta, 
                clipping_norm=1.0, noise_multiplier=1.0):
    """Single DP-SGD training step"""
    with tf.GradientTape() as tape:
        predictions = model(batch, training=True)
        loss = compute_loss(labels, predictions)
    
    # Compute gradients
    gradients = tape.gradient(loss, model.trainable_variables)
    
    # Clip gradients per example
    clipped_grads = []
    for grad in gradients:
        grad_norm = tf.norm(grad)
        clipped = grad * tf.minimum(1.0, clipping_norm / grad_norm)
        clipped_grads.append(clipped)
    
    # Aggregate and add noise
    sigma = noise_multiplier * clipping_norm / epsilon
    noisy_grads = []
    for clipped in clipped_grads:
        noise = tf.random.normal(shape=clipped.shape, 
                                 mean=0, stddev=sigma)
        noisy_grads.append(clipped + noise)
    
    # Update model
    optimizer.apply_gradients(zip(noisy_grads, 
                                  model.trainable_variables))
    return loss
```

#### KEY CONCEPTS INTRODUCED
- Differential privacy
- Privacy budget (epsilon)
- Laplace mechanism
- Membership inference attacks
- Privacy-utility trade-off
- DP-SGD
- Noise addition
- Privacy as robustness

#### TIMING BREAKDOWN
- Hook (Apple keyboard privacy): 0:00-0:45 (45 sec)
- Privacy Problem: 0:45-2:15 (90 sec)
- DP Mechanism: 2:15-4:30 (135 sec)
- Privacy Budgets: 4:30-6:00 (90 sec)
- Real-world Applications: 6:00-6:45 (45 sec)
- Bridge to Testing: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "What does epsilon control in differential privacy?" (mechanics)
- IVQ 2: "Why does DP make models more robust?" (reasoning)
- IVQ 3: "What's the privacy-utility trade-off in your application?" (applied)

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

**VIDEO TITLE:** Red Team Methodology: Thinking Like an Attacker  
**MODULE:** Module 3 - The AI Security Lifecycle  
**ALIGNED LEARNING OBJECTIVE:** LO3 - Evaluate security measure effectiveness through adversarial testing  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor in professional setting, showing tactical planning
- At 1:00: Red team framework diagram with phases
- At 2:00: Reconnaissance examples visualization
- At 3:30: Exploitation techniques demonstration
- At 4:45: Reporting template and metrics dashboard
- At 5:30: Real-world red team scenario walkthrough
- At 6:15: Lessons learned and improvements made
- Use military/strategic metaphors: Planning → Reconnaissance → Attack → Reporting
- Color progression: Gray (planning) → Orange (testing) → Green (secure)
- Timeline showing attack progression from hypothesis to verification

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"There's a critical moment in product security. You've built your defenses. You've implemented adversarial training. You've added differential privacy. You've hardened your inputs. Everything looks good on paper.

Then you ask one question: Are we actually secure?

And suddenly, you realize: you don't know.

You have no evidence. You've built defenses, but you haven't tested whether they work. Not against a real adversary. Not against someone determined to break your system.

That's the purpose of red teaming. You *become* the attacker. You follow a systematic methodology to find the vulnerabilities your blue team missed. And you report your findings so they can fix them before an actual attacker finds them.

Today, we're teaching you to think like a red team."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. Professional red teams are systematic. They're organized. They follow a methodology. And in this video, I'm going to teach you that methodology."

[CORE SECTION 1: THE RED TEAM FRAMEWORK - 0:45 to 2:30]

"Professional red teams follow a structured framework.

[VISUAL CUE: Show red team framework diagram]

Phase one: Planning and Scoping. Before you attack anything, you plan. You define:

- What's the scope? Are we testing the entire system or specific models?
- What's in bounds? Can we modify the code? The data? The infrastructure?
- What's the threat model? Are we testing against FGSM attacks? PGD attacks? Poisoning? Extraction?
- What are success criteria? If we achieve X, we've found a vulnerability?

This phase prevents wasted effort. You're not just randomly attacking. You're attacking with purpose.

Phase two: Reconnaissance. You study the system without modifying it.

- What's the model architecture?
- What data was it trained on?
- What preprocessing is applied?
- How is it deployed?
- What's the API?

You're building a map of the target.

[VISUAL CUE: Show reconnaissance checklist]

Phase three: Exploitation. You execute your attacks.

- Evasion attacks: Can you fool the model with adversarial inputs?
- Poisoning attacks: Can you corrupt training data?
- Extraction attacks: Can you steal the model?
- Bypass attacks: Can you find edge cases or corner cases?

This is where the actual security testing happens.

Phase four: Reporting. You document everything.

- What vulnerabilities did you find?
- How severe are they?
- How can they be fixed?
- What's the business impact?

This phase is critical. Without clear reporting, findings don't get acted on."

[CORE SECTION 2: PRACTICAL EXECUTION - 2:30 to 4:30]

"Let me walk you through what each phase looks like in practice.

[SCREEN RECORDING: Show red team execution scenario]

Scenario: We're testing a content moderation AI. The system is supposed to flag harmful content and mark it for human review.

Reconnaissance:
- We determine the model classifies content into categories: safe, questionable, harmful.
- We observe that the API returns confidence scores.
- We test with clean content and observe response patterns.
- We identify that the model is a TensorFlow model based on response latency patterns.

Exploitation:
- We generate adversarial examples using PGD attacks, aiming to make harmful content appear safe.
- We submit our adversarial content. Success rate: 40%. The model misclassifies harmful content as safe.
- We try poisoning: we submit thousands of training examples (if we have access) mislabeling harmful content as safe.
- We attempt extraction: we generate queries to build a surrogate model.

[VISUAL CUE: Show attack success rates]

Results:
- Evasion: 40% of carefully crafted harmful content bypasses the filter.
- Poisoning: If an attacker could inject data, they could teach the model to accept harmful content.
- Extraction: We successfully extracted a surrogate model with 92% agreement on our test set.

These findings go into the report."

[CORE SECTION 3: REPORTING AND REMEDIATION - 4:30 to 5:45]

"Professional red teams produce professional reports.

[VISUAL CUE: Show report template]

A good red team report includes:

Executive Summary: What vulnerabilities were found? What's the business impact?

Technical Details: For each vulnerability:
- How does the attack work?
- What are the technical requirements?
- What's the likelihood?
- What's the impact if successfully exploited?

Proof of Concept: If possible, include code or demonstrations showing the vulnerability.

Remediation: For each finding, suggest fixes. Maybe:
- For evasion: Implement stronger adversarial training.
- For poisoning: Add data validation and anomaly detection.
- For extraction: Add differential privacy to limit information leakage.

[VISUAL CUE: Show remediation priority matrix]

Risk Assessment: Prioritize findings.
- Critical: Immediate action required.
- High: Should be fixed before production.
- Medium: Consider for future iterations.
- Low: Monitor, but not urgent.

The key principle: professional red teams present findings in business terms, not just technical terms. They explain: 'This vulnerability could allow attackers to bypass safety filters,' not just 'Model accuracy drops to 40% under adversarial attack.'"

[CORE SECTION 4: CONTINUOUS IMPROVEMENT - 5:45 to 6:45]

"Red teaming isn't a one-time activity.

After you report vulnerabilities and the blue team fixes them, you test again. You verify that fixes actually work. You look for new vulnerabilities introduced by the fixes.

[VISUAL CUE: Show testing cycle]

The cycle:
- Test systems
- Report findings  
- Blue team implements fixes
- Red team verifies fixes
- Repeat

This is continuous improvement. Each iteration makes the system more secure.

In mature security programs, red teaming is an ongoing process. There's a standing red team constantly testing against the latest threats, simulating new attack vectors, and validating defenses.

Organizations like Microsoft, Google, and OpenAI have dedicated red teams. They're not one-time security consultants. They're permanent teams whose job is to be adversaries to their own systems."

[BRIDGE TO METRICS AND LIFECYCLE - 6:45 to 7:30]

"Red teaming produces findings. But how do you know if your security is good enough?

That's where security metrics come in. How do you quantify security? How do you measure whether your defenses are working?

And how do you integrate all of this—attacks, defenses, testing, metrics—into a complete security lifecycle?

In the next videos, we answer these questions. We show you security metrics that matter. We show you how to build a security-focused ML pipeline that continuously validates and improves.

Buckle up. We're entering the operational side of AI security."

---

#### TECHNICAL ASSETS
- Red team framework diagram (4 phases)
- Reconnaissance checklist
- Attack execution flowchart
- Red team report template
- Risk assessment matrix
- Security testing cycle diagram
- Real-world scenario walkthrough
- Vulnerability metrics dashboard
- Remediation progress tracking
- Jupyter Notebook with red team tools

#### CODE EXAMPLE
**Red Team Testing Framework (Pseudocode):**
```python
class RedTeamAssessment:
    def __init__(self, model, threat_model="comprehensive"):
        self.model = model
        self.threat_model = threat_model
        self.findings = []
    
    def reconnaissance(self):
        """Phase 1: Study the target"""
        self.model_info = self._extract_model_info()
        self.data_info = self._analyze_training_data()
        self.api_signature = self._probe_api()
        return self.model_info
    
    def evasion_testing(self):
        """Phase 3a: Test evasion attacks"""
        results = {
            'fgsm': self._test_fgsm(),
            'pgd': self._test_pgd(),
            'carlini_wagner': self._test_carlini_wagner()
        }
        self.findings.append(results)
        return results
    
    def poisoning_testing(self):
        """Phase 3b: Test data poisoning"""
        results = self._attempt_backdoor_insertion()
        self.findings.append(results)
        return results
    
    def extraction_testing(self):
        """Phase 3c: Test model extraction"""
        results = self._attempt_model_stealing()
        self.findings.append(results)
        return results
    
    def generate_report(self):
        """Phase 4: Generate professional report"""
        report = {
            'executive_summary': self._summarize_findings(),
            'technical_details': self._detail_vulnerabilities(),
            'risk_assessment': self._prioritize_findings(),
            'remediation': self._suggest_fixes()
        }
        return report
```

#### KEY CONCEPTS INTRODUCED
- Red team methodology
- Reconnaissance phase
- Exploitation phase
- Professional reporting
- Risk assessment
- Remediation strategies
- Continuous testing
- Security validation

#### TIMING BREAKDOWN
- Hook (Testing problem): 0:00-0:45 (45 sec)
- Framework Overview: 0:45-2:30 (105 sec)
- Practical Execution: 2:30-4:30 (120 sec)
- Reporting: 4:30-5:45 (75 sec)
- Continuous Improvement: 5:45-6:45 (60 sec)
- Bridge to Metrics: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "What are the four phases of red teaming?" (framework)
- IVQ 2: "How would you prioritize vulnerabilities?" (decision-making)
- IVQ 3: "Why is continuous testing important?" (operational thinking)

---

### **Security Metrics and Validation**

**VIDEO TITLE:** Security Metrics and Validation  
**MODULE:** Module 3 - The AI Security Lifecycle  
**ALIGNED LEARNING OBJECTIVE:** LO3 - Evaluate security measure effectiveness  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor reviewing metrics dashboard
- At 1:15: Metrics definition framework displayed
- At 2:30: Notebook showing metric calculations
- At 3:45: Dashboard with real-time metrics
- At 5:00: Acceptance criteria decision tree
- At 5:45: Stakeholder communication examples
- At 6:30: Business impact assessment
- Use visual dashboard: Multiple metrics updated in real-time
- Color coding: Red (unacceptable) → Yellow (review) → Green (acceptable)
- Comparison charts before/after defenses implemented

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"You've tested your model. Your red team found vulnerabilities. You've implemented fixes. Now, the question your executives ask: 'Are we secure enough to deploy?'

And you realize: you don't have a good answer. Because you haven't defined what 'secure enough' means.

Is 90% accuracy under attack good? Is 85%? What about 75%? At what point do you say 'no, this isn't secure enough'?

Without metrics, security becomes subjective. Without metrics, you can't measure progress. You can't convince stakeholders that your defenses are working.

Today, we define security metrics that matter. We show you how to quantify security, set acceptance criteria, and make deployment decisions based on data, not gut feel."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. If you can't measure it, you can't manage it. That's true for security."

[CORE SECTION 1: KEY SECURITY METRICS - 0:45 to 2:30]

"Let's define the metrics that matter.

[VISUAL CUE: Show metrics framework]

First: Robustness metrics. These measure how well your defenses work against attacks.

- Certified Robustness: Under PGD attack with epsilon X, what percentage of inputs does the model classify correctly? This is your 'certified' security level.
- Clean Accuracy: How well does your model perform on unperturbed data? You want this high.
- Accuracy Under Attack: How well does your model perform on adversarial examples? You want this as high as possible.
- Robustness Gap: The difference between clean accuracy and accuracy under attack. Smaller is better.

[VISUAL CUE: Show formulas and example calculations]

Second: Privacy metrics. These measure how well your privacy-preserving defenses work.

- Epsilon (privacy budget): Smaller epsilon means stronger privacy guarantees.
- Membership Inference Attack Success Rate: What percentage of membership inference attacks succeed? You want this low.
- Differential Privacy Guarantee: What's your formal privacy level?

Third: Extraction Resistance.

- Query Efficiency: How many queries does an attacker need to extract the model? More is better.
- Surrogate Model Accuracy: If an attacker extracts your model, how close is their surrogate? Lower is better.
- Time to Extraction: How long does extraction take? Longer is better.

[SCREEN RECORDING: Show notebook calculating metrics]

Here's what calculating these metrics looks like:

```python
def calculate_security_metrics(model, attack_config, test_data):
    metrics = {}
    
    # Clean accuracy
    clean_acc = model.evaluate(test_data)
    metrics['clean_accuracy'] = clean_acc
    
    # Robustness under PGD
    adv_data = pgd_attack(test_data, model, epsilon=0.3)
    robust_acc = model.evaluate(adv_data)
    metrics['robust_accuracy'] = robust_acc
    
    # Robustness gap
    metrics['robustness_gap'] = clean_acc - robust_acc
    
    # Extraction difficulty
    query_count = extraction_attack(model)
    metrics['queries_to_extract'] = query_count
    
    return metrics
```

It's straightforward. You're just measuring performance under different conditions."

[CORE SECTION 2: SETTING ACCEPTANCE CRITERIA - 2:30 to 4:30]

"Now, having metrics is one thing. Using them is another.

You need to define acceptance criteria. Guidelines that say: 'If our metrics meet these thresholds, we can deploy. If they don't, we can't.'

[VISUAL CUE: Show acceptance criteria matrix]

For a content moderation system, your criteria might be:

- Clean Accuracy: Must be ≥ 95%
- Robustness Gap: Must be ≤ 5%
- Certified Robustness (epsilon 0.3): Must be ≥ 85%
- Extraction Query Efficiency: Must be > 10,000 queries

If these criteria are met, deploy. If not, continue iterating.

[VISUAL CUE: Show decision tree]

But acceptance criteria are context-dependent. They depend on:

- Your threat model. Who are you defending against?
- Your risk tolerance. How much security do you need?
- Your performance constraints. How much accuracy can you afford to lose?
- Regulatory requirements. Do you have compliance obligations?

For a high-stakes application like autonomous vehicles, your criteria might be much stricter. For a recommendation system, they might be more lenient.

The key principle: be explicit. Write down your criteria before you finish building. Not after. This prevents rationalization. It prevents deploying systems that don't meet your standards."

[CORE SECTION 3: COMMUNICATING WITH STAKEHOLDERS - 4:30 to 5:45]

"Here's a reality: your executives and product managers don't care about epsilon or robustness gaps. They care about business impact.

So when you communicate metrics, translate them to business language.

[VISUAL CUE: Show communication templates]

Instead of: 'Our model's robustness gap is 8%.'
Say: 'Under realistic adversarial attack, our model is 92% accurate, down from 100% on normal data.'

Instead of: 'Query extraction efficiency is 15,000 queries.'
Say: 'Extracting our model through the API would cost approximately $50,000 and take several weeks.'

Instead of: 'Our privacy budget (epsilon) is 5.'
Say: 'We provide strong privacy protections. An individual's participation in training is nearly undetectable from model outputs.'

[VISUAL CUE: Show dashboard for stakeholders]

Professional security teams use dashboards that translate technical metrics into business metrics.

- Model Security Score (0-100): Aggregated security level
- Risk Level: Green (Low Risk) / Yellow (Moderate Risk) / Red (High Risk)
- Time to Exploit: Estimated time for an attacker to compromise the model
- Business Impact if Compromised: Potential damage from security failure
- Cost of Attack: Approximate cost for attacker
- Recommended Actions: What should we do next?"

[CORE SECTION 4: DEPLOYMENT DECISIONS - 5:45 to 6:45]

"With metrics and acceptance criteria, deployment decisions become systematic.

[VISUAL CUE: Show deployment decision flowchart]

Question one: Do our metrics meet acceptance criteria?
- If yes, proceed.
- If no, don't deploy. Go back to fixing.

Question two: Are we confident in our metrics?
- Do we trust our testing? Have we tested against realistic threats?
- If yes, proceed.
- If no, do more testing first.

Question three: Are there residual risks we're willing to accept?
- No system is perfectly secure. Some risk is always present.
- Have we accepted those risks consciously?
- If yes, proceed.
- If no, implement more defenses.

Question four: Have we planned for ongoing monitoring?
- Deployment isn't the end. It's the beginning.
- After deployment, will we continue to test?
- If yes, proceed.
- If no, don't deploy.

This is a systematic, defensible process. When (not if) a security incident occurs, you can explain: 'We measured security. We set criteria. We met them before deploying. Here's our documentation.'"

[BRIDGE TO COMPLETE LIFECYCLE - 6:45 to 7:30]

"So far, we've covered pieces: attacks, defenses, testing, metrics.

But how do all these pieces fit together? How do you build a complete, ongoing, sustainable security program?

That's the security lifecycle. It's not a one-time process. It's a continuous loop: measure, defend, test, improve, repeat.

In the final video of this course, we show you the complete picture. We show you how to integrate everything you've learned into a production AI security program.

Let's do this."

---

#### TECHNICAL ASSETS
- Security metrics framework diagram
- Metric calculation formulas
- Acceptance criteria matrix
- Dashboard showing real-time metrics
- Decision tree for deployment
- Business translation examples
- Risk assessment matrix
- Jupyter Notebook with metric calculations
- Stakeholder communication templates
- Before/after comparison charts

#### CODE EXAMPLE
**Security Metrics Calculator:**
```python
class SecurityMetricsCalculator:
    def __init__(self, model, test_data):
        self.model = model
        self.test_data = test_data
    
    def clean_accuracy(self):
        """Baseline accuracy on clean data"""
        correct = 0
        for x, y in self.test_data:
            pred = np.argmax(self.model.predict(x))
            if pred == y:
                correct += 1
        return correct / len(self.test_data)
    
    def robustness_accuracy(self, epsilon, attack='pgd'):
        """Accuracy under adversarial attack"""
        adversarial_data = generate_adversarial_batch(
            self.test_data, self.model, epsilon, attack)
        return self.evaluate_on_data(adversarial_data)
    
    def robustness_gap(self, epsilon):
        """Difference between clean and robust accuracy"""
        clean = self.clean_accuracy()
        robust = self.robustness_accuracy(epsilon)
        return clean - robust
    
    def generate_report(self):
        """Generate security metrics report"""
        return {
            'clean_accuracy': self.clean_accuracy(),
            'robustness_0.1': self.robustness_accuracy(0.1),
            'robustness_0.3': self.robustness_accuracy(0.3),
            'gap_0.3': self.robustness_gap(0.3),
            'timestamp': datetime.now()
        }
```

#### KEY CONCEPTS INTRODUCED
- Security metrics definition
- Robustness metrics
- Privacy metrics
- Extraction resistance metrics
- Acceptance criteria
- Deployment decision-making
- Stakeholder communication
- Business translation

#### TIMING BREAKDOWN
- Hook (Define secure): 0:00-0:45 (45 sec)
- Key Metrics: 0:45-2:30 (105 sec)
- Acceptance Criteria: 2:30-4:30 (120 sec)
- Stakeholder Communication: 4:30-5:45 (75 sec)
- Deployment Decisions: 5:45-6:45 (60 sec)
- Bridge to Lifecycle: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "What metrics would you use to measure model security?" (definition)
- IVQ 2: "How would you set acceptance criteria?" (practical)
- IVQ 3: "How would you explain security to executives?" (communication)

---

### **The Complete Security Lifecycle**

**VIDEO TITLE:** The Complete Security Lifecycle: From Design to Deployment and Beyond  
**MODULE:** Module 3 - The AI Security Lifecycle  
**ALIGNED LEARNING OBJECTIVE:** LO3 - Comprehensive security lifecycle integration  
**TARGET DURATION:** 7.5 minutes  
**FORMAT:** Talking Head + Demonstration  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor showing ML pipeline
- At 1:15: Security lifecycle diagram overlay on pipeline
- At 2:30: Design phase security checklist
- At 3:45: Development phase integration screenshot
- At 4:30: Testing and validation phase demo
- At 5:15: Deployment and monitoring dashboard
- At 6:00: Real-world incident response example
- Use circular flow visualization: Design → Dev → Test → Deploy → Monitor → Update
- Animations showing feedback loops and continuous improvement
- Color coding: Planning (blue) → Implementation (green) → Testing (orange) → Production (red)
- Timeline showing security activities across model lifecycle

#### SCRIPT (Approximately 1,050 words)

[HOOK - 0:00 to 0:45]

"There's a common misconception about security. People think it's a checkpoint. You get to a certain point in your project, you run a security audit, you check a box, and then you're done.

That's not how it works. That's like thinking you can exercise once in a lifetime and then be healthy forever.

Security is a process. It's a continuous cycle that runs parallel to everything else you do. It starts before you write a single line of code. It continues after deployment. It never stops.

Today, we're showing you the complete security lifecycle. Not as a one-time activity. As an integrated part of how you build and maintain AI systems."

[TRANSITION - 0:45]

"I'm Rifat Erdem Sahin. If you take nothing else from this course, take this: security done right isn't a tax on development. It's integral to development."

[CORE SECTION 1: THE PHASES OF THE LIFECYCLE - 0:45 to 2:30]

"The AI security lifecycle has five phases.

[VISUAL CUE: Show lifecycle diagram]

Phase One: Design and Threat Modeling. Before you build anything, you think about security.

- What's your threat model? Who are your adversaries?
- What would successful attacks look like?
- What's your risk tolerance?
- What are your security requirements?

At this phase, you're answering questions, not building solutions. You're designing with security in mind.

[VISUAL CUE: Show threat modeling checklist]

Checklist: Have you identified potential attacks? Have you defined acceptable risk levels? Have you planned for privacy requirements?

Phase Two: Development and Integration. You're building your model. But you're building it with security built-in.

- Are you using secure data pipelines?
- Are you logging decisions for audit trails?
- Are you implementing defenses during training?
- Are you hardening your code?

[VISUAL CUE: Show development security practices]

Phase Three: Testing and Validation. You're red teaming your system. You're trying to break it.

- Do your defenses actually work?
- Did you test all the attacks we discussed?
- Have you measured your security metrics?
- Do you meet your acceptance criteria?

Phase Four: Deployment and Monitoring. Your model is in production. But security doesn't stop.

- Are you monitoring for suspicious patterns?
- Are you tracking model performance and security metrics?
- Are you ready to respond if something goes wrong?
- Do you have a rollback plan?

Phase Five: Incident Response and Improvement. If a security incident occurs (and statistically, it will), how do you respond?

- How do you detect the problem?
- How do you contain it?
- How do you remediate?
- How do you prevent recurrence?

[VISUAL CUE: Show feedback loop back to design]

Then you loop back. You analyze what happened, you update your threat model, and you start the cycle again with what you've learned."

[CORE SECTION 2: PRACTICAL IMPLEMENTATION - 2:30 to 4:30]

"Let me show you what this looks like in practice.

[VISUAL CUE: Show ML pipeline with security checkpoints]

Traditional ML pipeline: Data → Preprocessing → Training → Validation → Deployment

Security-enhanced pipeline: Data (with validation) → Preprocessing (with sanitization) → Training (with adversarial examples) → Validation (with red team testing) → Deployment (with monitoring)

Notice the additions. At every stage, security considerations are built in.

[SCREEN RECORDING: Show version control with security annotations]

Here's what your repository might look like:

- Data directory: Contains data validation scripts. Are we catching poisoned data?
- Models directory: Contains model definitions. Are we using adversarial training?
- Tests directory: Contains security tests. Are we testing evasion? Extraction?
- Deployment directory: Contains monitoring code. Are we tracking security metrics in production?
- Documentation: Security threat model. Acceptance criteria. Incident response procedures.

[VISUAL CUE: Show CI/CD pipeline with security gates]

Your CI/CD pipeline includes security checks:

1. Code check: Does this code follow security best practices?
2. Data check: Is the training data clean?
3. Model check: Does the model meet our security acceptance criteria?
4. Security test: Do adversarial attacks pass at expected rates?
5. Deployment: Only if all checks pass, deploy.

If any security check fails, the deployment is blocked. Manual review is required. You don't accidentally deploy insecure models."

[CORE SECTION 3: MONITORING AND INCIDENT RESPONSE - 4:30 to 5:45]

"Deployment is not the end. It's the middle of the story.

After deployment, you're monitoring continuously.

[VISUAL CUE: Show production monitoring dashboard]

What are you tracking?

- Model Performance: Accuracy, precision, recall. Are normal metrics changing?
- Security Metrics: Robustness, privacy, extraction resistance. Are they holding?
- Input Patterns: Are we seeing unusual inputs? Patterns that might indicate attacks?
- User Feedback: Are users reporting issues?

If something seems wrong, you escalate.

[VISUAL CUE: Show incident response flowchart]

Incident Response:

1. Detection: Monitoring alerts that something is wrong. Maybe accuracy dropped. Maybe we're seeing suspicious query patterns. Maybe we detected an extraction attempt.

2. Analysis: What happened? Is this a real security incident or a false alarm?

3. Containment: If it's real, limit the damage. Maybe you disable the model. Maybe you serve a different version.

4. Investigation: Root cause analysis. How did this happen? Was it an attack? Was it a deployment mistake?

5. Remediation: Fix the issue. Maybe you retrain. Maybe you add new defenses. Maybe you deploy a patched version.

6. Communication: Tell stakeholders what happened. What was the impact? What are you doing about it?

[VISUAL CUE: Show postmortem document]

Post-Incident: You write a postmortem. You analyze what went wrong. You update your threat model. You build defenses to prevent this from happening again.

This incident becomes a learning opportunity for your entire team."

[CORE SECTION 4: CONTINUOUS IMPROVEMENT - 5:45 to 6:45]

"Here's what makes this lifecycle sustainable: continuous improvement.

Each time you go through the cycle, you get better. You identify new threats. You implement better defenses. You measure security more carefully.

After a year of running this cycle, your security posture is dramatically better than it was on day one. Not because you got lucky. Because you systematized it. Because you made it continuous.

[VISUAL CUE: Show long-term security trend]

Look at this graph. This is a company's security metrics over two years.

- Month 1-3: They implement initial defenses. Robustness improves from 60% to 75%.
- Month 4-6: They encounter their first incident. They respond quickly. Security improves to 80%.
- Month 7-9: They implement differential privacy. Privacy metrics improve significantly.
- Month 10-12: Continued monitoring and small improvements. Robustness reaches 88%.
- Month 13-24: They've added new attack vectors to their threat model. They've improved their red teaming. They're now at 92% robustness, with strong privacy guarantees.

This isn't rocket science. It's discipline. It's commitment. It's treating security as a continuous process, not a checkpoint."

[BRIDGE TO COURSE CONCLUSION - 6:45 to 7:30]

"We've now covered the entire AI security lifecycle.

We started with attacks: evasion, poisoning, extraction. The ways your model can be broken.

We covered defenses: adversarial training, input sanitization, differential privacy. The ways you protect your model.

We covered testing: red teaming, metrics, validation. The ways you verify that your defenses work.

And now, we've covered the lifecycle: the organizational structure that makes security continuous.

But knowledge isn't action. The real challenge starts now. When you go back to your own projects, you need to make security part of your culture. Part of your process. Part of how you build.

That's hard. That's why we have the labs and the practical exercises that follow this video series. Use them. Apply them to real models. Build the muscle memory of secure AI development.

The future of AI security depends on people like you. People who understand that security is not optional. People who integrate it from day one. People who measure it. People who improve it continuously.

Thank you for joining me on this journey. Now go build secure AI."

---

#### TECHNICAL ASSETS
- Complete lifecycle diagram
- Threat modeling checklist
- ML pipeline with security checkpoints
- CI/CD pipeline visualization
- Security testing automation diagram
- Production monitoring dashboard
- Incident response flowchart
- Postmortem template
- Long-term security trend graph
- Real-world incident case study
- Team structure for security (red team, blue team, security engineers)

#### CODE EXAMPLE
**Security-Enhanced ML Pipeline (Pseudocode):**
```python
class SecureMLPipeline:
    def __init__(self, threat_model, acceptance_criteria):
        self.threat_model = threat_model
        self.acceptance_criteria = acceptance_criteria
        self.security_metrics = {}
    
    def design_phase(self):
        """Phase 1: Threat modeling and design"""
        return {
            'threats_identified': self.threat_model,
            'risk_assessment': self._assess_risks(),
            'defense_requirements': self._define_defenses()
        }
    
    def development_phase(self):
        """Phase 2: Secure development"""
        # Use adversarial training
        self.model = self._train_with_adversarial_examples()
        
        # Validate data
        self._validate_training_data()
        
        # Log model decisions
        self._setup_audit_logging()
    
    def testing_phase(self):
        """Phase 3: Security testing"""
        self.security_metrics = {
            'evasion_robustness': self._test_evasion(),
            'poisoning_resistance': self._test_poisoning(),
            'extraction_difficulty': self._test_extraction(),
            'privacy_level': self._test_privacy()
        }
        
        # Check acceptance criteria
        if not self._meets_criteria():
            raise SecurityException("Metrics don't meet acceptance criteria")
        
        return self.security_metrics
    
    def deployment_phase(self):
        """Phase 4: Secure deployment"""
        self._setup_monitoring()
        self._deploy_with_gradual_rollout()
        self._establish_incident_response()
    
    def monitoring_phase(self):
        """Phase 5: Continuous monitoring"""
        while True:
            metrics = self._collect_metrics()
            if self._anomaly_detected(metrics):
                self._escalate_incident()
            time.sleep(monitoring_interval)
    
    def _meets_criteria(self):
        """Check if metrics meet acceptance criteria"""
        for metric, threshold in self.acceptance_criteria.items():
            if self.security_metrics[metric] < threshold:
                return False
        return True
```

#### KEY CONCEPTS INTRODUCED
- Complete security lifecycle
- Threat modeling
- Secure development practices
- Security testing integration
- Production monitoring
- Incident response
- Continuous improvement
- Security culture

#### TIMELINE BREAKDOWN
- Hook (Security misconception): 0:00-0:45 (45 sec)
- Lifecycle Phases: 0:45-2:30 (105 sec)
- Practical Implementation: 2:30-4:30 (120 sec)
- Monitoring & Response: 4:30-5:45 (75 sec)
- Continuous Improvement: 5:45-6:45 (60 sec)
- Course Conclusion: 6:45-7:30 (45 sec)

#### ASSESSMENT ALIGNMENT
- IVQ 1: "What are the five phases of the security lifecycle?" (comprehensive)
- IVQ 2: "Why is continuous monitoring important?" (operational)
- IVQ 3: "How would you respond to a security incident?" (applied)

---

### **Red Team Security Audit**

**PRACTICE ASSIGNMENT TITLE:** Red Team Security Audit  
**MODULE:** Module 3 - The AI Security Lifecycle  
**ALIGNED LEARNING OBJECTIVE:** LO3 - Evaluate security measure effectiveness through simulated adversarial attacks  
**FORMAT:** Hands-On Lab (Jupyter Notebook / Google Colab)  
**DIFFICULTY LEVEL:** Intermediate  
**ESTIMATED COMPLETION TIME:** 60-90 minutes  

---

#### LAB OVERVIEW

**Scenario Context:**
You are the Lead Security Analyst for SynthSafe Corporation. Your team has developed a next-generation content moderation AI that flags harmful images with 96% accuracy. The system is scheduled for production deployment in 48 hours, but leadership has assigned you one final task: conduct a comprehensive red team security audit. You must validate the model's resilience against sophisticated attacks and provide a go/no-go recommendation.

**Your Mission:**
Test the content moderation model against three critical threat vectors:
1. **Evasion Attacks** - Can adversarial perturbations bypass the safety filter?
2. **Data Poisoning** - Can backdoors be implanted to cause misclassification?
3. **Model Extraction** - Can the model's functionality be stolen via queries?

Your audit findings must include quantitative metrics, specific vulnerabilities discovered, and remediation recommendations.

---

#### LAB STRUCTURE

**Part 1: Environment Setup & Model Loading (10 minutes)**

Learners will:
- Load the pre-trained content moderation model (pre-deployed for the audit)
- Familiarize themselves with the model's API interface
- Establish baseline performance metrics (clean accuracy, inference time)
- Review the acceptance criteria for security metrics

**Part 2: Evasion Attack Testing (25 minutes)**

Learners will:
- Implement PGD (Projected Gradient Descent) attacks - a stronger variant of FGSM
- Generate adversarial examples with varying perturbation budgets
- Measure robustness degradation as epsilon increases
- Document the epsilon threshold where accuracy drops below acceptable levels
- Interpret results: "At what perturbation magnitude does our defense fail?"

**Sample Code Structure:**
```python
# Load audit scenario
audit_model = load_model('content_moderation_v1.h5')
test_dataset = load_audit_dataset('harmful_images_test.npy')

# Part 1: Baseline Performance
baseline_accuracy = evaluate_clean_accuracy(audit_model, test_dataset)
print(f"Clean Accuracy: {baseline_accuracy:.2%}")

# Part 2: Run PGD Attack
adversarial_images = pgd_attack(
    model=audit_model,
    images=test_dataset,
    labels=true_labels,
    epsilon=8/255,  # perturbation budget
    alpha=2/255,    # step size
    num_iterations=7
)

# Measure robustness
attacked_accuracy = evaluate_accuracy(audit_model, adversarial_images)
robustness_loss = baseline_accuracy - attacked_accuracy
print(f"Accuracy Under Attack: {attacked_accuracy:.2%}")
print(f"Robustness Loss: {robustness_loss:.2%}")
```

**Part 3: Data Poisoning Detection (25 minutes)**

Learners will:
- Analyze the model's decision patterns on benign vs backdoored inputs
- Create a trigger pattern detector (statistical analysis of activation patterns)
- Measure the model's susceptibility to trigger activation
- Identify false positive rates on clean data
- Document findings: "Does the model contain hidden triggers? How reliably can they activate?"

**Sample Code Structure:**
```python
# Test for backdoor susceptibility
trigger_pattern = load_trigger_pattern('adversarial_trigger.npy')

# Create backdoored images
backdoored_images = inject_trigger(test_dataset, trigger_pattern)

# Measure trigger effectiveness
baseline_preds = audit_model.predict(test_dataset[:100])
triggered_preds = audit_model.predict(backdoored_images[:100])

trigger_effectiveness = (triggered_preds != baseline_preds).mean()
print(f"Trigger Activation Rate: {trigger_effectiveness:.2%}")

# Verify no false positives on clean data
clean_stability = (audit_model.predict(test_dataset) == baseline_preds).mean()
print(f"Clean Data Stability: {clean_stability:.2%}")
```

**Part 4: Model Extraction Testing (20 minutes)**

Learners will:
- Query the model strategically to build a surrogate model
- Measure query efficiency (how many queries needed for 90% agreement?)
- Calculate extraction cost vs model value
- Assess intellectual property vulnerability
- Document findings: "How easily can someone clone our model?"

**Sample Code Structure:**
```python
# Query-based extraction
query_budget = 1000
query_count = 0
surrogate_data = []

while query_count < query_budget:
    random_image = generate_random_image()
    victim_pred = audit_model.predict([random_image])[0]
    surrogate_data.append((random_image, victim_pred))
    query_count += 1

# Train surrogate on collected data
surrogate_model = train_surrogate_model(surrogate_data)

# Measure extraction success
victim_accuracy = evaluate_accuracy(audit_model, test_dataset)
surrogate_accuracy = evaluate_accuracy(surrogate_model, test_dataset)
agreement_rate = measure_prediction_agreement(audit_model, surrogate_model, test_dataset)

print(f"Surrogate Agreement Rate: {agreement_rate:.2%}")
print(f"Extraction Efficiency: {surrogate_accuracy / victim_accuracy:.2%}")
```

---

#### DELIVERABLES

Learners must submit:

**1. Security Audit Report (Written, ~500 words)**
- Executive summary (security posture: PASS/FAIL)
- Detailed findings for each attack vector
- Quantitative metrics with charts
- Risk ratings: Critical / High / Medium / Low
- Remediation recommendations

**2. Jupyter Notebook with Annotated Results**
- All code used in the audit
- Output metrics and visualizations
- Interpretation of findings
- Comments explaining what each section demonstrates

**3. Decision Recommendation**
- Go/No-Go decision for production deployment
- Conditional go (if specific defenses are implemented)
- Timeline for remediation if "no-go"

---

#### ACCEPTANCE CRITERIA

**For PASS rating, model must meet ALL criteria:**
- Evasion robustness: ≥85% accuracy at epsilon=8/255 (PGD attack)
- Backdoor resistance: Trigger activation rate <5% on benign data
- Model extraction resistance: Surrogate agreement <75% with 1000 queries
- No critical vulnerabilities discovered

**For CONDITIONAL PASS:**
- One metric fails, but remediable through additional adversarial training or input sanitization

**For FAIL:**
- Multiple critical vulnerabilities; deployment should be delayed pending security improvements

---

#### LEARNING OUTCOMES

Upon completing this lab, learners will:
- ✅ Design and execute systematic security tests
- ✅ Interpret adversarial robustness metrics quantitatively
- ✅ Identify specific model vulnerabilities through empirical testing
- ✅ Make evidence-based deployment recommendations
- ✅ Communicate security findings to technical and non-technical stakeholders

---

#### INSTRUCTOR NOTES

- Pre-load the model to avoid long setup times
- Provide the audit dataset (200 representative images)
- Consider a leaderboard: whose audit finds the most vulnerabilities?
- This lab directly simulates how Microsoft, OpenAI, and other major AI organizations conduct security reviews before production deployment
- Real-world audit budgets are often larger; this exercise shows how constraints drive methodology decisions

---

### **Microsoft's AI Red Team is Building a Safer Future for AI**

**READING TITLE:** How Professional Red Teams Validate AI Security  
**MODULE:** Module 3 - The AI Security Lifecycle  
**DIFFICULTY LEVEL:** Intermediate  
**READING FORMAT:** Comprehensive Case Study + Methodology Guide  
**ESTIMATED READING TIME:** 15-20 minutes  

---

#### READING INTRODUCTION

In 2023, Microsoft published groundbreaking research revealing their red teaming methodology for large language models and AI systems. This case study demonstrates how industry-leading organizations systematically validate AI security before production deployment. Unlike the academic labs where you've been testing models, real-world red teams operate under constraints: budget limitations, time pressures, and the need to balance security with functionality. This reading explores Microsoft's framework and shows how to apply it to your own AI systems.

---

#### KEY CONCEPTS: PROFESSIONAL RED TEAMING

**1. Structured Threat Modeling**

Professional red teams don't attack randomly. They start with systematic threat modeling:

- **Threat Identification**: What are the realistic attacks? Evasion? Poisoning? Extraction? Social engineering?
- **Attack Surfaces**: Which interfaces are vulnerable? APIs? Training pipelines? User inputs?
- **Attacker Profiles**: What resources do realistic attackers have? Script kiddies? Well-funded organizations? State actors?
- **Impact Assessment**: What's the damage from each attack? Financial loss? Privacy breach? Safety risk?

Microsoft's threat model for their GPT-4 deployment included:
- Adversarial prompts designed to bypass safety filters
- Injection attacks exploiting system prompts
- Data extraction attacks targeting training information
- Misuse scenarios (fraud, harassment, illegal content generation)

**2. Attack Surface Prioritization**

With unlimited time and budget, you could test everything. In reality, you need to prioritize:

- **High-impact + High-probability attacks** → test first
- **High-impact + Medium-probability attacks** → test second
- **Low-impact attacks** → deprioritize or use automated scanning

Microsoft found that adversarial prompts (attacks that require no technical expertise) were higher priority than sophisticated model extraction attempts.

**3. Coordinated Vulnerability Disclosure**

Once vulnerabilities are found:

- **Severity Classification**: Critical (immediate risk) vs High (serious but managed) vs Medium (should fix) vs Low (nice to fix)
- **Responsible Disclosure**: Give the team time to fix before public announcement (typically 90 days)
- **Stakeholder Communication**: Security findings must reach both engineers and leadership
- **Remediation Tracking**: Monitor fix implementation and retest after patches

---

#### MICROSOFT'S FIVE-PHASE RED TEAM FRAMEWORK

**Phase 1: Planning & Scoping**
- Define threat model (what are we protecting against?)
- Set success metrics (what does "secure enough" mean?)
- Allocate resources (budget, time, team size)
- Establish acceptance criteria (when can we deploy?)

*Real-world example:* Microsoft allocated 3 months and a team of 15 security researchers for GPT-4's initial red team. They defined 12 attack categories as in-scope, 8 categories as out-of-scope (for a future phase).

**Phase 2: Reconnaissance & Analysis**
- Study the model's capabilities and limitations
- Review training data composition (what might have been in training?)
- Test known attack vectors from academic literature
- Look for patterns in model behavior that might indicate vulnerabilities

*Real-world example:* Microsoft's team tested 1,000+ adversarial prompts to understand failure patterns. They found that the model was more vulnerable to multi-turn conversations that gradually pushed boundaries.

**Phase 3: Exploitation & Testing**
- Actively attempt attacks against the system
- Document each successful attack with reproducible proof-of-concept
- Measure attack success rates and severity
- Iterate: learn from failures and refine attacks

*Real-world example:* When basic adversarial prompts didn't work, Microsoft's red team tried indirect approaches: asking the model to role-play characters that would perform harmful actions, using historical examples to establish "precedent," framing harmful requests as academic thought experiments.

**Phase 4: Reporting & Prioritization**
- Compile findings into a detailed security report
- Classify vulnerabilities by severity and exploitability
- Recommend mitigations (training, filtering, monitoring)
- Communicate findings to stakeholders in actionable terms

*Real-world example:* Microsoft's report categorized 50+ vulnerabilities into:
- 5 "critical" (immediate action required)
- 12 "high" (fix before deployment)
- 20 "medium" (backlog items)
- 13 "low" (monitor and reassess)

**Phase 5: Continuous Monitoring & Iteration**
- Deploy with monitoring systems to detect new attack patterns in production
- Collect adversarial examples from users (with privacy protection)
- Regularly re-run red team exercises on updated models
- Share learnings with broader research community

*Real-world example:* Microsoft implemented continuous monitoring for GPT-4 in production. When users discovered new attack vectors, the team collected anonymized examples (with user consent) and incorporated them into the next red team cycle.

---

#### APPLYING MICROSOFT'S FRAMEWORK TO YOUR SYSTEMS

**For Small Teams (Under-resourced situation):**
1. **Start focused**: Pick 2-3 attack vectors, not all
2. **Use automation**: Automated adversarial prompt generation, fuzzing tools
3. **Leverage community**: Bug bounty programs, external red teams
4. **Iterate rapidly**: Multiple short sprints rather than one long audit

**For Resource-Constrained Scenarios:**
1. **Threat model ruthlessly**: Accept that you can't test everything; be strategic
2. **Prioritize by risk**: Test what matters most for your business
3. **Use baselines**: Start with known attacks (FGSM, PGD, basic poisoning) before custom attacks
4. **Document assumptions**: Record what you tested and what you intentionally skipped

**For Scaling Red Teams:**
1. **Build reusable tools**: Shared attack libraries, metric dashboards, reporting templates
2. **Create playbooks**: Standard procedures for testing common model types
3. **Enable junior testers**: Clear methodology so non-experts can follow it
4. **Continuous feedback**: Regular team debriefs to improve methodology over time

---

#### MEASURING RED TEAM EFFECTIVENESS

How do you know your red team exercise was thorough?

**Metric 1: Attack Coverage**
- Did you test representative attacks from all threat categories?
- Example: For vision models, did you test evasion (FGSM, PGD), poisoning, extraction, and out-of-distribution inputs?

**Metric 2: Severity Distribution**
- What percentage of found vulnerabilities were critical vs high vs medium vs low?
- Industry baseline: ~10% critical, ~20% high, ~40% medium, ~30% low
- If you find zero critical, you either did excellent work or didn't dig deep enough

**Metric 3: Reproducibility**
- Can someone else reproduce each finding using your documentation?
- If findings aren't reproducible, they're not credible to engineers

**Metric 4: Remediation Time**
- How long did it take to fix vulnerabilities after discovery?
- Healthy organization: Critical fixes in <1 week, High in <2 weeks, Medium in <1 month
- If fixes take months, it indicates deeper organizational issues

---

#### KEY TAKEAWAYS FROM MICROSOFT'S APPROACH

1. **Red teaming is not about finding every vulnerability**. It's about systematically finding the vulnerabilities that matter for your deployment context.

2. **Threat modeling comes first**. You can't properly red team without understanding what you're actually defending against.

3. **Continuous iteration beats one-time audits**. A single red team exercise gives you a snapshot. Ongoing monitoring + regular re-testing gives you confidence.

4. **Document everything**. Each found vulnerability should be reproducible, measurable, and traceable to impact.

5. **Red teaming is a team sport**. Effective red teams include security researchers, engineers, domain experts, and operations teams.

6. **Share learnings, not just findings**. The methodology and frameworks are as valuable as the specific vulnerabilities discovered.

---

#### DISCUSSION QUESTIONS

After reading this case study, consider:

1. **For your own project**: What would be your top 5 vulnerabilities to prioritize testing? Why those?

2. **Resource constraints**: If you had only 1 week and 1 engineer to red team your model, what would you focus on?

3. **Stakeholder communication**: How would you explain a "medium severity" vulnerability to a non-technical product manager?

4. **Continuous improvement**: After deploying a model, what monitoring systems would give you the earliest signal of a security issue?

---

#### FURTHER READING & RESOURCES

- Microsoft Red Team Report on LLM Safety: "Evaluating the Safety of Large Language Models" (2023)
- OpenAI's Bug Bounty Program: Case studies of real-world findings
- NIST AI Risk Management Framework: Formal risk assessment methodology
- Adversarial ML Red Team Playbook: Specific attack techniques and defenses

---

### **Course Wrap Up**

**VIDEO TITLE:** The Road Ahead: Your Next Steps in AI Security  
**MODULE:** Course Conclusion  
**ALIGNED LEARNING OBJECTIVE:** Synthesis of LO1, LO2, and LO3  
**TARGET DURATION:** 5 minutes  
**FORMAT:** Talking Head + Montage  
**DIFFICULTY LEVEL:** Intermediate  

---

#### PRODUCTION NOTES
- Open with instructor in professional setting
- At 0:30: Transition to quick montage showing all three modules (10-second highlight reel)
- At 1:00: Return to instructor full screen
- At 2:15: Show certificate of completion design (mock-up)
- At 3:00: Transition to resource library visual (books, documentation, GitHub repos)
- At 3:45: Final CTA with course roadmap showing how this connects to advanced courses
- End with forward-looking motivation sequence
- Use calm, reflective music in background (not distracting)

#### SCRIPT (Approximately 700 words)

[HOOK - 0:00 to 0:30]

"You made it. Seventy minutes ago, you started this course asking a simple question: how do I build AI that's not just accurate, but actually secure? By now, you've seen attacks that would make most data scientists uncomfortable. You've built defenses. You've measured security rigorously. And you've learned that the most important thing isn't a perfect score on a test—it's resilience when something goes wrong.

That's a fundamental shift in how you think about machine learning."

[MONTAGE - 0:30 to 1:00]

[Quick cuts showing]:
- Stop sign with adversarial stickers
- Training loop visualization from Module 1
- Adversarial training animation from Module 2
- Red team testing dashboard from Module 3
- Return to instructor

[TRANSITION - 1:00]

"Over this course, we've covered three critical pillars of AI security."

[CORE SECTION 1: RECAP & SYNTHESIS - 1:00 to 3:00]

"**Module One: Understanding Attacks**

You learned that attackers don't think like engineers. They think like economists. They ask: 'What's the minimum effort to break this?' Evasion attacks showed you that 99% accuracy is meaningless against adversarial inputs. Data poisoning revealed that trust in your training data can be weaponized. Model extraction demonstrated that your intellectual property can be stolen through a simple API.

The core insight: attackers only need to be right once. You need to be right every single time.

[VISUAL CUE: Show brief clips of attack demonstrations]

**Module Two: Building Defenses**

Then you learned something equally important: defense is possible. Adversarial training makes models robust by inoculating them against attack. Input sanitization provides immediate protection with simple, proven techniques. Differential privacy lets you use sensitive data without privacy-shaming yourself.

But—and this is critical—there's no silver bullet. These defenses work together, not separately. Adversarial training without input sanitization leaves holes. Differential privacy without adversarial training sacrifices robustness. The principle is defense in depth: multiple overlapping protections.

[VISUAL CUE: Show defense architecture diagram]

**Module Three: The Security Lifecycle**

Finally, you learned that security isn't a destination. It's a direction. A commitment. You tested models systematically using red team methodologies. You established metrics that mean something to stakeholders. And you learned that the most important thing you can do after deployment is watch, listen, and adapt.

[VISUAL CUE: Show security lifecycle diagram - emphasizing the continuous loop]

The professionals you studied—Microsoft, OpenAI, other leading organizations—don't do security once and call it done. They do it perpetually."

[BRIDGE SECTION - 3:00 to 3:45]

"So what's next?

[VISUAL CUE: Show certificate of completion]

First: you've earned this certificate. That's not a trophy. It's a credential. It means you understand AI security at a level that's still relatively rare. You can speak credibly about threat models. You can spot vulnerabilities. You can design defenses.

[TRANSITION]

But certification is just permission to go deeper.

[VISUAL CUE: Show resource library: books, code repos, papers, tools]

The field of adversarial machine learning is evolving monthly. New attacks appear. New defenses emerge. My recommendations:

**Stay Current:**
- Follow adversarial ML research. The Adversarial Robustness Toolbox, CleverHans, and TextAttack are maintained actively.
- Read papers from major AI safety groups: Anthropic, OpenAI, DeepMind, Hugging Face.
- Participate in red teaming communities. OpenAI, Google, Meta all run ongoing bug bounties.

**Build Hands-On Experience:**
- Take this knowledge to real projects. Security is learned by doing, not just watching videos.
- Contribute to open-source security tools. Your perspective is valuable.
- Participate in competitions: adversarial robustness challenges on Kaggle, ML security competitions.

**Connect Security to Your Domain:**
- If you're in healthcare: understand how adversarial perturbations could misdiagnose disease.
- If you're in finance: model the impact of extraction attacks on trading algorithms.
- If you're in autonomous systems: model attacks on perception systems with safety consequences.
- Security isn't abstract. It's concrete. It lives in your domain.

**Think Systemically:**
- Security is a property of the *entire system*, not just the ML model.
- Your defenses are only as strong as your data pipeline, your model serving, your monitoring systems.
- The best attack isn't always technical. It's organizational. It's social. Stay alert."

[FINAL SECTION: FORWARD MOMENTUM - 3:45 to 5:00]

"Here's what I want you to remember.

The paradox you came in with—accurate models can still be insecure—that paradox is now your superpower. While most ML engineers chase accuracy scores, you're thinking about robustness. While they're deploying models, you're thinking about what could go wrong. While they're hoping for security, you're building it intentionally.

[PAUSE]

That mindset—security as a first-class design concern, not an afterthought—that's what separates organizations that get breached from organizations that don't.

[VISUAL CUE: Show montage of real-world AI applications (autonomous vehicles, healthcare, financial systems, content moderation) - emphasizing stakes]

Every model you build will be attacked. Some attacks you'll see coming. Others you won't. Your job isn't to prevent every attack—that's impossible. Your job is to:

1. **Understand the threats** - which you now do.
2. **Design thoughtfully** - layered defenses that reinforce each other.
3. **Test ruthlessly** - red teaming, metric validation, edge case hunting.
4. **Monitor relentlessly** - because the work doesn't end at deployment.
5. **Learn continuously** - when something breaks, understand why and improve.

That's professionalism in AI security.

[FINAL CTA - 4:45 to 5:00]

[VISUAL CUE: Show course completion card with next recommended courses]

This is just the beginning. Advanced topics await: certified robustness, formal verification of neural networks, adversarial training at scale, privacy-preserving machine learning, and much more.

But before you move forward: look back at where you started. You came in thinking security was someone else's problem. Now you know it's *your* problem. Own it.

The field needs more people thinking like you think now.

Thank you for taking this course. Build secure AI. The world is counting on you."

[FADE TO BLACK - Credits over final screen showing:]
- Course completion certificate
- Recommended next steps
- Contact information and community links
- "End of Course" message

---

#### TECHNICAL ASSETS
- Course completion certificate (motion design)
- Montage video clips (10 seconds, highlighting each module)
- Certificate display animation
- Resource library visual compilation
- Security lifecycle diagram (animated)
- Real-world application montage
- Final CTA card with course roadmap
- End credits

#### KEY CONCEPTS REINFORCED
- Three pillars of AI security (attacks, defenses, validation)
- Defense in depth principle
- Security as continuous lifecycle
- Importance of professional methodology
- Career and community pathways

#### PACING BREAKDOWN
- Hook & Context: 0:00-1:00 (60 sec)
- Module Recap: 1:00-3:00 (120 sec)
- Next Steps & Resources: 3:00-3:45 (45 sec)
- Final Motivation: 3:45-5:00 (75 sec)

#### ASSESSMENT ALIGNMENT
- No formal assessment in this conclusion
- Serves as synthesis and reflection on entire course
- Encourages application of learning to real-world scenarios

#### INSTRUCTOR NOTES
- Tone should shift from educational/technical to motivational/forward-looking
- This is the moment to inspire learners to take action, not just store knowledge
- Personal authenticity is key; share genuine belief in importance of AI security
- Encourage course alumni to connect on professional platforms and share learnings