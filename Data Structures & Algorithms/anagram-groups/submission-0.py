class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p={}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in p:
                p[key] = []
            p[key].append(i)
        return list(p.values())
