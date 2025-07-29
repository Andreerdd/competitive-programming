import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return nums

        count = collections.Counter(nums)
        sol = sorted(count.keys(), key=count.get, reverse=True)

        return sol[:k]


case = [1, 1, 2, 2, 2, 3]
k = 2
print(Solution().topKFrequent(case, k))