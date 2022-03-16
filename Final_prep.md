#Possible topics in Final (03/16/22)

##Visuatlization: 
https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

0. Binary tree-
In a binary tree, a node can have maximum two children.

1. Binary search tree (BST)

- Definition: It is a special type of binary tree in which left child of a node has value less
than the partent and right child has value greater than parent.

- Complexity of operations 
  - [Quiz] worst case: The worst-case time for **deleting** an item from a BST of size n - O(n)
  (if I do not make any additional assumptions about the tree, other than its ordering property)
  
  - searching: worst case O(n), in general, O(h) where **h** is the height of BST
  - insertion: worst case O(n), in general, O(h)
  - deletion: worst case O(n), in general, O(h)
  
  
2. AVL / Height balanced tree-

- Definition: It is a BST with additional property that difference between hieght of left sub-tree
and right sub-tree of any node can't be more than 1.

3. B-tree

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