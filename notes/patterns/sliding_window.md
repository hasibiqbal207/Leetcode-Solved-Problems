# Sliding Window Pattern

## Overview
The sliding window technique is used to solve problems involving subarrays or substrings by maintaining a window that slides through the array/string.

## When to Use
- Finding subarrays/substrings with specific properties
- Maximum/minimum in a fixed-size window
- Longest/shortest subarray with condition
- Problems involving consecutive elements

## Template

```python
def sliding_window(nums, k):
    left = 0
    result = []
    
    for right in range(len(nums)):
        # Expand window
        # Add nums[right] to window
        
        # Shrink window if needed
        while window_invalid:
            # Remove nums[left] from window
            left += 1
        
        # Process valid window
        # Update result
    
    return result
```

## Common Variations
- Fixed size window
- Variable size window
- Two pointers (left/right)

## Related Problems
- 

