class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(s)
        for i in range(len(indices)):
            source = sources[i]
            index = indices[i]
            target = targets[i]
            s_substring = s[index:index+len(source)]
            if s_substring == source:
                ans[index] = target
                for ans_i in range(index+1, index+len(source)):
                    ans[ans_i] = ''

        return ''.join(ans)