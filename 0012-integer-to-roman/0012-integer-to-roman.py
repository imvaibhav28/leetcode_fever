class Solution:
    def intToRoman(self, num: int) -> str:
        dictionary = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

        # given an integer
        # is it similar to denomination?
        rev = str(num)
        int_num = int(rev)
        res=''
        for i in range(len(rev)):
            place_value = int_num%(10**(i+1))
            # print(place_value,10**i+1)
            denom = place_value - int_num%(10**(i))
            # print(denom)
            # if (denom + 1 in dictionary.keys()) or (denom + 10 in dictionary.keys()) or (denom+100 in dictionary.keys()):
            if (denom + (10**(i)) in dictionary.keys()) and  denom!=0:
                # print("subtract ",(10**(i)),"from",denom + (10**(i)))
                res=res+dictionary[denom + (10**(i))]+dictionary[(10**(i))]
                # print(res)
            else:
                # print('add',denom,10**(i))
                if denom in dictionary.keys(): res=res+dictionary[denom]
                else:
                    # divide it further
                    temp=denom
                    while temp!=0:
                        res=res+dictionary[10**(i)]
                        temp=temp-10**(i)
                        if temp in  dictionary.keys():
                            res=res+dictionary[temp]
                            temp=0
                    # pass
                # print(res)
                
        return res[::-1]