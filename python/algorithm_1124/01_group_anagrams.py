# https://leetcode.com/problems/group-anagrams/ 

import collections

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list) # 일반 딕셔너리에서는 '없는 키'를 조회했을 때, 에러(Key Error)가 나기 때문에 사용함  
        for i in strs:
            # print(sorted(i), ''.join(sorted(i)), i)
            anagrams[''.join(sorted(i))].append(i)
        # print(anagrams)
        return list(anagrams.values())
        
strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

a = Solution()
print(a.groupAnagrams(strs))


# print(sorted("eat"))
# print(''.join(sorted("eat")))