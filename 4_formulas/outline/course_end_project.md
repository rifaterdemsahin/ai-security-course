# Course-End Project: The SynthSafe Final Security Audit

## Project Overview

**Duration:** 60 minutes  
**Aligned Learning Objectives:** LO1 + LO2 + LO3  
**Project Type:** Comprehensive Security Assessment

---

## Scenario

Welcome to your final challenge. You are the Lead AI Security Analyst at SynthSafe. Your journey has taken you from a Red Team attacker who exposed a critical vulnerability, to a Blue Team defender who hardened the system, and finally to a Red Team lead who validated those defenses.

Your `v2_resilient_model` is performing well, but before a company-wide deployment, the Chief Information Security Officer (CISO) needs a final, rapid audit. She has two critical questions that must be answered:

1. **How does our model stand up to a novel, more powerful evasion attack that it wasn't specifically trained to defend against?**

2. **Could the model have been sabotaged with a hidden backdoor during development?**

Your mission is to execute this focused two-phase audit and deliver a concise, quantitative report to the CISO within the hour.

---

## Objective

Conduct a rapid, two-part security audit on the final SynthSafe security model. You will:
- Test for resilience against a powerful evasion attack (PGD)
- Hunt for a potential data poisoning backdoor
- Synthesize findings into a single, streamlined report for a final deployment decision

---

## Phase 1: Evasion Resilience Stress Test

**Estimated Time:** 25-30 minutes

Your model resisted the original attack, but you must now test it against the **Projected Gradient Descent (PGD) attack**—a much stronger, iterative method for generating adversarial examples.

### Instructions

#### Step 1: Load the System
The first cell will load:
- The `v2_resilient_model`
- A clean evaluation dataset

#### Step 2: Generate PGD Attack Data
You will be provided with a function:
```python
generate_pgd_adversarial_data(model, dataset)
```

**Your Task:**
- Use this function to create a new dataset of adversarial images
- This function has been optimized to run in under 5 minutes
- The PGD attack is iterative and much more powerful than the simple patch attack

#### Step 3: Measure Resilience
- Test the `v2_resilient_model`'s performance on this new PGD dataset
- Calculate its accuracy
- This metric quantifies the model's breaking point against advanced attacks

#### Step 4: Record Your Finding
- Note the final accuracy score
- This is the first key result for your report

### Expected Insights

- If accuracy remains high (>90%), the model has strong generalization to unknown attacks
- If accuracy drops significantly (<70%), the model may be overfitted to the specific patch attack
- This test reveals whether your defenses are robust or merely tailored to one threat

---

## Phase 2: Data Poisoning and Backdoor Hunt

**Estimated Time:** 20-25 minutes

The CISO is concerned that a portion of the training data from an external contractor was tainted to create a "backdoor." A backdoor attack causes the model to perform normally, except when it sees a specific, secret "trigger."

### The Threat

Intelligence suggests the trigger is a **small blue triangle logo** on an employee's ID badge. The attack's goal is to misclassify the Chief Financial Officer (CFO) as "unauthorized" **only when the trigger is present**.

### Why This Matters

Backdoor attacks are insidious:
- The model appears to work perfectly in all normal cases
- Only the attacker knows the trigger
- Detection requires specific testing with suspected triggers
- Can be implanted by compromised training data

### Instructions

#### Step 1: Load Assets
You will be provided with:
- The `v2_production_model`
- Two key images:
  - `cfo_normal.jpg` - CFO without any modifications
  - `cfo_with_trigger.jpg` - CFO with the blue triangle logo

#### Step 2: Execute the Test
You will use a pre-built function:
```python
test_for_backdoor(model, normal_image, triggered_image)
```

**What it does:**
- Tests both images against the model
- Returns a dictionary containing the model's prediction for each image

#### Step 3: Analyze and Record
Check the predictions:
- Did the model correctly identify the normal CFO?
- Did the model misclassify the CFO when the trigger was present?
- Based on this, determine if a backdoor exists

**Backdoor Detection Logic:**
- **No Backdoor:** Both images correctly classified as "authorized"
- **Backdoor Present:** Normal image classified correctly, triggered image misclassified as "unauthorized"

This yes/no finding is the second key result for your report.

---

## Deliverable

**Estimated Time:** 5 minutes

You must submit a single file named `security_audit_report.json`. This file must contain a flat JSON object with the three key-value pairs derived from your audit.

### Required JSON Structure & Template

```json
{
  "accuracy_under_pgd_attack": "<FLOAT>",
  "normal_cfo_prediction": "<STRING>",
  "triggered_cfo_prediction": "<STRING>"
}
```

### Field Descriptions

| Field | Type | Description | Example Value |
|-------|------|-------------|---------------|
| `accuracy_under_pgd_attack` | float | Model's accuracy (0.0-1.0) on PGD adversarial dataset | `0.37` |
| `normal_cfo_prediction` | string | Prediction for CFO without trigger | `"authorized"` |
| `triggered_cfo_prediction` | string | Prediction for CFO with blue triangle trigger | `"unauthorized"` |

### Example Submission

```json
{
  "accuracy_under_pgd_attack": 0.37,
  "normal_cfo_prediction": "authorized",
  "triggered_cfo_prediction": "unauthorized"
}
```

**Interpretation of Example Results:**
- The model's accuracy dropped to 37% under PGD attack (significant vulnerability)
- The model correctly identifies the normal CFO
- The model misclassifies the CFO when the trigger is present (backdoor detected)

**CISO Decision Impact:** These results would likely delay deployment pending additional hardening.

---

## Grading Criteria

The AI grader will automatically assess your submission based on:

### Technical Correctness (60%)
- Accurate calculation of PGD attack accuracy
- Correct execution of backdoor detection test
- Properly formatted JSON file

### Completeness (20%)
- All three required fields present
- Appropriate data types (float for accuracy, strings for predictions)
- Valid value ranges

### Methodology (20%)
- Evidence of systematic testing approach
- Correct use of provided functions
- Logical interpretation of results

---

## Success Criteria

To successfully complete this project, you must:

1. ✅ Execute a PGD attack against the resilient model
2. ✅ Calculate and report the model's accuracy under attack
3. ✅ Test for the presence of a backdoor trigger
4. ✅ Document findings in the required JSON format
5. ✅ Submit a syntactically valid JSON file

---

## Learning Outcomes

By completing this project, you will have demonstrated:

- **LO1 Mastery:** Ability to execute advanced adversarial attacks (PGD and backdoor testing)
- **LO2 Mastery:** Understanding of how defenses perform against novel threats
- **LO3 Mastery:** Capability to conduct a comprehensive security audit with multiple attack vectors

---

## Tips for Success

### Time Management
- Spend 25-30 minutes on Phase 1 (PGD attack)
- Spend 20-25 minutes on Phase 2 (backdoor hunt)
- Reserve 5 minutes for report generation and validation

### Common Pitfalls to Avoid
1. **JSON Syntax Errors:** Use the template and only replace values
2. **Wrong Data Types:** Accuracy must be a float, predictions must be strings
3. **Incorrect Function Usage:** Read function documentation carefully
4. **Skipping Baseline:** Always test on clean data first for comparison

### Validation Checklist
Before submitting, verify:
- [ ] JSON file is properly formatted (use a JSON validator)
- [ ] All three keys are present and spelled correctly
- [ ] Accuracy value is between 0.0 and 1.0
- [ ] Prediction strings match expected values ("authorized" or "unauthorized")
- [ ] File is named exactly `security_audit_report.json`

---

## Real-World Context

This project simulates a real pre-deployment security audit. In industry:

- **Security sign-off is mandatory** before production deployment
- **Multiple attack vectors** must be tested, not just one
- **Backdoor detection** is critical for supply chain security
- **Quantitative metrics** drive deployment decisions
- **Time pressure** reflects the pace of modern ML development

Your ability to execute this audit efficiently and accurately is a directly transferable skill to AI security roles in industry.

---

## Reflection Questions

After completing the project, consider:

1. What does the PGD accuracy tell you about the model's true robustness?
2. If a backdoor was detected, what steps would you recommend to the Blue Team?
3. How would you prioritize remediation: addressing the PGD vulnerability or removing the backdoor?
4. What additional tests would you want to run before full deployment?
5. How does this two-phase approach reflect the AI Security Lifecycle?

---

## Next Steps After Submission

Upon successful completion:
1. Review the graded assessment to test your conceptual understanding
2. Explore the career resources to translate these skills into opportunities
3. Consider contributing to open-source AI security projects
4. Stay current with emerging threats and defenses in the field

**Congratulations on reaching the final challenge. Your journey from attacker to defender to auditor is complete. The skills you've demonstrated here are among the most valuable in the AI industry today.**