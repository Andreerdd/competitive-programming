class Solution:
    def calcHappy(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        # obtém a soma
        sum = 0
        for c in str(n):
            sum += int(c)**2

        return sum

    def isHappy(self, n: int, _fast=None) -> bool:
        if n == 1 or _fast == 1: return True
        slow = self.calcHappy(n)
        fast = 0
        if _fast is None:
            fast = self.calcHappy(self.calcHappy(n))
        else:
            fast = self.calcHappy(self.calcHappy(_fast))
        if slow == fast and slow != 1:
            return False
        elif fast == 1:
            return True
        else:
            return self.isHappy(slow, fast)


n = 10
print(Solution().isHappy(n))
