# https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                len_nums -= 1
            else:
                i += 1


nums = [0, 0, 0 ,0 ,0 ,1]

test = Solution()
test.moveZeroes(nums)
print(nums)
