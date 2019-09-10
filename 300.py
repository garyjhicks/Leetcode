class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0 
        dp = []
        for i in range(len(nums)):
            dp.append(0)
        
        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)+1
                
