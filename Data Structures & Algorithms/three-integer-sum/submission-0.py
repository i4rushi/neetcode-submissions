class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    out.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j = j + 1
                    while j<k and nums[k] == nums[k-1]:
                        k = k - 1
                    j = j + 1
                    k = k - 1
                elif val > 0:
                    k = k - 1
                elif val < 0:
                    j = j + 1

        return out
            