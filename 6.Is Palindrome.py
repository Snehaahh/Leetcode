class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for char in s:
            if char.isalnum():
                rev+=char.lower()
        return rev==rev[::-1]
                
