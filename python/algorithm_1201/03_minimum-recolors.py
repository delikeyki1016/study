# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 첫 윈도우를 만든다
        window = blocks[:k]
        # 윈도우 내에 W 개수를 구하는 함수를 만든다.
        # def min_c(window):
        #     count = 0
        #     for j in range(len(window)):
        #         if window[j] == 'W':
        #             count += 1
        #     return count
        # 최소카운트는 첫 윈도우의 카운트로 셋팅
        # min_count = min_c(window)
        # count 이용
        min_count = window.count('W')

        # k번 인덱스부터 끝까지 돌려서 윈도우를 다시 만든다. 
        for i in range(k, len(blocks)):
            # 앞의 글자 하나 빼고, 그 다음 인덱스를 붙여 윈도우를 생성 
            window = window[1:] + blocks[i] 
            # 해당 윈도우의 카운트를 구함 
            count = window.count('W')
            # 최소카운트와 해당 카운트의 최소 카운트 구함 
            min_count = min(min_count, count)

        return min_count
    
sol = Solution()
blocks = "WBBWBBWBW"
k = 7
print(sol.minimumRecolors(blocks, k))