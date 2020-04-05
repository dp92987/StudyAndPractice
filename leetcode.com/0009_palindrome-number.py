# https://leetcode.com/problems/palindrome-number/solution/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
