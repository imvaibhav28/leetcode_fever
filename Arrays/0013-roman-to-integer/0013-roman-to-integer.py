class Solution:
    def romanToInt(self, s: str) -> int:
        rev = s[::-1]
        res=0 
        # print(rev)
        map={'I':1,'V':5,
        'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        for _ in range(len(rev)):
            # check for subtraction
            # print('i = ',i,' for char ',rev[:i+1])
            if i < len(rev)-1 and map[rev[i+1]]<map[rev[i]]:
                res=res+(map[rev[i]]-map[rev[i+1]])
                # print('RES',res)
                i=i+2
            elif i < len(rev)-1 and map[rev[i+1]]>=map[rev[i]]:
                res=res+map[rev[i]]
                # print('Res',res)
                i=i+1
            elif i==len(rev)-1:
                res=res+map[rev[i]]
                i=i+1
            
        return res  