from typing import List


# Time: O() | Space: O()
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        response = []
        
        for num in nums:
            digits = []
            while num > 0:
                digits.append(num % 10)
                num //= 10
            response.extend(digits[::-1])
        
        return response
            
            

if __name__ == "__main__":
    s = Solution()

    tests = [
        ([13, 25, 83, 77], [1, 3, 2, 5, 8, 3, 7, 7]),
        ([7, 1, 3, 9], [7, 1, 3, 9]),
    ]

    for i, (nums, expected) in enumerate(tests):
        result = s.separateDigits(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums} | Expected: {expected} | Got: {result}")
