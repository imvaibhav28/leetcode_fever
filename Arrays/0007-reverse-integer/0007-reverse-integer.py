class Solution:
    
    def reverse(self, x: int) -> int:
        MAX_INT=2147483647
        if x<0:
            res= int(str(-1*x)[::-1])
            if res<=MAX_INT:
                return -1*res
            return 0
        if x>=0:
            res= int(str(x)[::-1])
            if res<=MAX_INT:
                return res
            return 0
        # if x == 0:
        #     return 0