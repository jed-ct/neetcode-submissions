class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map:dict[int,int] = {}
        bucket:list[list[int]] = []
        result:list[int] = []

        #Initialize bucket
        for i in range(0, len(nums) + 1):
            bucket.append([])

        #Map the numbers to their frequency
        for num in nums:
            if num in map:
                map[num] = map.get(num) + 1
            else:
                map[num] = 1

        #Store the numbers in the bucket with their frequency as their index
        for num,freq in map.items():
            bucket[freq].append(num)

        #Iterate through the backwards, appending k numbers to result
        for arr in reversed(bucket):
            if arr == []:
                continue
            for nums in arr:
                result.append(nums)
                if len(result) == k:
                    return result
        return []
        