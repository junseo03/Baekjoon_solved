import sys
import heapq
N = int(sys.stdin.readline())

left_heap = []
right_heap = []

k = int(sys.stdin.readline())
heapq.heappush(left_heap,(-k,k))
print(k)

for _ in range(N-1):
    
    k = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        if k <= right_heap[0][1]:
            heapq.heappush(left_heap, (-k,k))
        else: 
            heapq.heappush(right_heap, (k,k))
            p = heapq.heappop(right_heap)
            heapq.heappush(left_heap, (-p[0],p[1]))
    else:
        if k >= left_heap[0][1]:
            heapq.heappush(right_heap, (k,k))
        else:
            heapq.heappush(left_heap,(-k,k))
            p = heapq.heappop(left_heap)
            heapq.heappush(right_heap, (-p[0] , p[0]))
    
    print(left_heap[0][1])
