#Intuition
'''
This problem deals with pairs of numbers. Furthermore, the height of the water depends on the smallest of the edge elements, so its better to look for other edge elements.
'''

#Approach
'''
Use two pointers algorithm. Calculate area, compare it to current max area, then move the left/right pointer if left/right value is smaller, respectively.
'''

#Complexity
'''
Time Complexity - O(n) since we only have to traverse the array once
Space Complexity - O(1) since we only store the left,right and max_area variables
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            if area > max_area:
                max_area = area
            
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
        return max_area
            