# Possible topics in Final (03/16/22)

* [Visuatlization](https://dichchankinh.com/~galles/visualization/Algorithms.html)

### Binary tree: In a binary tree, a node can have maximum two children.

### Binary search tree (BST)
- Definition: It is a special type of binary tree in which left child of a node has value less
than the partent and right child has value greater than parent.
- The properties of a BST are recursive: if we consider any nodes as a "root", these properties will remain true.

- Complexity of operations 
  - [Quiz] worst case: The worst-case time for **deleting** an item from a BST of size n - O(n)
  (if I do not make any additional assumptions about the tree, other than its ordering property)
  
  - searching: worst case O(n), in general, O(h) where **h** is the height of BST
  - insertion: worst case O(n), in general, O(h)
  - deletion: worst case O(n), in general, O(h)

### traversal
- Due to the way nodes in a BST are ordered, an _in-order traversal_ (left node, than root node, then right note) will always produce a sequence of values in increasing numerical order.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/84297888/158663534-e26726f0-16db-4f3a-9c9f-e67616b3b0ba.png">

* 보충 설명 + 그림 [출처](https://m.blog.naver.com/4717010/60209908735)
- 연결리스트로 구현된 트리는 루트노드의 포인터만 갖고 있으면, 트리의 모든 노드에 접근이 가능하다.
- 어떤 목적을 가지고 트리의 모든 노드에 방문하는 것을 트리 순회(traversal)이라고 한다.
- 트리의 계층적인 구조로 인해 순회 방법은 다양하다 (선형 구조는 하나)
<img width="400" alt="image" src="https://user-images.githubusercontent.com/84297888/158664028-64fcdafb-1ffa-47e1-8867-19462be1a931.png">

- 예시
<img width="400" alt="image" src="https://user-images.githubusercontent.com/84297888/158664378-61b0607d-5790-4048-ba1d-366204a3ef72.png">

1. pre-order: A-B-D-H-I-E-C-F-G
2. in-order: H-D-I-B-E-A-F-C-G
3. post-order: H-I-D-E-B-F-G-C-A

<img width="300" alt="image" src="https://user-images.githubusercontent.com/84297888/158664753-8ba76fd6-b875-4443-9825-abc26f7b16da.png">

### AVL / Height balanced tree

- Definition: It is a BST with additional property that difference between hieght of left sub-tree
and right sub-tree of any node can't be more than 1.

### B-tree

- Definition: It is a self-balancing search tree. In most of the other self-balancing search trees (like AVL and RBT),
it is assumed that everything is in main memory. 
- Think of B-tree as a generalitztion of a BST. Similar to a BST, the stored data is sorted in a B-tree,
but unlike a BST, a B-tree can have more than two child nodes.
- In addition to having multiple children, each node in a B-tree can have more than one key,
which keeps the height of the tree relatively small.

- Complexity of operations (when n is the number of keys stored in the tree)
  
  - searching: O(log n)
  - insertion: O(log n)
  - deletion: O(log n)

### Red-black tree (RBT)

- Definition: A RBT is a type of self-balancing BST. It is complex, but has a good worst-case running time for its operations and is efficient in practice: it can search, insert, and delete in O(log n) time, where n is the total number of elements in the tree.

- Properties
  - In RBT, the leaft nodes are not relevant and do not contain data. A null child pointer can encode the fact that this child is a leaf.
  - Like BSTs, RBT allow efficient in-order traversals of elements.
  - The search time on a RBT results in O(log n) time.

* 보충 설명 + [참고](https://jwdeveloper.tistory.com/280)

- Condition
  - 각 노드는 red / black
  - 루트 노드(최상단 노드)는 black
  - 모든 리프 노드(최하단 노드)는 black 
  - red 노드의 하식들은 모두 black (red-red 연속 불가)
  - 모든 노드에 대해서 그 노드의 자손인 리프 노드에 이르는 모든 경로에는 동일한 개수의 black 노드 존재
  - red-red가 연속되면 --> 좌우로 회전
<img width="200" alt="image" src="https://user-images.githubusercontent.com/84297888/158667139-44375a7a-d327-4603-bee3-0bb298d7afe6.png">
<img width="675" alt="image" src="https://user-images.githubusercontent.com/84297888/158667216-a53d0b72-3ac1-4ec4-bf0c-3c8e60b00190.png">
<img width="251" alt="image" src="https://user-images.githubusercontent.com/84297888/158667254-5b2f35dd-9131-4c90-93d6-897af818b28a.png">

- 회전 기준
  - 삼촌이 레드일 때: 부모와 삼촌의 색깔을 blakc으로 바꾸고 할아버지 색깔을 바꿈
  - 삽입템이 부모의 오른쪽 자식인 경우: 부모를 기준으로 좌회전
  - 삽입템이 부모의 왼쪽 자식인 경우: 부모를 기준으로 우회전\
  - 시뮬레이션 참고
