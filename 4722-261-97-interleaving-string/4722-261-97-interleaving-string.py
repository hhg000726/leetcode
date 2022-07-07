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