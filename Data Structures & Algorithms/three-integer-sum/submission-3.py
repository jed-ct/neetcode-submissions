#Intuition
'''
If the array is sorted, the sum from two pointers can be predicted (moving left will increase it, moving right will decrease it). We can fix one number and look for the other two using this.
'''

#Approach
'''
Sort the array, then use two pointers. For each element, Assign left to next index and right to the end. If sum > 0 we decrement right to decrease it, and if sum < 0 we increment left to increase it. 

If sum == 0, we store it in result and move both pointers. We then check for duplicates by moving to the next iteration/left pointer if repeated.
'''
#Complexity
'''
Time Complexity - O(n^2)
Space Complexity - O(1) if we ignore the result array
'''

#Code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:     
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result
        
