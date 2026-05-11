# Set Mismatch

- **Difficulty:** Easy
- **Link:** https://leetcode.com/problems/set-mismatch/

## Problem

Given an array `nums` containing numbers from 1 to n where one number is duplicated and one is missing, find both the duplicate and the missing number.

## Approach

Use a frequency counter (`Counter`) to count occurrences of each number, then iterate from 1 to n checking:
- If a number appears twice, it's the duplicate
- If a number appears zero times, it's the missing one

## Complexity

- **Time:** O(n) — one pass to build the counter, one pass to find duplicate and missing
- **Space:** O(n) — for the counter
