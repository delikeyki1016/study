class Solution:
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        # 예외사항 1칸 짜리 화단
        if flowerbed == [0]:
            flowerbed = [1]
            n -= 1
        # 1) 만약 맨 앞에 2칸이 0, 0 이면,
        if flowerbed[:2] == [0, 0]:
            # 2) 1, 0로 변경! n을 1 감소
            flowerbed[0] = 1
            print(flowerbed)
            n -= 1
        # 3) 만약 맨 뒤에 2칸이 0, 0 이면,
        if flowerbed[-2:] == [0, 0]:
            # 4) 0, 1로 변경! n을 1 감소
            flowerbed[-1] = 1
            n -= 1
        # 5) 1번째부터 -4번째까지 세칸을 기준으로 반복:
        for i in range(len(flowerbed[1:-3])):
            print(flowerbed[i+1:i+4])
            # 6) 세칸이 [0, 0, 0] 이면
            if flowerbed[i+1:i+4] == [0, 0, 0]:
                # 7) 가운데를 1로 변경! n을 감소
                flowerbed[i+2] = 1
                n -= 1
        # 8) 결과 반환
        return n <= 0
        
        
sol = Solution()
result = sol.can_place_flowers([0, 0], 2)
print(result)