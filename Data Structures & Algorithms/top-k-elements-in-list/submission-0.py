class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i in m:
                m[i] +=1
            else: m[i] = 1

        tmp = sorted(m.items(),key= lambda x : x[1], reverse = True)
        res = [i[0] for i in tmp][:k]
        return res


        