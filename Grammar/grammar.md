## Python Grammar



### 주의!!

- C++ 혹은 Java 처럼 코드를 작성하지 말기



#### 용어

- iterable : 자신의 멤버를 하나씩 리턴할 수 있는 객체 (list, str, tuple, dict)
- sequence: int 타입 인덱스를 통해, 원소에 접근할 수 있는 iterable (list, str, tuple)





#### map 

- list(map(함수, 리스트))
- tuple(map(함수, 튜플))

```python
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
# [1,2,3,4]

a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int,a))
# [1,2,3,4]
```

- map에는 리스트뿐만 아니라 반복 가능한 모든 객체 넣을 수 있음



#### 몫과 나머지 - divmod

- 정수를 나눈 몫과 나머지를 구하는 함수

```python
a,b = 7,5
print(a//b, a%b)

print(*divmod(a, b))
```

- divmod를 사용하는게 무조건 좋은 방법은 아님
  - 작은 숫자를 다룰 때는 divmode는 a//b, a%b 보다 느리다.
  - 큰 숫자를 다룰 때는 divmode가 더 빠름



#### string 숫자 n 진법 변환

- 문자열 숫자 n 진법 변환

```python
num = '3212'
base = 5
print(int(num,base))

# 기본 풀이
answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * (base ** idx)
```



#### range, enumerate 

- range([start], stop [,step])

  - 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴

  ```python
  print(range(5), type(range(5)))
  print(tuple(range(5)))
  print(set(range(5)))
  print(list(range(5)))
  
  # 출력
  range(0, 5) <class 'range'>
  (0, 1, 2, 3, 4)
  {0, 1, 2, 3, 4}
  [0, 1, 2, 3, 4]
  ```

- enumerate

  - 순서와 리스트의 값을 전달
  - 순서가 있는 자료형(list,set,tuple,dictionary,string)

  ```python
  data = enumerate((1,2,3))
  print(data, type(data))
  
  for idx, value in data:
      print(i, ":", value)
  
  # 출력
  <enumerate object at 0x0000000002424EA0> <class 'enumerate'>
  0 : 1
  1 : 2
  2 : 3
  ```

  

#### 문자열 정렬하기

- ljust
- center
- rjust

```python
s = '가나다라'
n = 7

s.ljust(n) 	# 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) 	# 우측 정렬
```



#### 알파벳 출력

- 파이썬은 해당 스트링을 상수(constants)로 정의

```python
import string

string.ascii_lowercase # 소문자 abcdefg...
string.ascii_uppercase # 대문자 ABCDEFGH....
string.ascii_letters # 대소문자 모두 abcdefg....ABCDEF....
string.digits # 숫자 0123456789
```



#### 리스트 정렬 - sorted

- sort() 함수로 리스트 원소 정렬할 수 있음
- 원본의 순서는 변경하지 않고, 정렬된 값을 구하기 위해선

```python
# 보통 다른 언어에서는..
list1 = [3,2,1]
list2 = [i for i in list1]
list2.sort()

# python 에서는..
list1 = [3,2,1]
list2 = sorted(list1)
```



#### 2차원 리스트 뒤집기 - zip

- zip과 unpacking을 이용함

```python
mylist = [[1,2,3],[4,5,6],[7,8,9]]
new_list = list(map(list, zip(*mylist)))
```



#### zip

- zip(*iterables)는 각  iterables의 요소들을 모으는 이터레이터를 만듦
- 튜플의 이터레이터를 반환하는데, i 번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i 번째 요소를 포함

```python
mylist = [1,2,3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print(i)

# 출력
(1, 40)
(2, 50)
(3, 50)

animals = ['cat','dog','lion']
sounds = ['meow', 'woof', 'roar']
anmswer = dict(zip(animals, sounds))

# 출력
{'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```



#### packing과 unpacking

- packing

  - \* 한개를 매개변수 앞에 붙임으로 사용
  - 여러개의 값을 하나의 객체로 합쳐서 받을 수 있도록 함

  ```python
  def print_family_name(*parents, **sibling):
        print("아버지 :", parents[0])
        print("어머니 :", parents[1])
        if sibling:
             print("호적 메이트..")
             for title, name in sibling.items():
                   print('{} : {}'.format(title, name))
  
  print_family_name("홍길동", '심사임당', 누나='김태희', 여동생='윤아')
  
  # 출력
  아버지 : 홍길동
  어머니 : 심사임당
  호적 메이트..
  누나 : 김태희
  여동생 : 윤아
  ```

- unpacking

  - 여러개의 객체를 포함하고 있는 하나의 객체를 풀어줌
  - 매개변수에 \*을 붙이는 것이 아니라 인자 앞에 \*을 붙여서 사용
  - 함수 호출 시, 인자를 해체하는 개념이므로, 해체된 결과가 함수의 매개변수에 갯수와 다르면 에러 발생

  ```python
  def cal(first, op, second):
      if op == '+':
          return first + second
      if op == '/':
          return first / second
      if op == '-':
          return first - second
      if op == '*':
          return first * second
  
  prob = {
    'first': 12,
    'second': 34,
    'op': '*'
  }
  
  cal(**prob) # 결과 : 408
  
  # 아래와 같이 동작
  1. cal(**prob)
  2. cal(prob = {
    'first': 12,
    'second': 34,
    'op': '*'
  })
  3. cal(first=12, second=34, op='*')
  ```



#### 곱집합(Cartesian product) - product

- 'ABCD', 'xy'의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy

```python
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)
```



#### 2차원 리스트 1차원 리스트로 만들기 - from_iterable

```python
my_list = [[1, 2], [3, 4], [5, 6]]

answer = sum(my_list, [])
```



#### 순열과 조합 - combinations, permutations

```python
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools,permutations(pool))))
print(list(map(''.join, itertools.permuations(pool, 2))))
```



#### collections - Counter

- 해당 원소에 대한 개수를 dictionary 형식으로 반환

```python
from collections import Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
counter = Counter(my_list)

# O(N) 소요
for i in range(1, 10):
    print(counter[i])
```

- Counter 클래스는 원소 접근 시 시간 복잡도 O(1)
- list.count 사용 시 시간복잡도는 O(N)이므로 count를 여러번 해야하는경우에는 list가 아니라 Counter 클래스를 사용하기



#### for문과 if문을 한번에 - List comprehension의 if문

- list comprehension을 사용하면 한 줄안에 for문과 if문을 한 번에 처리 가능

```python
mylist = [3,6,2,7]
answer = [i**2 for i in mylist if i%2 == 0]
```



#### flag OR for-else

- flag 변수 이용하여 푸는 문제들에 적용할 수 있음

```python
import math

numbers = [int(input()) for _ in range(5)]
multiplied = 1
for number in numbers:
    multiplied *= number
    if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
        print('found')
        break
else:
    print('not found')
```



#### 두 변수 값 바꾸기 - swap

```python
a = 3
b = 'abc'

a, b = b, a
```



#### 이진 탐색하기 - binary search (bisect)

- **오름차순으로 정렬된 리스트**에서 특정한 값의 위치를 찾는 알고리즘
- 검색 속도가 아주 빠름

```python
import bisect
mylist = [1,2,3,7,9,11,33]
print(bisect.bisect(mylist, 3))
```



#### 클래스 인스턴스 출력하기 - class의 자동 string casting

- \__str\_\_ 메소드를 사용해 class 내부 출력 format 지정 가능

```python
class Coord(object):
    def __init__(self, x,y):
        self.x, self.y = x, y
    
    def __str__(self):
        return '({},{})'.format(self.x, self.y)

point = Coord(1,2)
print(point)

# 출력
(3, 4)
```



#### 가장 큰 수, inf

```python
min_val = float('inf')
max_val = float('-inf')
```



#### 파일 입출력 간단하게 하기

- with -as 구문 사용

  1. 파일을 close 하지 않아도 됨. with -as 블록이 종료되면 파일이 자동으로 close
  2. readlines가 EOF까지 읽으므로, while문에서 EOF 체크할 필요 없음

  - socket이나 http 등에서도 사용할 수 있음

```python
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))
```



#### if else 문 한 줄로 쓰기

```python
# 기본 if else
if count == m:
    last = timetable_second[pos-1] - 1
else:
    last = time

# 한 줄로 쓰는 if else
last = timetable_second[pos-1] - 1 if count == m else time
```



#### 문자열 앞에 0 채우기

- string.zfill(width) 
  - 앞에 0을 채워서 스트링 길이를 width로 맞춤
- string.rjust(width[,fillchar])
  - 앞에 fillchar를 채워서 스트링 길이를 width로 맞춤

```python
"5".zfill(5)
"5".rjust(5, '0')
"%05d" % 5		# 번외

#출력 
00005
```

