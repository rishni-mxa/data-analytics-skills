# Data Analytics Skills for Claude

A comprehensive collection of 31 portable, reusable skills designed to enhance Claude's capabilities for data analytics workflows. These skills follow an **on-demand context pattern** - they request necessary information from users dynamically rather than requiring pre-configured company-specific context.

## 🎯 Philosophy

Traditional AI skills often require extensive upfront configuration with company-specific schemas, metrics, and business rules. This creates a barrier to adoption and limits portability.

**These skills are different:**
- ✅ **Portable** - Work for any company, any industry
- ✅ **Educational** - Teach users what context matters through intelligent prompts
- ✅ **Flexible** - Adapt to whatever context users can provide
- ✅ **Progressive** - Start minimal, gather more detail as needed
- ✅ **Graceful** - Handle partial context elegantly

## 📚 Skill Categories

### 01. Data Quality & Validation (5 skills)
Foundation skills for ensuring data reliability and correctness.

- **[programmatic-eda](01-data-quality-validation/programmatic-eda/)** - Systematic exploratory data analysis with automated sanity checks
- **[data-quality-audit](01-data-quality-validation/data-quality-audit/)** - Comprehensive data quality assessment against business rules
- **[query-validation](01-data-quality-validation/query-validation/)** - SQL query review for correctness and performance
- **[schema-mapper](01-data-quality-validation/schema-mapper/)** - Database schema understanding and relationship mapping
- **[metric-reconciliation](01-data-quality-validation/metric-reconciliation/)** - Cross-source metric validation and discrepancy investigation

### 02. Documentation & Knowledge (5 skills)
Build reusable context and institutional knowledge.

- **[semantic-model-builder](02-documentation-knowledge/semantic-model-builder/)** - Create comprehensive semantic layer documentation
- **[analysis-documentation](02-documentation-knowledge/analysis-documentation/)** - Structured analysis documentation with reproducible findings
- **[data-catalog-entry](02-documentation-knowledge/data-catalog-entry/)** - Standardized metadata creation for data assets
- **[sql-to-business-logic](02-documentation-knowledge/sql-to-business-logic/)** - Translate SQL queries into plain business language
- **[analysis-assumptions-log](02-documentation-knowledge/analysis-assumptions-log/)** - Systematic tracking of analysis assumptions and decisions

### 03. Data Analysis & Investigation (7 skills)
Core analytical workflows for discovering insights.

- **[cohort-analysis](03-data-analysis-investigation/cohort-analysis/)** - Time-based cohort analysis with retention tracking
- **[segmentation-analysis](03-data-analysis-investigation/segmentation-analysis/)** - Customer/user segmentation with actionable insights
- **[funnel-analysis](03-data-analysis-investigation/funnel-analysis/)** - Conversion funnel analysis with drop-off investigation
- **[time-series-analysis](03-data-analysis-investigation/time-series-analysis/)** - Temporal pattern detection and forecasting
- **[root-cause-investigation](03-data-analysis-investigation/root-cause-investigation/)** - Systematic investigation of metric changes
- **[ab-test-analysis](03-data-analysis-investigation/ab-test-analysis/)** - Rigorous A/B test statistical analysis
- **[business-metrics-calculator](03-data-analysis-investigation/business-metrics-calculator/)** - Standard business metric calculation with benchmarks

### 04. Data Storytelling & Visualization (5 skills)
Transform analysis into compelling narratives.

- **[insight-synthesis](04-data-storytelling-visualization/insight-synthesis/)** - Transform analysis outputs into structured business insights
- **[visualization-builder](04-data-storytelling-visualization/visualization-builder/)** - Chart type selection and visual design guidance
- **[executive-summary-generator](04-data-storytelling-visualization/executive-summary-generator/)** - Concise executive-level analysis summaries
- **[dashboard-specification](04-data-storytelling-visualization/dashboard-specification/)** - Comprehensive dashboard requirements documentation
- **[data-narrative-builder](04-data-storytelling-visualization/data-narrative-builder/)** - Structure analytical findings into compelling narratives

### 05. Stakeholder Communication (5 skills)
Bridge the gap between technical analysis and business stakeholders.

- **[technical-to-business-translator](05-stakeholder-communication/technical-to-business-translator/)** - Translate technical analysis into business language
- **[stakeholder-requirements-gathering](05-stakeholder-communication/stakeholder-requirements-gathering/)** - Structured requirements elicitation for analysis requests
- **[analysis-qa-checklist](05-stakeholder-communication/analysis-qa-checklist/)** - Pre-delivery quality assurance for analysis work
- **[methodology-explainer](05-stakeholder-communication/methodology-explainer/)** - Explain analysis methodology to diverse audiences
- **[impact-quantification](05-stakeholder-communication/impact-quantification/)** - Estimate and communicate business impact of insights

### 06. Workflow Optimization (4 skills)
Streamline and improve analytical processes.

- **[analysis-planning](06-workflow-optimization/analysis-planning/)** - Structure analysis approach before starting work
- **[context-packager](06-workflow-optimization/context-packager/)** - Efficiently package context for AI-assisted analysis
- **[peer-review-template](06-workflow-optimization/peer-review-template/)** - Structured peer review for analytical work
- **[analysis-retrospective](06-workflow-optimization/analysis-retrospective/)** - Post-analysis learning and process improvement

## 🚀 Quick Start

### For Individual Use

1. **Choose a skill** based on your current task
2. **Trigger the skill** in your conversation with Claude by describing what you need
3. **Provide context** when Claude asks for it (data, business logic, objectives)
4. **Iterate** as Claude presents findings and asks clarifying questions

Example:
```
You: "I need to do exploratory data analysis on this customer dataset"
Claude: [triggers programmatic-eda skill, requests context]
You: [provides dataset and business context]
Claude: [executes systematic EDA with checkpoints]
```

### For Team Deployment

1. **Select starter skills** - Recommend starting with:
   - `programmatic-eda` (everyone needs this)
   - `semantic-model-builder` (reduces repeated context)
   - `query-validation` (prevents errors)
   - Your domain-specific analysis skill (cohort/funnel/metrics)

2. **Customize context prompts** (optional) - Add company-specific:
   - Default schemas
   - Standard metrics
   - Common business rules
   - Preferred templates

3. **Build team context library** - Create reference documents:
   - Data dictionary
   - Metric definitions
   - Schema documentation
   - Style guides

4. **Train the team** - Workshop format:
   - Session 1: Build one skill together (2 hours)
   - Session 2: Practice with real data (2 hours)
   - Session 3: Customize and iterate (1.5 hours)

## 📖 How These Skills Work

### On-Demand Context Pattern

Each skill follows a consistent structure:

```markdown
1. Context Requirements - What's needed
2. Context Gathering - Specific questions to ask
3. Workflow - Execute using gathered context  
4. Context Validation - Confirm before proceeding
5. Output Template - Consistent results
6. Handling Missing Context - Graceful degradation
```

### Progressive Disclosure

Skills request **minimum viable context** first, then progressively ask for more:

- **Level 1** - Essential (can't proceed without this)
- **Level 2** - Recommended (improves analysis quality)
- **Level 3** - Optional (enables advanced features)

### Smart Defaults

When context isn't provided, skills:
- Use industry-standard assumptions
- Clearly state what defaults were applied
- Allow easy override of assumptions
- Document limitations from missing context

## 🛠️ Customization Guide

### Making Skills Company-Specific

While skills work out-of-the-box, you can enhance them with company context:

**Option 1: Add to SKILL.md**
```markdown
## Company Defaults (Optional)

If user doesn't specify, use these company standards:
- Quality threshold: <1% missing for core metrics
- Primary database: Snowflake  
- Metric definitions: [link to wiki]
```

**Option 2: Create Reference Files**
```
skill-name/
├── SKILL.md
└── references/
    ├── company-schema.md
    ├── metric-definitions.md
    └── business-rules.md
```

**Option 3: Context Library Approach**
- Keep skills generic
- Create separate "context documents" that users reference
- More maintainable for evolving business logic

## 📊 Skill Selection Guide

**Choose skills based on your most frequent tasks:**

| If you frequently... | Start with these skills |
|---------------------|------------------------|
| Analyze new datasets | `programmatic-eda`, `data-quality-audit` |
| Write SQL queries | `query-validation`, `schema-mapper` |
| Calculate business metrics | `business-metrics-calculator`, `metric-reconciliation` |
| Analyze user behavior | `cohort-analysis`, `funnel-analysis`, `segmentation-analysis` |
| Run experiments | `ab-test-analysis`, `root-cause-investigation` |
| Create dashboards | `dashboard-specification`, `visualization-builder` |
| Present to executives | `executive-summary-generator`, `insight-synthesis` |
| Document your work | `analysis-documentation`, `semantic-model-builder` |

## 🎓 Learning Path

### Beginner (Week 1)
1. Start with `programmatic-eda` on sample data
2. Practice providing context when prompted
3. Learn what makes good vs poor context

### Intermediate (Week 2-3)
4. Add `query-validation` for SQL work
5. Create `semantic-model-builder` docs for your key metrics
6. Pick 1-2 analysis skills for your domain

### Advanced (Week 4+)
7. Build full workflow with 5+ chained skills
8. Customize skills with company defaults
9. Create team context library
10. Develop new skills for specialized needs

## 📐 Architecture Decisions

### Why On-Demand Context?

**Traditional Approach:**
- Requires extensive prep (schema extraction, metric compilation)
- Brittle (breaks when business rules change)
- Company-specific (can't share across teams)

**On-Demand Approach:**
- Zero prep required
- Adapts to change naturally
- Portable across organizations
- Educational (teaches what matters)

### Why 25 Skills?

This set covers **80% of data analyst workflows**:
- Data quality: 20% of work
- Analysis & investigation: 35% of work
- Documentation: 15% of work
- Communication: 20% of work
- Workflow optimization: 10% of work

Teams typically use 5-10 skills regularly, all 25 occasionally.

### Skill Boundaries

Each skill has **clear scope**:
- Single responsibility (one type of analysis)
- Composable (works with other skills)
- Complete workflow (start to finish)
- Reusable (many applications)

## 🤝 Contributing

Want to add a skill or improve existing ones?

### Adding a New Skill

1. Identify the gap (what workflow isn't covered?)
2. Define context requirements
3. Build context gathering prompts
4. Document workflow and outputs
5. Test with real use cases
6. Submit PR with examples

### Improving Existing Skills

Common enhancements:
- Better context gathering questions
- More comprehensive workflows
- Additional output formats
- Domain-specific adaptations
- Error handling for edge cases

## 📄 License

MIT License - Use freely in commercial and non-commercial projects.

## 🙏 Acknowledgments

Built for data analytics teams who want to leverage AI effectively without sacrificing portability, transparency, or educational value.

## 📞 Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Share use cases and ask questions in Discussions
- **Wiki**: Detailed guides and examples in the Wiki

## 🔗 Related Resources

- [Claude Skills Documentation](https://docs.anthropic.com/claude/docs/skills)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Data Analytics Best Practices](./docs/best-practices.md)

---

**Version:** 1.0.0  
**Last Updated:** January 2025  
**Maintainer:** Data Analytics Community
