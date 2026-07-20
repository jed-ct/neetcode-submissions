class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s : dict[str,int] = {}
        letters_t : dict[str,int] = {}

        for char in s:
            count = letters_s.get(char) if not None else 1
            if (char in letters_s):
                letters_s.update({char : count + 1})
            else: 
                letters_s.update({char : 1})

        for char in t:
            count = letters_t.get(char) if not None else 1
            if (char in letters_t):
                letters_t.update({char : count + 1})
            else: 
                letters_t.update({char : 1})

        return letters_s == letters_t