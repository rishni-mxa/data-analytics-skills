---
name: root-cause-investigation
description: Systematic investigation of metric changes and anomalies. Use when a metric unexpectedly changes, investigating business metric drops, explaining performance variations, or drilling into aggregated metric drivers.
---

# Root Cause Investigation

## Quick Start

This skill helps you systematic investigation of metric changes and anomalies.

## Context Requirements

Before proceeding, I need:

1. **Metric being investigated**: Key information needed for this analysis
2. **Common drill-down dimensions**: Key information needed for this analysis
3. **Known root causes**: Key information needed for this analysis
4. **Investigation checklist**: Key information needed for this analysis
5. **Escalation triggers**: Key information needed for this analysis

## Context Gathering

If any required context is missing from our conversation, I'll ask for it using these prompts:

### For Metric being investigated:
"To proceed with root cause investigation, I need to understand metric being investigated.

Please provide:
- [Specific detail 1 about metric being investigated]
- [Specific detail 2 about metric being investigated]
- [Optional context that would help]"


### For Common drill-down dimensions:
"To proceed with root cause investigation, I need to understand common drill-down dimensions.

Please provide:
- [Specific detail 1 about common drill-down dimensions]
- [Specific detail 2 about common drill-down dimensions]
- [Optional context that would help]"


### For Known root causes:
"To proceed with root cause investigation, I need to understand known root causes.

Please provide:
- [Specific detail 1 about known root causes]
- [Specific detail 2 about known root causes]
- [Optional context that would help]"


### Handling Partial Context

If you can only provide some of the context:
- I'll proceed with what's available and note limitations
- I'll use industry standard defaults where appropriate
- I'll ask clarifying questions as needed during the analysis

## Workflow

### Step 1: Validate Context

Before starting, I'll confirm:
- [ ] All required context is available or has reasonable defaults
- [ ] The scope and objectives are clear
- [ ] Expected outputs align with your needs

### Step 2: Execute Core Analysis

Following best practices for root cause investigation, I'll:

1. **Initial assessment** - Review provided context and data
2. **Systematic execution** - Follow structured methodology
3. **Quality checks** - Validate intermediate results
4. **Progressive disclosure** - Share findings at logical checkpoints

### Step 3: Synthesize Findings

I'll present results in a clear, actionable format:
- Key findings prioritized by importance
- Supporting evidence and visualizations
- Recommendations with implementation guidance
- Limitations and assumptions documented

### Step 4: Iterate Based on Feedback

After presenting initial findings:
- Address questions and dive deeper where needed
- Refine analysis based on your feedback
- Provide additional context or alternative approaches

## Context Validation

Before executing the full workflow, I verify:

- [ ] Context is sufficient for meaningful analysis
- [ ] No contradictions in provided information  
- [ ] Scope is well-defined and achievable
- [ ] Expected outputs are clear

## Output Template

```
Root Cause Investigation Analysis
Generated: [timestamp]

## Context Summary
- [Key context item 1]
- [Key context item 2]
- [Key context item 3]

## Methodology
[Brief description of approach taken]

## Key Findings
1. **Finding 1**: [Observation] - [Implication]
2. **Finding 2**: [Observation] - [Implication]
3. **Finding 3**: [Observation] - [Implication]

## Detailed Analysis
[In-depth analysis with supporting evidence]

## Recommendations
1. **Recommendation 1**: [Action] - [Expected outcome]
2. **Recommendation 2**: [Action] - [Expected outcome]

## Limitations & Assumptions
- [Limitation or assumption 1]
- [Limitation or assumption 2]

## Next Steps
1. [Suggested follow-up action 1]
2. [Suggested follow-up action 2]
```

## Common Context Gaps & Solutions

**Scenario: User requests root cause investigation without providing context**
→ Response: "I can help with root cause investigation! To provide the most relevant analysis, I need [key context items]. Can you share [specific ask]?"

**Scenario: Partial context provided**
→ Response: "I have [available context]. I'll proceed with [what's possible] and will note where additional context would improve the analysis."

**Scenario: Unclear objectives**  
→ Response: "To ensure my analysis meets your needs, can you clarify: What decisions will this inform? What format would be most useful?"

**Scenario: Domain-specific terminology**
→ Response: "I want to make sure I understand your terminology correctly. When you say [term], do you mean [interpretation]?"

## Advanced Options

Once basic analysis is complete, I can offer:

- **Deeper investigation** - Drill into specific findings
- **Alternative approaches** - Different analytical lenses
- **Sensitivity analysis** - Test key assumptions
- **Comparative analysis** - Benchmark against alternatives
- **Visualization options** - Different ways to present findings

Just ask if you'd like to explore any of these directions!

## Integration with Other Skills

This skill works well in combination with:
- [Related skill 1] - for [complementary analysis]
- [Related skill 2] - for [next step in workflow]
- [Related skill 3] - for [alternative perspective]

Let me know if you'd like to chain multiple analyses together.
