class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre , post = [1]*n , [1]*n

        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i-1]
            post[n-1-i] = post[n-i]*nums[n-i]

        return [pre[i]*post[i] for i in range(n)]        