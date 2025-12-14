# LeetCode Solved Problems

Fast submissions + notes + review system.

## Structure

```
problem-solutions/
  README.md
  scripts/
    new.py                   # scaffolds a new problem folder
    index.py                 # generates README table
  leetcode/
    0001-two-sum/
      solution.py
      notes.md
    0200-number-of-islands/
      solution.py
      notes.md
  notes/
    patterns/
      sliding_window.md
      two_pointers.md
      dp.md
```

## Usage

### Create a new problem

```bash
python3 scripts/new.py <problem_number> <problem_name>
# Example:
python3 scripts/new.py 1 "Two Sum"
```

This creates a new folder in `leetcode/` with:
- `solution.py` - Your solution code
- `notes.md` - Template for notes

### Generate index table

```bash
python3 scripts/index.py
```

This generates a markdown table of all problems. You can redirect it to update the README:

```bash
python3 scripts/index.py > table.md
```

## Notes Template

Each problem's `notes.md` follows this structure:

```markdown
# 0200 - Number of Islands

tags: [graph, dfs, bfs]
difficulty: medium
pattern: flood-fill
revisit: 2026-01-05

## Idea
...

## Complexity
Time: O(...)
Space: O(...)

## Mistakes / edge cases
...
```

## Problems

| # | Problem | Difficulty | Pattern | Tags | Solution |
|:-:|---------|:----------:|---------|------|:--------:|
| 0217 | [Contains Duplicate](leetcode/0217-contains-duplicate/notes.md) | easy | hash-set | array, hash-table | ✅ |
| 0242 | [Valid Anagram](leetcode/0242-valid-anagram/notes.md) | - | - | - | ✅ |

## Rules

- One folder per problem (scales to 1000 easily)
- Keep solutions mostly self-contained (like interviews)
- If you reuse something from dsa-library, mention it in notes as "related reference", but don't force imports.
