
class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        res = []
        nums.sort()

        i = 0
        while i < n - 3:
            l = i + 1

            while l < n - 2:
                r = l + 1
                j = n - 1

                while r < j:
                    total = nums[i] + nums[l] + nums[r] + nums[j]

                    if total == target:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        r += 1
                        j -= 1

                        while r < j and nums[r] == nums[r - 1]:
                            r += 1

                        while r < j and nums[j] == nums[j + 1]:
                            j -= 1

                    elif total < target:
                        r += 1
                    else:
                        j -= 1

                l += 1
                while l < n - 2 and nums[l] == nums[l - 1]:
                    l += 1

            i += 1
            while i < n - 3 and nums[i] == nums[i - 1]:
                i += 1

        return res
