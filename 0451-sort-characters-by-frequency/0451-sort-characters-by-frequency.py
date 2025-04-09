class Solution:
    def frequencySort(self, s: str) -> str:
        charc_freq = defaultdict(int)
        for charc in s:
            charc_freq[charc] += 1
        print(charc_freq)
        heap = []
        for char,count in charc_freq.items():
            heapq.heappush(heap,(-count, char))
        result = []
        while heap:
            neg_count, char = heapq.heappop(heap)
            result.append(char * -neg_count)
        
        return ''.join(result)