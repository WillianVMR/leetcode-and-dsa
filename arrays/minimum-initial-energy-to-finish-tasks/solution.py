from typing import List


# Time: O(n log n) | Space: O(1)
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Get the difference from maximum effort to minimum effort
        def sort_key(x):
            return x[1] - x[0]

        # Sort the tasks based on size of effort variation between min and max
        tasks.sort(key=sort_key)

        ans = 0

        # Acumulator for answer
        for task in tasks:
            ans = max(ans + task[0], task[1])

        return ans


if __name__ == "__main__":
    s = Solution()

    tests = [
        ([[1, 2], [2, 4], [4, 8]], 8),
        ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32),
        ([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27),
    ]

    for i, (tasks, expected) in enumerate(tests):
        result = s.minimumEffort([t[:] for t in tasks])
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i + 1}: {status} | Input: {tasks} | Expected: {expected} | Got: {result}")
