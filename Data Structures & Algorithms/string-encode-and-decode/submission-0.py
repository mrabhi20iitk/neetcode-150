class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for i in strs:
            sizes.append(len(i))
        res = ''
        for i in sizes:
            res += str(i)
            res+= ","
        res+='#'
        for i in strs:
            res+=i
        return res
        

    def decode(self, s: str) -> List[str]:
        sizes = []
        i = 0
        while s[i] != '#':
            curr = ""
            while s[i] != ',':
                curr+=s[i]
                i+=1
            sizes.append(int(curr))
            i+=1
        i+=1
        res = []
        for j in sizes:
            res.append(s[i:i+j])
            i+=j

        return res

