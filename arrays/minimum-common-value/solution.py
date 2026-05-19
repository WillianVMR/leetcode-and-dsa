from typing import List


# Time: O(n + m) | Space: O(1)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([1, 2, 3], [2, 4], 2),
        ([1, 2, 3, 6], [2, 3, 4, 5], 2),
        ([1, 2, 3], [4, 5, 6], -1),
    ]

    for i, (nums1, nums2, expected) in enumerate(tests):
        result = s.getCommon(nums1, nums2)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {nums1}, {nums2} | Expected: {expected} | Got: {result}")
