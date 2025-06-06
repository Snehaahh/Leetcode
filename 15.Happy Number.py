class Solution:
    def isHappy(self, n: int) -> bool:
        hashset=set()
        while n not in hashset:
            hashset.add(n)
            n=self.helper(n)
            if n==1:
                return True
        return False
    def helper(self,n:int) -> int:
            s=0
            while n:
                rem=n%10
                s+=rem*rem
                n=n//10
            return s
