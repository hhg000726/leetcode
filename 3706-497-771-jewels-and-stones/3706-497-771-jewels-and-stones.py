class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    answer += 1
        return answer