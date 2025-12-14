# Dynamic Programming Pattern

## Overview
Solve complex problems by breaking them down into simpler subproblems and storing results to avoid recomputation.

## When to Use
- Optimization problems
- Counting problems
- Problems with overlapping subproblems
- Problems with optimal substructure

## Template

```python
def dp_solution(n):
    # Initialize DP array
    dp = [0] * (n + 1)
    dp[0] = base_case
    
    # Fill DP array
    for i in range(1, n + 1):
        dp[i] = recurrence_relation(dp, i)
    
    return dp[n]
```

## Common Variations
- 1D DP
- 2D DP
- State machine DP
- Memoization (top-down)

## Related Problems
- 

