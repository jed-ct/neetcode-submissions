class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_list:list[int] = []
        r_list:list[int] = []
        result_list:list[int] = []

        for i in range(0, len(nums)):
            if i == 0:
                l_list.append(1)
            else:
                l_list.append(nums[i-1] * l_list[i-1])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                r_list.append(1)
            else:
                r_list.append(nums[i+1] * r_list[len(r_list) - 1])
        
        r_list.reverse()

        for i in range(0, len(l_list)):
            result_list.append(l_list[i] * r_list[i])
        
        return result_list


            

        