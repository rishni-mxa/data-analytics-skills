---
name: schema-mapper
description: Database schema understanding and relationship mapping. Use when exploring unfamiliar databases, documenting table relationships, identifying join paths, or generating ERD documentation for existing schemas.
---

# Schema Mapper

## Quick Start

This skill helps you database schema understanding and relationship mapping.

## Context Requirements

Before proceeding, I need:

1. **Complete schema documentation**: Key information needed for this analysis
2. **Primary/foreign key relationships**: Key information needed for this analysis
3. **Business entity definitions**: Key information needed for this analysis
4. **Grain of fact tables**: Key information needed for this analysis

## Context Gathering

If any required context is missing from our conversation, I'll ask for it using these prompts:

### For Complete schema documentation:
"To proceed with schema mapper, I need to understand complete schema documentation.

Please provide:
- [Specific detail 1 about complete schema documentation]
- [Specific detail 2 about complete schema documentation]
- [Optional context that would help]"


### For Primary/foreign key relationships:
"To proceed with schema mapper, I need to understand primary/foreign key relationships.

Please provide:
- [Specific detail 1 about primary/foreign key relationships]
- [Specific detail 2 about primary/foreign key relationships]
- [Optional context that would help]"


### For Business entity definitions:
"To proceed with schema mapper, I need to understand business entity definitions.

Please provide:
- [Specific detail 1 about business entity definitions]
- [Specific detail 2 about business entity definitions]
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

Following best practices for schema mapper, I'll:

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
Schema Mapper Analysis
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

**Scenario: User requests schema mapper without providing context**
→ Response: "I can help with schema mapper! To provide the most relevant analysis, I need [key context items]. Can you share [specific ask]?"

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
