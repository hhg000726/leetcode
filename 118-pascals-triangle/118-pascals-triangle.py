class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for i in range(1, numRows):
            answer.append([1])
            for j in range(1, i):
                answer[i].append(answer[i - 1][j - 1] + answer[i - 1][j])
            answer[i].append(1)
        return answer