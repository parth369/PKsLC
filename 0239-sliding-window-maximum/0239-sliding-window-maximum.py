class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #Brut force
        #return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
        q = deque()
        result = []
        for i,num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
            if i >= k-1:
                result.append(nums[q[0]])
        return result
        