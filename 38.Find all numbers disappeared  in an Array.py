class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        for i,num in enumerate(nums):
            if num>0:
                res.append(i+1)
        
        return Ares
        
