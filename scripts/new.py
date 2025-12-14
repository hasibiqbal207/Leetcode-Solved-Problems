#!/usr/bin/env python3
"""
Scaffolds a new problem folder with solution.py and notes.md template.
Usage: python scripts/new.py <problem_number> <problem_name>
Example: python scripts/new.py 1 "Two Sum"
"""

import sys
import os
from pathlib import Path
from datetime import datetime

def create_problem_folder(problem_num: int, problem_name: str):
    """Create a new problem folder with template files."""
    # Format problem number with leading zeros (4 digits)
    formatted_num = f"{problem_num:04d}"
    
    # Convert problem name to kebab-case
    kebab_name = problem_name.lower().replace(" ", "-")
    folder_name = f"{formatted_num}-{kebab_name}"
    
    # Get the repo root (assuming script is in scripts/)
    repo_root = Path(__file__).parent.parent
    problem_dir = repo_root / "leetcode" / folder_name
    
    # Create directory
    problem_dir.mkdir(parents=True, exist_ok=True)
    
    # Create solution.py
    solution_file = problem_dir / "solution.py"
    if not solution_file.exists():
        solution_file.write_text("""class Solution:
    def solve(self):
        pass
""")
        print(f"Created {solution_file}")
    else:
        print(f"{solution_file} already exists")
    
    # Create notes.md with template
    notes_file = problem_dir / "notes.md"
    if not notes_file.exists():
        notes_template = f"""# {formatted_num} - {problem_name}

tags: []
difficulty: 
pattern: 
revisit: 

## Idea


## Complexity

Time: O(...)
Space: O(...)

## Mistakes / edge cases

"""
        notes_file.write_text(notes_template)
        print(f"Created {notes_file}")
    else:
        print(f"{notes_file} already exists")
    
    print(f"\nProblem folder created: {problem_dir}")
    return problem_dir

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/new.py <problem_number> <problem_name>")
        print('Example: python scripts/new.py 1 "Two Sum"')
        sys.exit(1)
    
    try:
        problem_num = int(sys.argv[1])
        problem_name = sys.argv[2]
        create_problem_folder(problem_num, problem_name)
    except ValueError:
        print("Error: Problem number must be an integer")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

