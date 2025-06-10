class Solution:
    def reverse(self, x: int) -> int:
        res=0
        MAX=2147483647
        MIN=-2147483648 
        while x:
            num=int(math.fmod(x,10))
            if (res > MAX/10) or (res < MIN/10):
                return 0
            elif (res == MAX/10) and (num > MAX%10):
                return 0
            elif (res == MIN/10) and (num < MIN%10):
                return 0
            else:
                res=res*10+num
            x=int(x/10)
        return res
