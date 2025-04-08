class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        heap = []
        for word,count in freq.items():
            heapq.heappush(heap,(-count,word))
            #if len(heap) > k:
                #heapq.heappop(heap)
        #heap = sorted(heap, key=lambda x: -x[0])
        
        return [word for (neg_count,word) in heapq.nsmallest(k,heap)]
