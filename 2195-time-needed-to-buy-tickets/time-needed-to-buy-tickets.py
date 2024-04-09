class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time = 0
        # while tickets[k] !=0:
        #     for i in range(len(tickets)):
        #         if tickets[i]!=0:
        #             tickets[i]-=1
        #             time+=1
        #         if tickets[k]==0:
        #             return time
        
                
        # return time
        
        time = 0
        for i in range(len(tickets)):
            if i<k and tickets[i]>=tickets[k]:
                time+=tickets[k]
            elif i<k and tickets[i]<tickets[k]:
                time+=tickets[i]
            elif i==k:
                time+=tickets[i]
            elif i>k and tickets[i]>=tickets[k]:
                time+= tickets[k]-1
            elif i>k and tickets[i]<tickets[k]:
                time += tickets[i]
        return time