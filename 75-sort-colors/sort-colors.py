class Solution(object):
    def sortColors(self, nums):
       l = 0
       n = len(nums)
       m = 0
       r = n-1
       while m <= r:
        if nums[m] == 0:
          nums[m],nums[l] = nums[l],nums[m]
          l+=1
          m+=1
        elif nums[m]==1:
          m+=1
        else:
          nums[m],nums[r] = nums[r],nums[m]
          r-=1
    
        