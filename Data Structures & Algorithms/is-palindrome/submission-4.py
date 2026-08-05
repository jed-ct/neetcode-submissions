#Intuition
''' Since a palindrome is the same string forward and backward, we can iterate through the string from the left and the right, checking each character if they are equal '''

#Approach
''' 
Use two pointer algorithm to iterate through the string, skipping if it is not an alphanumeric character and checking if the lowercase chars are equal
'''

#Complexity
''' 
Time complexity - O(n) since we iterate through the array once
Space complexity - O(1) since we only store four variables (the pointers and their characters)
'''

#Code
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


            
            