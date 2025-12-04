class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        dic = {}
        for i,n in enumerate(temp):
            if n not in dic:
                dic[n] = i
        res = []
        for num in nums:
            res.append(dic[num])
        return res
        
