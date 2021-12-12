import queue

data_queue = queue.Queue()

data_queue.put("funcoding")
data_queue.put(1)
print(data_queue.qsize())

print(data_queue.get())
print(data_queue.qsize())

p_queue = queue.PriorityQueue()
p_queue.put((10, "korea"))
p_queue.put((1, "나는 첫번째"))
p_queue.put((0, '나는 0번째'))
p_queue.put((-1, '나는 -1'))
print(p_queue.get())

# Lifo Queue가 정책으로 구현되어있다.
# 근데 Lifo Queue면 그냥 스택 아니냐?