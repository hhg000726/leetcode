class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for i in operations:
            if "++" in i:
                answer += 1
            else:
                answer -= 1
        return answer