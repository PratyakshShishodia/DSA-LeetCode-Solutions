class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zero = 0
        ans = 0
        for r in range (0,len(nums)):
            if nums[r] == 0:
                zero+=1
            
            while zero > k:
                if nums[l]==0:
                    zero -=1
                l+=1

            ans = max(ans,r-l+1)
        return ans
        