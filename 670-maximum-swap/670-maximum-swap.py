class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            m = int(num[i])
            change = -1
            for j in range(i + 1, len(num)):
                if (change == -1 and m < int(num[j])) or (change != -1 and m <= int(num[j])):
                    change = j
                    m = int(num[j])
            if change != -1:
                num = num[:i] + num[change] + num[i + 1:change] + num[i] + num[change + 1:]
                break
        return int(num)