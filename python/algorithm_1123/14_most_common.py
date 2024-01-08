# https://leetcode.com/problems/most-common-word
# banned 문자를 제외한 단어 중 제일 빈도가 높은 단어 리턴

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import re, collections
        
        # paragraph = re.sub(r"[^a-zA-Z,\s]", "", paragraph) #\W : 알파벳,숫자가 아닌 것들을 매치 
        # p_list = paragraph.lower().replace(',', ' ').split()
        
        # if banned:
        #     for j in banned:
        #         while j in p_list:
        #             p_list.remove(j)
        
        p_list = re.sub(r"[\W]", " ", paragraph.lower()).split()
        result_list = [i for i in p_list if banned not in p_list]
                
        word = collections.Counter(result_list).most_common(1)
        
        return word[0][0]

paragraph = "abc abc? abcd the jeff!"
banned = ['a', 'the'] 

a = Solution()
print(a.mostCommonWord(paragraph, banned))