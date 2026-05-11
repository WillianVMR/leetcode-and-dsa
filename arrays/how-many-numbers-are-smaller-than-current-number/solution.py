from typing import List
from collections import Counter

# Time: O(n log n) | Space: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        
        sorted_keys = sorted(counter.keys())
        
        response = [0 for i in range(len(nums))]

        
        storage = 0
        
        for key in sorted_keys:
            temp = counter[key]
            counter[key] = storage
            storage += temp
            
        for i in range(len(nums)):
            response[i] = counter[nums[i]]
            
        return response
        
        
        



if __name__ == "__main__":
    s = Solution()

    tests = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8], [2, 1, 0, 3]),
        ([7, 7, 7, 7], [0, 0, 0, 0]),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.smallerNumbersThanCurrent(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
