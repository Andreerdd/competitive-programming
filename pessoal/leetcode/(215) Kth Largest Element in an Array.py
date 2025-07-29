from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


case = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(case, k))
