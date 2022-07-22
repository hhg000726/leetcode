class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for i in sentences:
            answer = max(answer, len(i.split()))
        return answer