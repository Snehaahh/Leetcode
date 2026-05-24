class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for char in ransomNote:
            freq[char] = freq.get(char,0) + 1
        for ch in magazine:
            if ch in freq:
                freq[ch] = freq.get(ch) - 1
        for value in freq.values():
            if value>0:
                return False
        return True
