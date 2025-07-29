from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []

        heap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while len(pairs) < k:
            val, i, j = heapq.heappop(heap)

            # add in answer
            pairs.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))


        return pairs



nums1 = [1,1,2]
nums2 = [1, 2, 3]
k = 2
print(Solution().kSmallestPairs(nums1, nums2, k))