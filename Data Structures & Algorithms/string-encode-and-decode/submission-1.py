class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string:str = ""
        for strings in strs:
            encoded_string = encoded_string + strings + "ñ"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs:list[str] = []
        word:str = ""
        for char in s:
            if char == "ñ":
                strs.append(word)
                word = ""
            else: 
                word = word + char
        return strs
            