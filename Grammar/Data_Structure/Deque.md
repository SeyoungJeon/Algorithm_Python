## Deque



#### deque란

- 양방향에서 데이터 처리할 수 있는 queue형 자료구조

- front (앞) , rear (뒤)



#### maxlen

- 고정 크기 큐를 생성함
- 큐가 꽉 찬 상태에서 새 원소를 넣으면 첫 원소가 자동으로 삭제

```python
cache_list = deque(maxlen=cacheSize)
```



#### append

- list.append(x)와 마찬가지로 deque의 오른쪽(마지막)에 원소 추가

```python
import collections

deq = collections.deque(['a','b','c'])
deq.append('d')

# 출력
deque(['a','b','c','d'])
```



#### appendleft

- deque의 왼쪽(앞)에 원소 추가

```python
import collections

deq = collections.deque(['a','b','c'])
deq.appendleft('d')

# 출력
deque(['d','a','b','c'])
```



#### extend

- 오른쪽(마지막)에 elements를 추가

```python
# collections.deque
deq = collections.deque(['a', 'b', 'c'])
deq.extend('d')

# 출력
deque(['a', 'b', 'c', 'd'])
```



#### extendleft

- 왼쪽(앞)에 elements를 추가

```python
deq = collections.deque(['a', 'b', 'c'])
deq.extendleft('de')

# 출력
deque(['e', 'd', 'a', 'b', 'c']) - 거꾸로 삽입되는 것을 확인할 수 있음
```



#### pop

- 오른쪽(마지막)에서부터 원소 제거 및 값 반환

```python
deq = collections.deque(['a', 'b', 'c'])
deq.pop()

# 출력
deque(['a','b'])
```



#### popleft

- 왼쪽(앞쪽)에서부터 원소 제거 및 반환

```python
deq = collections.deque(['a', 'b', 'c'])
deq.popleft()

# 출력
deque(['b','c'])
```



#### rotate(n)

- 요소들(elements)를 값만큼 회전
- n 값이 음수이면 왼쪽으로 회전, 양수이면 오른쪽으로 회전

```python
deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.rotate(1)

# 출력
e a b c d

deq2 = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq2.rotate(-1)

# 출력
b c d e a
```



#### remove(element)

- 해당 원소 삭제

```python
deq = collections.deque(['a', 'b', 'c', 'd', 'e'])
deq.remove('b')

# 출력
deque(['a','c','d','e'])
```

