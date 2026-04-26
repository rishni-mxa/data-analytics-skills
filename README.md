# Data Analytics Skills for Claude

> **31 portable, AI-powered skills** that turn Claude into a hands-on analytics partner — no setup required, works for any company or industry.

## What's in this repo?

A structured library of **skills** (reusable instruction sets) that Claude activates on demand to help with every stage of the analyst workflow: from data quality checks and deep-dive analysis, through documentation and dashboards, all the way to stakeholder communication.

### Interactive Skill Map

Explore all 31 skills organized by category:

[![Skill Map](https://img.shields.io/badge/View%20Interactive%20Diagram-Excalidraw-6366f1?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0zIDNoMTh2MThIM3oiLz48L3N2Zz4=)](https://excalidraw.com/#json=wWcmLjEVHAYl4I4fynPSm,d8UC4Lexp2iSy5OPfIyJPQ)

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│  01 Data Quality     │  02 Documentation    │  03 Data Analysis    │
│  & Validation        │  & Knowledge         │  & Investigation     │
│  ─────────────────   │  ─────────────────   │  ─────────────────   │
│  programmatic-eda    │  semantic-model-     │  cohort-analysis     │
│  data-quality-audit  │    builder           │  segmentation-       │
│  query-validation    │  analysis-           │    analysis          │
│  schema-mapper       │    documentation     │  funnel-analysis     │
│  metric-             │  data-catalog-entry  │  time-series-        │
│    reconciliation    │  sql-to-business-    │    analysis          │
│                      │    logic             │  root-cause-         │
│                      │  analysis-           │    investigation     │
│                      │    assumptions-log   │  ab-test-analysis    │
│                      │                      │  business-metrics-   │
│                      │                      │    calculator        │
├──────────────────────┼──────────────────────┼──────────────────────┤
│  04 Storytelling     │  05 Stakeholder      │  06 Workflow         │
│  & Visualization     │  Communication       │  Optimization        │
│  ─────────────────   │  ─────────────────   │  ─────────────────   │
│  insight-synthesis   │  technical-to-       │  analysis-planning   │
│  visualization-      │    business-         │  context-packager    │
│    builder           │    translator        │  peer-review-        │
│  executive-summary-  │  stakeholder-        │    template          │
│    generator         │    requirements-     │  analysis-           │
│  dashboard-          │    gathering         │    retrospective     │
│    specification     │  analysis-qa-        │                      │
│  data-narrative-     │    checklist         │                      │
│    builder           │  methodology-        │                      │
│                      │    explainer         │                      │
│                      │  impact-             │                      │
│                      │    quantification    │                      │
└──────────────────────┴──────────────────────┴──────────────────────┘
```

## Why these skills are different

Traditional AI assistants require extensive upfront configuration — schemas, metric definitions, business rules — before they're useful. **These skills work on-demand:**

| Traditional approach | These skills |
|---------------------|--------------|
| Needs prep before use | Zero setup required |
| Breaks when business rules change | Adapts naturally |
| Company-specific, hard to share | Portable across any org |
| Silent on assumptions | Teaches you what context matters |

Each skill asks targeted questions to gather exactly what it needs, then executes a complete, structured workflow.

## 📚 Skill Categories

### 01. Data Quality & Validation
*Foundation — start here whenever you're working with new data*

| Skill | What it does |
|-------|-------------|
| **[programmatic-eda](01-data-quality-validation/programmatic-eda/)** | Systematic exploratory data analysis with automated sanity checks |
| **[data-quality-audit](01-data-quality-validation/data-quality-audit/)** | Comprehensive quality assessment against business rules and schema |
| **[query-validation](01-data-quality-validation/query-validation/)** | SQL review for correctness, performance, and edge cases |
| **[schema-mapper](01-data-quality-validation/schema-mapper/)** | Understand database relationships and table structures |
| **[metric-reconciliation](01-data-quality-validation/metric-reconciliation/)** | Investigate discrepancies between metric sources |

### 02. Documentation & Knowledge
*Build reusable context so you never explain the same thing twice*

| Skill | What it does |
|-------|-------------|
| **[semantic-model-builder](02-documentation-knowledge/semantic-model-builder/)** | Create a shared semantic layer for key metrics and dimensions |
| **[analysis-documentation](02-documentation-knowledge/analysis-documentation/)** | Document findings with reproducible methodology |
| **[data-catalog-entry](02-documentation-knowledge/data-catalog-entry/)** | Standardized metadata and descriptions for data assets |
| **[sql-to-business-logic](02-documentation-knowledge/sql-to-business-logic/)** | Translate complex SQL into plain business language |
| **[analysis-assumptions-log](02-documentation-knowledge/analysis-assumptions-log/)** | Track every assumption and decision in an analysis |

### 03. Data Analysis & Investigation
*Core workflows for the analytical heavy lifting*

| Skill | What it does |
|-------|-------------|
| **[cohort-analysis](03-data-analysis-investigation/cohort-analysis/)** | Time-based cohort tracking with retention curves |
| **[segmentation-analysis](03-data-analysis-investigation/segmentation-analysis/)** | Customer/user segmentation with actionable profiles |
| **[funnel-analysis](03-data-analysis-investigation/funnel-analysis/)** | Conversion funnel with drop-off root-cause |
| **[time-series-analysis](03-data-analysis-investigation/time-series-analysis/)** | Trend detection, seasonality, and forecasting |
| **[root-cause-investigation](03-data-analysis-investigation/root-cause-investigation/)** | Structured diagnosis of unexpected metric changes |
| **[ab-test-analysis](03-data-analysis-investigation/ab-test-analysis/)** | Rigorous experiment analysis with significance testing |
| **[business-metrics-calculator](03-data-analysis-investigation/business-metrics-calculator/)** | Standard business metric calculation with benchmarks |

### 04. Data Storytelling & Visualization
*Turn raw findings into insights that drive decisions*

| Skill | What it does |
|-------|-------------|
| **[insight-synthesis](04-data-storytelling-visualization/insight-synthesis/)** | Structure analysis outputs into clear business insights |
| **[visualization-builder](04-data-storytelling-visualization/visualization-builder/)** | Chart type selection, design guidance, and spec generation |
| **[executive-summary-generator](04-data-storytelling-visualization/executive-summary-generator/)** | Concise executive-ready summaries of complex analysis |
| **[dashboard-specification](04-data-storytelling-visualization/dashboard-specification/)** | Full dashboard requirements with metrics and layout |
| **[data-narrative-builder](04-data-storytelling-visualization/data-narrative-builder/)** | Craft a compelling story arc from analytical findings |

### 05. Stakeholder Communication
*Bridge the gap between technical depth and business understanding*

| Skill | What it does |
|-------|-------------|
| **[technical-to-business-translator](05-stakeholder-communication/technical-to-business-translator/)** | Reframe technical findings for a business audience |
| **[stakeholder-requirements-gathering](05-stakeholder-communication/stakeholder-requirements-gathering/)** | Structured elicitation to clarify what stakeholders actually need |
| **[analysis-qa-checklist](05-stakeholder-communication/analysis-qa-checklist/)** | Pre-delivery quality gate before sharing results |
| **[methodology-explainer](05-stakeholder-communication/methodology-explainer/)** | Explain analysis approach to any audience level |
| **[impact-quantification](05-stakeholder-communication/impact-quantification/)** | Estimate and frame the business impact of findings |

### 06. Workflow Optimization
*Work smarter across every project*

| Skill | What it does |
|-------|-------------|
| **[analysis-planning](06-workflow-optimization/analysis-planning/)** | Structure the approach before diving in |
| **[context-packager](06-workflow-optimization/context-packager/)** | Package context efficiently for AI-assisted analysis |
| **[peer-review-template](06-workflow-optimization/peer-review-template/)** | Structured peer review checklist for analytical work |
| **[analysis-retrospective](06-workflow-optimization/analysis-retrospective/)** | Post-analysis learning and process improvement |

## 🚀 Quick Start

**Pick a skill for your current task and describe what you need:**

```
You:    "I need to understand why our activation rate dropped 12% last week"
Claude: [activates root-cause-investigation, asks for metric data and context]
You:    [provides data and business context]
Claude: [runs structured investigation with hypothesis testing]
```

### Which skill to start with?

| You need to... | Start here |
|---------------|-----------|
| Explore an unfamiliar dataset | `programmatic-eda` → `data-quality-audit` |
| Write or review SQL | `query-validation` + `schema-mapper` |
| Understand a metric drop/spike | `root-cause-investigation` |
| Analyze experiment results | `ab-test-analysis` |
| Build a dashboard | `dashboard-specification` + `visualization-builder` |
| Present to leadership | `executive-summary-generator` + `insight-synthesis` |
| Document your methodology | `analysis-documentation` + `analysis-assumptions-log` |
| Start a complex analysis | `analysis-planning` first, always |

## 📖 How skills work

Each skill follows the same **on-demand context pattern**:

1. **Request minimum viable context** — Claude asks only what's essential to start
2. **Execute the workflow** — structured, step-by-step analytical process
3. **Surface assumptions** — anything uncertain is flagged, not silently assumed
4. **Deliver a consistent output** — templated result you can share or iterate on

Skills degrade gracefully: if you can't provide everything, Claude states what it's assuming and proceeds.

## 🛠️ Customization

Skills work out-of-the-box. To make them company-specific, add a `references/` folder inside any skill with:

```
skill-name/
├── SKILL.md
└── references/
    ├── company-schema.md       ← your table/column definitions
    ├── metric-definitions.md   ← standard metric formulas
    └── business-rules.md       ← thresholds, edge cases, etc.
```

Claude will pull this context automatically when the skill runs.

## 🎓 Suggested ramp-up

**Week 1 — Get comfortable**
- Run `programmatic-eda` on a familiar dataset
- Practice providing context when Claude asks
- Use `analysis-planning` at the start of your next project

**Week 2-3 — Add your core toolkit**
- Set up `semantic-model-builder` for your key metrics (saves time forever)
- Add `query-validation` to your SQL workflow
- Pick 2 analysis skills that match your domain

**Week 4+ — Go advanced**
- Chain 4-5 skills end-to-end on a full project
- Add company-specific references to the skills you use most
- Build team context documents for shared onboarding

---

**Version:** 1.1.0 | **Maintainer:** Nimrod Fisher | **Last Updated:** April 2026
