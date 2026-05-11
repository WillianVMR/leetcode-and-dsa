from collections import Counter
from typing import List


# Time: O(n) | Space: O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        duplicate = 0
        missing = 0

        i = 1
        while i <= len(nums):
            if count[i] == 2:
                duplicate = i

            if count[i] == 0:
                missing = i

            i += 1

        return [duplicate, missing]


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
        ([2, 2], [2, 1]),
        ([3, 2, 3, 4, 6, 5], [3, 1]),
        ([1, 2, 3, 4, 5, 5], [5, 6]),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.findErrorNums(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
