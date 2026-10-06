"""
https://leetcode.com/problems/two-sum/

Даны массив целочисленных значений nums и целое число target,
верните индексы двух таких чисел, которые в сумме равны target.

Гарантируется, что каждый ввод имеет ровно одно решение.
Также учтите, что вы не можете использовать одно и то же число дважды.
"""

class Solution:
    def bruteforce(self, nums: list[int], target: int) -> list[int] | None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def optimal(self, nums: list[int], target: int) -> list[int] | None:
        seen: dict[int, int] = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen.keys():
                return [seen[complement], i]
            seen[nums[i]] = i
        return None


sol = Solution()
print(sol.optimal([2, 7, 11, 15], 9))
print(sol.optimal([3, 2, 4], 6))
print(sol.optimal([3, 3], 6))
