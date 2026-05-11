from typing import List


# Time: O(n) | Space: O(n)
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         response = []
#         nums_set = set(nums) # Set lookups are O(1) instead of O(n) of a lookup in array
#         for i in range(1, len(nums) + 1):

#             if i not in nums_set:
#                 response.append(i)

                
#         return response



# This one use kind of a hashmap strategy to don't have to create a set of the array
# That saves load another array in memory
# Time: O(n) | Space: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for num in nums:
            nums[abs(num) - 1] = - abs(nums[abs(num) - 1])
        
        response = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                response.append(i + 1)
                         
        return response

if __name__ == "__main__":
    s = Solution()

    tests = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.findDisappearedNumbers(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")