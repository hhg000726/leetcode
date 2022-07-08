#처음 이 문제를 봤을때 모든 substring을 테스트하는 방법밖에 생각나지 않았고 더 나은 해결 방법을 찾지 않으면 답답함이 안풀릴 것 같아 찾아봤다.
#대부분 DP를 활용한다고 하는데 어디서부터 접근해야할지 막막했다. 코드를 봐도 무슨말인지 모르겠고 그래서 천천히 생각해봤다.
#Palindromic String이 되려면 어떻게 해야하나? 처음과 끝이 같은 문자이고 그 사이의 문자열이 Palindromic String이면 된다.
#사이의 문자열이 Palindromic String인지만 dp로 저장하고 짧은 문자열부터 처음과 끝 문자가 같다면 그 사이의 dp값만 확인해주면 된다.
#예외상황으로 문자열의 길이가 3이하인 경우는 처음과 끝이 같다면 무조건 해당되므로 첫 조건으로 따로 or 연산으로 예외처리 해준다.
#그리고 dp값이 채워질때마다 답을 갱신해주면 된다!

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        answer = ""

        for i in range(len(s)):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    if i < 3 or dp[j + 1][j + i - 1] == True:
                        dp[j][j + i] = True
                        if i + 1 > len(answer):
                            answer = s[j:j + i + 1]
        return answer
