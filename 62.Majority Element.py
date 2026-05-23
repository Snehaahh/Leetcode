class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maxfreq = float('-inf')
        for n in nums:
            freq[n] = freq.get(n,0) + 1
            if freq[n] > maxfreq:
                maxfreq = freq[n]
                maxElement = n
        return maxElement
