class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        for i in range(len(matches)):
            if matches[i][0] not in win:
                win[matches[i][0]] =1 
            else:
                win[matches[i][0]] +=1

        for i in range(len(matches)):
            if matches[i][1] not in lose:
                lose[matches[i][1]] =1 
            else:
                lose[matches[i][1]] +=1
        arr = []
        ans = []
        for i in win.keys():
            if i not in lose:
                arr.append(i)
        
        ans.append(sorted(arr))
        arr = []
        
        for i in lose.keys():
            if lose[i]==1:
                arr.append(i)
        
        ans.append(sorted(arr))
        return ans


        

        