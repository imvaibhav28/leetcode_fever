class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        nums.sort()
        # print (nums)
        for idx1 in range(len(nums)):
            # print("===================== \n")
            # print("IDX1 is ", idx1)
            if (nums[idx1] == nums[idx1-1] and idx1>0):
                # print("nums[idx1-1] ", nums[idx1])
                # print("nums[idx1-1] ", nums[idx1-1])
                continue
            
            idx2=idx1+1
            idx3=len(nums)-1
            
            # print("idx2 is ", idx2, " and idx3 is ", idx3)
            
            while (idx2<idx3):
                sum=nums[idx1] + nums[idx2] + nums[idx3]
                # print("SUms is",sum)
                
                if (sum== 0):
                    # print(nums[idx1]," ", nums[idx2] ," ", nums[idx3])
                    a.append([nums[idx1],nums[idx2],nums[idx3]])
                    idx3-=1
                    idx2+=1
                    while (idx2<idx3 and nums[idx3]==nums[idx3 +1]):
                        idx3-=1
                elif (sum<0):
                    idx2+=1
                
                else:
                    idx3-=1
        return a