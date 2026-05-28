class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        while strs:
            word = strs[0]
            sublist = [word]
            for word2 in strs[1::]:
                if sorted(word2) == sorted(word):
                    sublist.append(word2)

            output.append(sublist)
            for item in sublist:
                strs.remove(item)

        return output
        
        
                