class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            key=''.join(sorted(i))
            # print(key)
            res[key].append(i)
        return res.values()
            