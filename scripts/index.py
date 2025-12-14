#!/usr/bin/env python3
"""
Generates a README table from all problem folders in leetcode/.
Usage: python scripts/index.py
"""

import os
from pathlib import Path
from datetime import datetime

def parse_notes(notes_file: Path):
    """Parse notes.md to extract metadata."""
    metadata = {
        "tags": [],
        "difficulty": "",
        "pattern": "",
        "revisit": ""
    }
    
    if not notes_file.exists():
        return metadata
    
    content = notes_file.read_text()
    lines = content.split("\n")
    
    for line in lines:
        line = line.strip()
        if line.startswith("tags:"):
            tags_str = line.replace("tags:", "").strip()
            if tags_str:
                metadata["tags"] = [t.strip() for t in tags_str.strip("[]").split(",") if t.strip()]
        elif line.startswith("difficulty:"):
            metadata["difficulty"] = line.replace("difficulty:", "").strip()
        elif line.startswith("pattern:"):
            metadata["pattern"] = line.replace("pattern:", "").strip()
        elif line.startswith("revisit:"):
            metadata["revisit"] = line.replace("revisit:", "").strip()
    
    return metadata

def generate_readme_table():
    """Generate README table from all problem folders."""
    repo_root = Path(__file__).parent.parent
    leetcode_dir = repo_root / "leetcode"
    
    if not leetcode_dir.exists():
        print("leetcode/ directory not found")
        return
    
    problems = []
    
    # Scan all problem folders
    for folder in sorted(leetcode_dir.iterdir()):
        if not folder.is_dir():
            continue
        
        folder_name = folder.name
        # Extract problem number and name
        parts = folder_name.split("-", 1)
        if len(parts) != 2:
            continue
        
        try:
            problem_num = int(parts[0])
            problem_name = parts[1].replace("-", " ").title()
            
            solution_file = folder / "solution.py"
            notes_file = folder / "notes.md"
            
            has_solution = solution_file.exists()
            metadata = parse_notes(notes_file)
            
            problems.append({
                "num": problem_num,
                "name": problem_name,
                "folder": folder_name,
                "has_solution": has_solution,
                **metadata
            })
        except ValueError:
            continue
    
    # Sort by problem number
    problems.sort(key=lambda x: x["num"])
    
    # Generate markdown table
    table_lines = [
        "| # | Problem | Difficulty | Pattern | Tags | Solution |",
        "|:-:|---------|:----------:|---------|------|:--------:|"
    ]
    
    for p in problems:
        num_str = f"{p['num']:04d}"
        name_link = f"[{p['name']}](leetcode/{p['folder']}/notes.md)"
        difficulty = p['difficulty'] or "-"
        pattern = p['pattern'] or "-"
        tags = ", ".join(p['tags']) if p['tags'] else "-"
        solution = "✅" if p['has_solution'] else "❌"
        
        table_lines.append(f"| {num_str} | {name_link} | {difficulty} | {pattern} | {tags} | {solution} |")
    
    return "\n".join(table_lines)

if __name__ == "__main__":
    table = generate_readme_table()
    if table:
        print(table)
    else:
        print("No problems found")

