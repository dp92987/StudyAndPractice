# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if num not in nums[0:index] and num not in nums[index + 1:]:
                return num
