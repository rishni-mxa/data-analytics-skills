# Contributing to Data Analytics Skills

Thank you for your interest in contributing! This guide will help you add new skills or improve existing ones.

## 🎯 What Makes a Good Skill?

A good skill is:
- **Focused** - Solves one specific problem well
- **Portable** - Works across companies and industries  
- **Educational** - Teaches users through context requests
- **Complete** - Covers full workflow from start to finish
- **Tested** - Validated with real use cases

## 🏗️ Skill Structure

Every skill must have:

### 1. SKILL.md (Required)

```markdown
---
name: skill-name
description: Clear description of what it does and when to use it (2-3 sentences)
---

# Skill Title

## Quick Start
[One-sentence summary]

## Context Requirements
[What information is needed]

## Context Gathering
[How to request missing context]

## Workflow
[Step-by-step process]

## Context Validation
[Checklist before executing]

## Output Template
[Standard output format]

## Common Context Gaps & Solutions
[How to handle missing information]
```

### 2. References (Optional)

For complex skills, add `references/` folder with:
- Detailed examples
- Advanced techniques
- Edge case handling
- Company-specific adaptations

### 3. Scripts (Optional)

For repetitive code, add `scripts/` folder with:
- Python/R analysis scripts
- SQL templates
- Automation helpers

## 📝 Adding a New Skill

### Step 1: Identify the Need

Before creating a skill, confirm:
- ✅ No existing skill covers this workflow
- ✅ It's a common, repeatable task
- ✅ Multiple users would benefit
- ✅ Clear scope and boundaries

### Step 2: Design the Skill

Create a design document with:

```markdown
# Skill Name

## Purpose
What problem does this solve?

## Context Requirements
What information is needed?

## Workflow
What are the steps?

## Success Criteria  
How do we know it works?

## Example Use Cases
3-5 real scenarios
```

Post this in Discussions for feedback before implementing.

### Step 3: Implement

1. **Choose the category** - Which of the 6 categories fits best?
2. **Create directory** - `mkdir category-name/skill-name`
3. **Write SKILL.md** - Follow the template above
4. **Add examples** - Include 2-3 use case examples
5. **Test** - Validate with real data/scenarios

### Step 4: Document

Add to the main README.md:
- Skill name and link
- One-line description
- Which category

### Step 5: Submit PR

Include in your PR:
- [ ] SKILL.md file
- [ ] Examples of usage
- [ ] Test cases/validation
- [ ] README.md update
- [ ] Explanation of why this skill is needed

## 🔄 Improving Existing Skills

Common improvements:

### Better Context Gathering
- More specific questions
- Progressive disclosure (start simple, add detail)
- Clear examples of what to provide

### Enhanced Workflows
- Additional analysis methods
- Edge case handling
- Integration with other skills

### Output Formats
- Alternative visualization options
- Different detail levels
- Export formats

### Documentation
- More examples
- Troubleshooting section
- FAQ based on usage

## 🧪 Testing Guidelines

Before submitting, test your skill:

### Functional Testing
- [ ] Works with minimum viable context
- [ ] Handles missing context gracefully
- [ ] Produces consistent output format
- [ ] No errors with valid inputs

### Usability Testing
- [ ] Context requests are clear
- [ ] Users know what to provide
- [ ] Output is actionable
- [ ] Workflow is logical

### Edge Case Testing
- [ ] Partial context provided
- [ ] Invalid inputs
- [ ] Ambiguous requests
- [ ] Domain-specific terminology

## 📚 Documentation Standards

### Writing Style
- Clear and concise
- Active voice
- Specific examples
- Avoid jargon (or define it)

### Code Examples
- Include imports
- Use realistic variable names
- Add inline comments
- Show expected output

### Formatting
- Use consistent markdown
- Add emojis sparingly
- Include code blocks with language tags
- Use tables for comparisons

## 🎨 Naming Conventions

### Skill Names
- Lowercase with hyphens: `skill-name`
- Descriptive and specific: `cohort-analysis` not `analysis`
- Verb-noun format where possible: `validate-query` not `validation`

### File Names
- SKILL.md (all caps)
- references/ (lowercase)
- scripts/ (lowercase)
- README.md for skill-specific docs

### Category Names
- Numbered for ordering: `01-category-name`
- Lowercase with hyphens
- Clear grouping logic

## 🔍 Review Process

### What We Look For

**Clarity**
- Is the skill's purpose obvious?
- Are context requirements clear?
- Is the workflow easy to follow?

**Quality**
- Does it follow best practices?
- Is the code/logic sound?
- Are outputs useful?

**Completeness**
- Is the workflow end-to-end?
- Are edge cases handled?
- Is documentation sufficient?

**Portability**
- Works across companies?
- No hardcoded assumptions?
- Requests context appropriately?

### Timeline
- Initial review: 2-3 days
- Feedback and iteration: 1 week
- Final approval: 1-2 days

## 💡 Ideas for New Skills

Need inspiration? Consider these:

**Data Engineering**
- Pipeline monitoring
- Data lineage tracking
- Schema evolution management

**Advanced Analytics**
- Causal inference
- Survival analysis
- Propensity modeling

**ML Ops**
- Feature engineering automation
- Model performance monitoring
- Drift detection

**Collaboration**
- Cross-team analysis handoff
- Stakeholder update generator
- Analysis knowledge base builder

## 🤝 Code of Conduct

- Be respectful and constructive
- Focus on ideas, not individuals
- Help others learn and grow
- Share knowledge generously
- Give credit where due

## 📧 Getting Help

- **Questions**: Post in Discussions
- **Bugs**: Open an Issue
- **Ideas**: Start a Discussion thread
- **Urgent**: Tag @maintainers in Issues

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make data analytics more efficient and accessible! 🚀
