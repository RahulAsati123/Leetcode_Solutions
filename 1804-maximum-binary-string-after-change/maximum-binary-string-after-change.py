class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        leading_one, count_zero, count_one  = 0, 0, 0
        for x in binary:
            if x == '1':
                count_one+=1
                if not count_zero:
                    leading_one+=1
            else:
                count_zero+=1
         
        if count_zero > 1:
            return '1'*(leading_one+count_zero-1)+'0'+'1'*(count_one-leading_one)
        else:
            return binary