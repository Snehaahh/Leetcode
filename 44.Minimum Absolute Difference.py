class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff = float('inf')
        for i in range(1,len(arr)):
            min_diff = min(min_diff , abs(arr[i] - arr[i-1]))
        res = []
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1]) == min_diff:
                res.append([arr[i-1],arr[i]])
        return res
        
