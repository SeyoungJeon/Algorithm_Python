## Heap

- 우선순위 큐
- 최솟값 혹은 최댓값을 계속해서 호출해야 하는 경우, Heap 구조는 시간 측면에서 굉장히 효율적
- 기본적으로 **Min-priority-queue**

```python
import heapq
```



#### 기존 배열을 Heap 구조로 변경 - heapify()

```python
test_list = [1,3,2,6,8,0,6]
heapq.heapify(test_list)
```



#### Heap 요소 추가 - heappush(list_name, element)

```python
test_list = []
heapq.heappush(test_list, 3)
heapq.heappush(test_list, 5)
heapq.heappush(test_list, 1)
```



#### Heap 요소 삭제 - heappop(list_name)

- 요소를 삭제하면서 반환 값으로 받음

```python
test_list = []
heapq.heappush(test_list, 3)
heapq.heappush(test_list, 5)
heapq.heappush(test_list, 1)

heapq.heappop(test_list)
heapq.heappop(test_list)
```



#### Heap 최소 또는 최대값 얻기

```python
heap[0]
```



#### MaxHeap 구현

- \- (minus) 연산자 이용 

```python
test_list = [3,5,2,4,1]
test_heap = []
for value in test_list:
    heapq.heappush(test_heap, -value)
```



#### Heap에서 tuple 사용

- 첫 번째 요소를 기준으로 정렬

```python
test_list = [3,5,2,4,1]
test_heap = []
for value in test_list:
    heapq.heappush(test_heap, (-value,3))

heapq.heappop(test_heap)[1]
```

