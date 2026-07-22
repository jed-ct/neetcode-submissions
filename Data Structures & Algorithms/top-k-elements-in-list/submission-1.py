class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map:dict[int,int] = {}
        bucket:list[list[int]] = []

        for i in range(0, len(nums) + 1):
            bucket.append([])

        for num in nums:
            if num in map:
                map[num] = map.get(num) + 1
            else:
                map[num] = 1

        result:list[int] = []

        for num,freq in map.items():
            bucket[freq].append(num)

        for arr in reversed(bucket):
            if arr == []:
                continue
            for nums in arr:
                result.append(nums)
                if len(result) == k:
                    return result
        return []
        