# https://leetcode.com/problems/two-sum/


class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
                for j in range(len(nums)):
                    if nums[i] + nums[j] == target and i != j:
                        return i, j

class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
