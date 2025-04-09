class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        time = 0
        while max_heap:
            cycle = n + 1
            temp = []
            while cycle > 0 and max_heap:
                if -max_heap[0] > 1:
                    temp.append(heapq.heappop(max_heap) + 1)
                else:
                    heapq.heappop(max_heap)
                time += 1
                cycle -= 1
            
            for count in temp:
                heapq.heappush(max_heap, count)
            
            if max_heap:
                time += cycle  # Idle slots
        
        return time    