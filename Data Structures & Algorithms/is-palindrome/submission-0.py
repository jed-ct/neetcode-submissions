import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            char_left = s[left]
            if not char_left.isalnum():
                left += 1
                continue
            
            char_right = s[right]
            if not char_right.isalnum():
                right -= 1
                continue

            if char_left.lower() != char_right.lower():
                return False

            left += 1
            right -= 1
        return True


            
            