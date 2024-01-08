class Solution:
    def minimum_recolors(self, blocks: str, k: int) -> int:
        middle_str = blocks[:k]
        result = middle_str.count('W')

        for i in range(k, len(blocks)):
            middle_str = middle_str[1:] + blocks[i]
            if middle_str.count("W") == 0:
                result = 0
            # elif blocks[i] == "W":
            #     print("블록스의아이", i)
            elif middle_str.count("W") < result:
                result = middle_str.count("W")
        return result

sol = Solution()
print(sol.minimum_recolors('WBBWBBWBW', 7))