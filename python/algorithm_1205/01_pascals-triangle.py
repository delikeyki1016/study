# https://leetcode.com/problems/pascals-triangle/
# 바텀업 방식
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # [세팅] numRows개 요소로 구성된 이중 리스트 생성 및 양쪽 끝 값 1로 초기화
        temp_list = [[0] * (i + 1) for i in range(numRows)]
        for i in temp_list:
            i[0] = 1
            i[-1] = 1
        print(temp_list)
        
        # 원하는 곳까지 데이터를 누적하여 저장 (활용 가능)
        for row in range(2, numRows):
            for col in range(1, row):
                temp_list[row][col] = temp_list[row-1][col-1] + temp_list[row-1][col]
                print(temp_list[row])
        return temp_list

sol = Solution()
numRows = 5
print(sol.generate(numRows))

# 탑다운 방식
# class Solution:
#     def generate(self, numRows: int) -> list[list[int]]:
#         # 탈출 조건
#         if numRows ==  1:
#             return [[1]]
#         # 이전까지의 파스칼의 삼각형 가져오기 (triangle)
#         triangle = self.generate(numRows-1)
#         # 이전까지의 파스칼의 삼각형에서 가장 마지막 줄 가져오기 (prev)
#         prev = triangle[-1]
#         new_row = []
#         new_row.append(1)
#         for i in range(1, len(prev)):
#             new_row.append(prev[i-1] + prev[i])
#         new_row.append(1)
#         triangle.append(new_row)
#         print(triangle)
#         return triangle

# sol = Solution()
# numRows = 5
# print(sol.generate(numRows))
