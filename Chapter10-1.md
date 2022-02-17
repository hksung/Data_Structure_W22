## Introduction to Algorithm _ Chapter 10. Elementary Data Structures

### 10-1. Stacks and Queue

- LIFO: stack
- FIFO: queue

#### Stacks

    - PUSH: insertion operation
    - POP: deletion operation, which does not take an element argument

- Figure 10.1
<img width="537" alt="image" src="https://user-images.githubusercontent.com/84297888/150425168-09fa031f-1dc6-49ce-b660-b3de6c38abaa.png">

#### Queue
    - ENQUEUE: insertion operation
    - DEQUEUE: deletion operation

- Figure 10.2
<img width="315" alt="image" src="https://user-images.githubusercontent.com/84297888/150425205-b3c5d582-a8c2-43a6-97e2-90257ac3902e.png">

- examplary code (linked list - queue, 백준 10845) [reference](https://as-j.tistory.com/96)


```python
# an exmple of linked list - queue

import sys

# 연결 리스트
class LinkedListElement:
    def __init__(self, val,  p, n):
        self.value = val
        self.prev = p
        self.next = n

# 큐
class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def push(self, x):
        if self.empty():
            elem = LinkedListElement(x, None, None)
            self.start = self.end = elem
        else:
            elem = LinkedListElement(x, self.end, None)
            self.end.next = elem
            self.end = elem
        self.count += 1
        return

    def pop(self):
        if self.empty(): return -1
        elif self.size() == 1:
            start = self.start.value
            self.start = self.end = None
        else:
            start = self.start.value
            startNext = self.start.next
            self.start = startNext
            self.start.prev = None
        self.count -= 1
        return start

    def size(self):
        return self.count

    def empty(self):
        if self.count == 0: return 1
        return 0

    def front(self):
        if self.empty(): return -1
        return self.start.value

    def back(self):
        if self.empty(): return -1
        return self.end.value

def main():
    N = int(sys.stdin.readline())
    q = Queue()
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == 'push': q.push(int(command[1]))
        elif command[0] == 'pop': print(q.pop())
        elif command[0] == 'size': print(q.size())
        elif command[0] == 'empty': print(q.empty())
        elif command[0] == 'front': print(q.front())
        elif command[0] == 'back': print(q.back())
    return

if __name__ == "__main__":
    main()
```

#### 10.1-1

Using Figure 10.1 as a model, illustrate the result of each operation in the sequence PUSH(S,4), PUSH(S, 1), PUSH(S, 3), POP(S), PUSH(S, 8), and POP(S) on an initially empty stack S stored in array S[1...6].

<details>
    <summary> Answer </summary>
    <div>
<img width="197" alt="image" src="https://user-images.githubusercontent.com/84297888/150425390-3700c742-873e-47c8-b571-070513725f1b.png">
    </div>
    </details>


#### 10.1-2

Explain how to implement two stacks in one array A[1...n] in such a way that neither stack overflows(full) unless the total number of elements in both stacks together is n. The PUSH and POP operations should run in O(1) time.

<details>
    <summary> Answer </summary>
    <div>
- The first stack starts at 1 and grows up towards n, while the second starts from n and grows down towards 1. Stack overflow happens when an element is pushed when two stack pointers are adjacent.
    </div>
    </details>

#### 10.1-3

Using Figure 10.2 as a model, illustrate the result of each operation in the sequence ENQUEUE(Q,4), ENQUEUE(Q,1), ENQUEUE(Q,3), DEQUEUE(Q), ENQUEUE(Q, 8), and DEQUEUE(Q) on an initially empty queue Q stored in array Q[1...6].

<details>
    <summary> Answer </summary>
    <div>
<img width="274" alt="image" src="https://user-images.githubusercontent.com/84297888/150425514-5bfea9e3-c030-489e-bae8-e5f4dcd750fc.png">
    </div>
    </details>

#### 10.1-4

Rewrite ENQUEUE and DEQUEUE to detect underflow and overflow of a queue.


```python
QUEUE-EMPTY(Q)
 if Q.head == Q.tail
 return true
 else return false
```


```python
QUEUE-FULL(Q)
 if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length)
 return true
 else return false
```


```python
ENQUEUE(Q, x)
 if QUEUE-FULL(Q)
 error "overflow"
 else
 Q[Q.tail] = x
 if Q.tail == Q.length
 Q.tail = 1
 else Q.tail = Q.tail + 1
```


```python
DEQUEUE(Q)
 if QUEUE-EMPTY(Q)
 error "underflow"
 else
 x = Q[Q.head]
 if Q.head == Q.length
 Q.head = 1
 else Q.head = Q.head + 1
 return x
```

#### 10.1-5

Whereas a stack allows insertion and deletion of elements at only one end, and a queue allows insertion at one end and deletion at the other end, a deque (double-ended queue) allows insertion and deletion at both ends. Write four O(1)-time procedures to insert elements into and delete elements from both ends of a deque implemented by an array.


```python
HEAD-ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
    error "overflow"
    else
    if Q.head == 1
    Q.head = Q.length
    else Q.head = Q.head -1 # move every element forward
    Q[Q.head] = x #Q.head is similar to idx
```


```python
TAIL-ENQUEUE(Q, x)
    if QUEUE-FULL(Q)
    error "overflow"
    else
    Q[Q.tail] = x
    if Q.tail == Q.length # element is only one
    Q.tail = 1
    else Q.tail = Q.tail+1 #+1 to idx
```


```python
HEAD-DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
    error "underflow"
    else
    x = Q[Q.head]
    if Q.head == Q.length
    Q.head = 1
    else  Q.head = Q.head+1
    return x
```


```python
TAIL-DEQUEUE(Q)
    if QUEUE-EMPTY(Q)
    error "underflow"
    else
    if Q.tail == 1
    Q.tail = Q.length
    else Q.tail = Q.tail-1
    x = Q[Q.tail]
    return x
```

> * Think about how to implement a queue using two stacks, and also how to implement a stack using two queues.

### 10-2. Linked lists

A linked list is a data structure in which the objects are arranged in a linear order. Unlike an array, however, in which the linear order is determined by the array indices, the order in a linked list is determined by a pointer in each object.

(Book: *Elements of Programming Interviews in Python*. (2019), Chapter 7.)

> A list implements an ordered collection of values, which may include repetitions. Specifically, a singly linked list is a data structure that contains a sequence of nodes such that each node contains an object and a reference to the next node in the list. The first node is referred to as the head and the last node is referred to as the tail; the tail's next field is null. There are many variants of the linked lists like a singly linked list, a doubly linked list, and a circular, doubly linked list with a sentinel
A list is similar to an array in that it contains objects in linear order. The key differences are that inserting and deleting elements in a list hasz time complexity O(1). On the other hand, obtaining the kth element in a list is expensive, having O(n) time complexity.

#### 10.2-5 Implement the dictionary operations INSERT, DELETE, and SEARCH using singly linked, circular lists. What are the running times of your procedures?

- INSERT: *O(1)*

```Python
LIST-INSERT(L, x)
  x.next = L.nil.next
  L.nil.next = x
```

- DELETE: *O(n)*

```Python
LIST-DELETE(L, x)
  prev = L.nil
  while pre.next !=x
  if prev.next == L.nil
  error "element not exist"
  prev = prev.next
  prev.next = x.next
```
- SEARCH: *O(n)*

```python
LIST-SEARCH(L, k)
  x = L.nil.next
  while x != L.nil and x.key !=k
  x = x.next
  return x
```

### 10-4. Representing rooted trees

<details>
    <summary> 선형구조와 비선형구조 (https://server-engineer.tistory.com/130) </summary>
    <div>
<img width="350" alt="image" src="https://user-images.githubusercontent.com/84297888/154380391-07f6d688-267f-41f0-9fee-5036e6a3764b.png">

1. 선형구조: 배열(선형 리스트), 연결 리스트, 스택, 큐, 데크 (double ended queue)
- 데이터가 연속적으로 연결되어 있는 모양으로 구성하는 방법
- 포인터 등을 사용하여 자료를 연결하면 그 결과가 자료에 일직선상에 표시되거나 하나의 원상에 표시되는 구조
        
> 연결리스트   
- 자료 항목의 순서에 따라 노드의 포인터 부분을 이용하여 서로 연결시킨 자료구조
- 노드의 삽입, 삭제 작업이 용이
- 기억 공간이 연속적으로 놓여있지 않아도 저장 가능
- 접근 속도가 느림 (포인터를 찾아가는 시간이 필요)
- 중간 노드의 연결이 끊어지면, 그 다음 노드를 찾기 힘듦
<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/154381088-a5f39fdb-74fa-41cb-9876-975a01e8ae8f.png">

> 스택
- 리스트의 한쪽 끝으로만 자료의 삽입, 삭제 작업이 이루어짐
- 인터럽트가 발생하여 복귀주소를 저장할 때 사용
<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/154381116-f379545d-0058-40bf-a1e3-1fc5ef4bbbd9.png">

> 큐
- 시작과 끝을 표시하는 두 개의 포인터가 존재
- 순서를 기다리는 대기 행렬 처리에 사용
<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/154381152-5fdfcf9a-c87c-436e-b494-8c952155878d.png">

> 데크 
- 삽입과 삭제가 리스트 양쪽 끝에서 모두 발생할 수 있는 자료구조
- 입력이 한쪽에서만 발생하고 출력은 양쪽에서 가능, 입력은 양쪽에서 일어나고 출력은 한쪽에서만 이루어지는 제한 가능
        
2. 비선형구조: 트리, 그래프
        
> 트리
- 정점(node)과 선분(branch)을 사용하여 사이클을 이루지 않도록 구성한 그래프의 형태
- 방향성 있음(부모와 자식 계층 구조가 명확)
<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/154381229-990b9889-b41f-433c-afd5-24fd69c55c8a.png">
        
> 그래프
- 정점(node)과 선분(branch)을 이용하여 사이클을 이루도록 구성
- 순환성
<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/154381297-379f8944-0353-4c2e-9888-3600fc4052c1.png">

</div>
</details>
