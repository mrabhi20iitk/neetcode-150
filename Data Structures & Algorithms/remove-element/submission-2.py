class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for i in nums:
            if i == val:
                continue
            res.append(i)

        for i in range(len(res)):
            nums[i] = res[i]

        return len(res)        