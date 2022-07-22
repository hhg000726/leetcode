class Solution:
    answer = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        def func(a, b, s):
            if a > 0:
                func(a - 1, b + 1, s + "(")
            if b > 0:
                func(a, b - 1, s + ")")
            if a == 0 and b == 0:
                self.answer.append(s)
        func(n, 0, "")
        return self.answer