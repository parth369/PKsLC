class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        result = []
        prev_char, prev_count = None, 0

        while max_heap:
            count,char = heapq.heappop(max_heap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))        

            prev_char, prev_count = char, count + 1
            print(result)
        
        return ''.join(result) if len(result) == len(s) else ""



                

            

        