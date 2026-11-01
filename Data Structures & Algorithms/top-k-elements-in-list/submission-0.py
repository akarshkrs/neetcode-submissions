from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            mydict[i] = 1 + mydict.get(i, 0)

        sorted_items = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in sorted_items[:k]]
