class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict:dict[int, int] = {};
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[nums[i]] = i
