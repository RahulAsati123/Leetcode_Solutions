class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = 10000000
        m = {}
        ans  =[]
        for i in range(len(list1)):
            m[list1[i]] = [i]
        
        for i in range(len(list2)):
            if list2[i] in m:
                m[list2[i]].append(i)
        
        print(m)
            
        for i in m.keys():
            if sum(m[i])<min_sum and len(m[i])==2:
                min_sum = sum(m[i])

        for i in m.keys():
            if sum(m[i]) == min_sum and len(m[i])==2:
                ans.append(i)
        return ans


        
        
        