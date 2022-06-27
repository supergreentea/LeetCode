#User function Template for python3

class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        heap = a[: k + 1] # min heap with first k + 1 elements
        heapq.heapify(heap)
        
        left = 0
        right = k
        
        while left < n:
            min_val = heapq.heappop(heap)
            a[left] = min_val
            
            left += 1
            if right + 1 < n:
                right += 1
                heapq.heappush(heap, a[right])
        
        return a
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends