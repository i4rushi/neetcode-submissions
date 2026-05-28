class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for idx,num in enumerate(nums):
            t = target - num
            if t == num:
                output.append(idx)
                continue
            if t in nums:
                return [idx,nums.index(t)] 
        return output   
