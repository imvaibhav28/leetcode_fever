class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashtable = {}
        for i in range(0, len(nums)):
            if nums[i] in hashtable:
                # check for index difference
                if abs(i - hashtable[nums[i]]) <= k:
                    return True
            hashtable[nums[i]] = i
        return False
