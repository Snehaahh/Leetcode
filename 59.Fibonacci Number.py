class Solution(object):
    def fib(self, n):
        if n==1:
            return 1
        if n==0:
            return 0
        prev1 = 0
        prev2 = 1
        for i in range(2,n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return prev2
