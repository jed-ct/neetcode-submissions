class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map:dict[tuple[int,...], list[str]] = {}
        for string in strs:
            position_array:list[int] = [0] * 26
            position_tuple: tuple[int, ...] = ()
            for char in string:
                position:int = ord(char.lower()) - 97
                position_array[position] = position_array[position] + 1
                position_tuple = tuple(position_array)

            if position_tuple in map:
                map[position_tuple].append(string)
            else:
                map[position_tuple] = [string]

        return list(map.values())


        