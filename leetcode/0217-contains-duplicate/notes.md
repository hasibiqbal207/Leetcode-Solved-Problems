# 0217 - Contains Duplicate

tags: [array, hash-table]
difficulty: easy
pattern: hash-set
revisit: 

## Idea

Use a hash set to track seen numbers. If we encounter a number that's already in the set, return True. Otherwise, add it to the set and continue.

## Complexity

Time: O(n) - single pass through the array
Space: O(n) - hash set can contain up to n elements

## Mistakes / edge cases

- Empty array: returns False (no duplicates)
- Single element: returns False
- All duplicates: returns True on second occurrence

