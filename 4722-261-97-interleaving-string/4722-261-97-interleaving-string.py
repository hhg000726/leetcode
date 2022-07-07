class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:  
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def func(s1, s2, s3):
            if s3 == "":
                return True
            if len(s1) * len(s2) > 0 and s1[0] == s2[0] == s3[0]:
                return func(s1[1:], s2, s3[1:]) or func(s1, s2[1:], s3[1:])
            else:
                if len(s1) > 0 and s1[0] == s3[0]:
                    return func(s1[1:], s2, s3[1:])
                elif len(s2) > 0 and s2[0] == s3[0]:
                    return func(s1, s2[1:], s3[1:])
                else:
                    return False
        return func(s1, s2, s3)
    #처음에는 dp만 머릿속에 박혀서 아무것도 떠오르지 않았다. 그러나 문제를 단계적으로 풀어가는 과정을 떠올리며 정리했다.
    #s3의 맨앞은 무조건 s1이나 s2의 맨앞과 같아야하고 그 맨앞을 제거하면서 같은 행동을 반복하여 모두 사라진다면 맞는 케이스일 것이다.
    #재귀를 활용해서 이를 반복했고 @cache를 이용해 중복되는 케이스들을 피했다.
