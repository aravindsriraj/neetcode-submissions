class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            mp[temp].append(s)
        return list(mp.values())
        