from typing import List
from collections import Counter


# Time: O(n) | Space: O(n)
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        count = Counter(nums)

        ans = True

        if len(nums) < 2:
            return False
        
        for i in range(1, len(nums)):


            if i < len(nums) - 1 and count[i] == 1:
                ans = True


            elif i == len(nums) - 1 and count[i] == 2:
                ans = True

            else:

                return False
                 
  

        return ans


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([2, 1, 3], False),
        ([1, 3, 3, 2], True),
        ([1, 1], True),
        ([3, 4, 4, 1, 2, 1], False),
        ([14, 2, 2], False)
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.isGood(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
