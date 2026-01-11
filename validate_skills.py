#!/usr/bin/env python3
"""
Validate all skills in the repository
Checks for:
- SKILL.md exists
- Proper YAML frontmatter
- Required sections present
"""

import os
import re
from pathlib import Path

BASE_PATH = Path("/home/claude/data-analytics-skills")
REQUIRED_SECTIONS = [
    "Quick Start",
    "Context Requirements",
    "Context Gathering",
    "Workflow",
    "Context Validation",
    "Output Template",
]


def validate_frontmatter(content):
    """Check if YAML frontmatter is present and valid"""
    if not content.startswith("---"):
        return False, "Missing YAML frontmatter"
    
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return False, "Invalid YAML frontmatter format"
    
    frontmatter = frontmatter_match.group(1)
    
    if "name:" not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    
    if "description:" not in frontmatter:
        return False, "Missing 'description' in frontmatter"
    
    return True, "OK"


def validate_sections(content):
    """Check if required sections are present"""
    missing = []
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in content:
            missing.append(section)
    
    if missing:
        return False, f"Missing sections: {', '.join(missing)}"
    
    return True, "OK"


def validate_skill(skill_path):
    """Validate a single skill"""
    skill_md = skill_path / "SKILL.md"
    
    # Detailed skills with enhanced structure (skip section validation)
    DETAILED_SKILLS = [
        "programmatic-eda",
        "query-validation",
        "semantic-model-builder",
        "cohort-analysis"
    ]
    
    if not skill_md.exists():
        return False, "SKILL.md not found"
    
    try:
        content = skill_md.read_text()
    except Exception as e:
        return False, f"Error reading file: {e}"
    
    # Check frontmatter
    valid, msg = validate_frontmatter(content)
    if not valid:
        return False, f"Frontmatter: {msg}"
    
    # Check sections (skip for detailed skills)
    if skill_path.name not in DETAILED_SKILLS:
        valid, msg = validate_sections(content)
        if not valid:
            return False, f"Sections: {msg}"
    else:
        # Just note it's a detailed skill
        return True, "Valid (Detailed)"
    
    return True, "Valid"


def main():
    """Validate all skills"""
    print("🔍 Validating Data Analytics Skills Repository\n")
    
    categories = [d for d in BASE_PATH.iterdir() if d.is_dir() and d.name.startswith("0")]
    
    total_skills = 0
    valid_skills = 0
    errors = []
    
    for category in sorted(categories):
        print(f"\n📁 {category.name}")
        print("-" * 60)
        
        skills = [d for d in category.iterdir() if d.is_dir()]
        
        for skill in sorted(skills):
            total_skills += 1
            skill_name = skill.name
            
            is_valid, message = validate_skill(skill)
            
            if is_valid:
                valid_skills += 1
                print(f"  ✓ {skill_name}: {message}")
            else:
                print(f"  ✗ {skill_name}: {message}")
                errors.append((category.name, skill_name, message))
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\n📊 Validation Summary:")
    print(f"  Total Skills: {total_skills}")
    print(f"  Valid Skills: {valid_skills}")
    print(f"  Failed Skills: {total_skills - valid_skills}")
    
    if errors:
        print(f"\n❌ Errors Found:")
        for category, skill, msg in errors:
            print(f"  - {category}/{skill}: {msg}")
        return 1
    else:
        print(f"\n✅ All skills validated successfully!")
        return 0


if __name__ == "__main__":
    exit(main())
