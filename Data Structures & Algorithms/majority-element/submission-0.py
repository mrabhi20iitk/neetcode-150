class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i] +=1
            else: m[i] =1

        for i in nums:
            if m[i] > len(nums)//2:
                return i
        