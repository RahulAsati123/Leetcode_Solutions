class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        box = set()
        box2 = set()
        for i in s:
            box2.add(i)
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        ans = []
        for i in order:
            if i in box2:
                box.add(i)
                for j in range(m[i]):
                    ans.append(i)
        for i in s:
            if i not in box:
                ans.append(i)
        return "".join(ans)
        

        