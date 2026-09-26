class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()
        for i,s in enumerate(strs):
            t = "".join(sorted(s))
            if t in my_dict:
                my_dict[t].append(s)
            else:
                my_dict[t] = [s]
        
        return list(my_dict.values())
        