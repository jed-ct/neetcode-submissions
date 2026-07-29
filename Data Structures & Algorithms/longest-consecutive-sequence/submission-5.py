class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset:set[int] = set(nums)
        highest_sequence_count = 1
        
        if len(nums) == 0:
            return 0

        for num in nums:
            if (num-1) in hashset:
                continue
            else:
                curr_sequence_count = 1
                num_increment = num + 1

                while num_increment in hashset:
                    num_increment += 1
                    curr_sequence_count += 1
                    if curr_sequence_count > highest_sequence_count:
                        highest_sequence_count = curr_sequence_count
            
        return highest_sequence_count

                    
                
        


            
        