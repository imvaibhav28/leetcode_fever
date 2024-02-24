class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res=[]
        keyvalue={}
        for i in range(len(nums)):
            diff= target - nums[i]
            # print(diff,' for a =',nums[i])
            if diff in keyvalue:
                res.append(i)
                res.append(keyvalue[diff])
                break
            keyvalue[nums[i]]=i
            # print(keyvalue)
        return res