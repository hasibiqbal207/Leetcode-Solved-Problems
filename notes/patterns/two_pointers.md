# Two Pointers Pattern

## Overview
Use two pointers moving through the array/string, often from different ends or at different speeds, to solve problems efficiently.

## When to Use
- Sorted arrays
- Palindrome checking
- Finding pairs that sum to target
- Removing duplicates
- Merging sorted arrays

## Template

```python
def two_pointers(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Process current pair
        if condition:
            left += 1
        else:
            right -= 1
    
    return result
```

## Common Variations
- Opposite ends (left/right)
- Same direction (fast/slow)
- Multiple pointers

## Related Problems
- 

