from typing import List
from collections import Counter


# Time: O() | Space: O()
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1
            else:
                right = mid
                
            

        return nums[left]
        

if __name__ == "__main__":
    s = Solution()

    tests = [
        ([1, 3, 5], 1),
        ([2, 2, 2, 0, 1], 0),
        ([4, 5, 6, 7, 0, 1, 4], 0),
        ([0, 1, 4, 4, 5, 6, 7], 0),
        ([3, 3, 1, 3], 1),
        ([1, 1, 1, 1], 1),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.findMin(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")