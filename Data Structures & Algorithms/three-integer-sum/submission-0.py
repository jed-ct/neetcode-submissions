class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right] + nums[i]
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:     
                    left += 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if triplet not in result:
                        result.append(triplet)
                    left += 1
                    right -= 1
        return result
        
