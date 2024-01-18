class Solution:
    def distance(self,x1,y1,x2,y2):
        return ((y2-y1)**2 + (x2-x1)**2)**(1/2)
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        count = 0
        ans = []
        for i in range(len(queries)):
            for j in range(len(points)):
                if self.distance(queries[i][0],queries[i][1],points[j][0],points[j][1]) <= queries[i][2]:
                    count+=1
            ans.append(count)
            count = 0
        return ans
                    

