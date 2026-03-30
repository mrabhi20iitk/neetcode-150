class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        nums = sorted(set(nums))
        res = 1
        tmp = 0
        i , j = 0,1
        while j < len(nums):
            if nums[j] == nums[i] +1 :
                res = max(res, j - tmp +1)
            else:
                tmp = j
            i = j
            j+=1
        return res