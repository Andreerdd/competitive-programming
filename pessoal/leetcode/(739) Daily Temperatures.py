from typing import List, override


class MySolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [] # Increasing Stack
        indexStack = [] # day of stack[i]
        result = [0 for _ in range(n)]

        # right to left
        for i in range(n-1, -1, -1):
            curr = temperatures[i]
            t = 1

            # while there's stack and the
            # current is greater than the top
            # one, we pop one
            while stack and curr >= stack[-1]:
                t += indexStack.pop()
                stack.pop()

            result[i] = t if stack else 0

            # add the new top
            stack.append(curr)
            indexStack.append(t)


        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res




case = [30,60,90]
print(Solution().dailyTemperatures(case))