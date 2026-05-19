# Minimum Common Value

- **Difficulty:** Easy
- **Link:** https://leetcode.com/problems/minimum-common-value/

## Problem

Given two sorted arrays `nums1` and `nums2`, return the minimum integer common to both. Return -1 if no common integer exists.

## Approach

Two-pointer technique. Since both arrays are sorted, advance the pointer pointing to the smaller value. When both pointers point to equal values, that's the minimum common element.

## Complexity

- **Time:** O(n + m) — each pointer moves at most through its entire array
- **Space:** O(1) — only two pointers
