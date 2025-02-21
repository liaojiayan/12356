import heapq

# 创建一个空的最小堆
min_heap = []

# 向最小堆中添加元素
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

# 打印最小堆
print("最小堆:", min_heap)

# 从最小堆中弹出最小元素
min_element = heapq.heappop(min_heap)
print("弹出的最小元素:", min_element)

# 打印弹出后的最小堆
print("弹出后的最小堆:", min_heap)
