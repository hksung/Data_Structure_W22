## Introduction to Algorithm _ Priority Queues with Binary Heaps
### (*Problem Solving with Algorithms and Data Structures using Python*, pp.256-266)


Priority queue acts like a queue that you dequeue an item by removing it from the front. However, in a priority queue the logical order of items inside a queue is determined by their priority. The highest priority items are at the front of the queue and the lowest priority items are at the back. Thus when you enqueue an item on a priority queue, the new item may move all the way to the front.

- The classic way to implement a priority queue is using a data structure called a binary heap.
- A binary heap will allow us both enqueue and dequeue items in O(logn).
- When we diagram the heap, it looks like a tree, but when we implement it, we use only a single list as an internal representation.

    - min heap: the smallest key is always at the front
    - max heap: the largest key is always at the front

[참고 및 그림 출처](https://velog.io/@holicme7/우선순위-큐Prioirity-Queue-mbk48cz764)

- 배열이나 연결리스트로 구현할 경우 간단히 구현이 가능하지만, 데이터 삽입과 삭제 과정에서 데이터를 한 칸씩 당기거나 밀어야 하는 연산을 계속 해야 함.
- 삽입의 위치를 찾기 위해 배열에 저장된 모든 데이터와 우선순위를 비교해야 함.
- 연결리스트의 경우, 삽입의 위치를 찾기 위해 첫 번째 노드부터 시작해 마지막 노드에 저장된 데이터와 우선순위 비교를 진행할 수도 있음 (성능 저하)
- 일반적으로 힙을 이용

<img width="773" alt="image" src="https://user-images.githubusercontent.com/84297888/151912228-28c4ed7a-c27d-43c2-a393-25d6c02d9a90.png">

#### 최대힙
- 부모 노드가 자식 노드보다 값이 큰 완전 이진트리
- 최대힙의 root node는 항상 최대값
- 전체 트리가 최대 힙 구조를 유지하도록 함

<img width="800" alt="image" src="https://user-images.githubusercontent.com/84297888/151912313-522eb2c4-1b90-415d-b822-90f5bdb73395.png">
<img width="800" alt="image" src="https://user-images.githubusercontent.com/84297888/151912358-b6f8e174-54b4-4c63-9d23-114aa490eb04.png">
<img width="800" alt="image" src="https://user-images.githubusercontent.com/84297888/151912555-8cc86ab8-e1b3-42ed-80a1-49bb2e47b0cd.png">
