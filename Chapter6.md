## Introduction to Algorithm _ Chapter 6. Heap

### 6-1. Heaps

- The binary heap data structure is an array object that we can view as a nearly complete binary tree. Each node of the tree corresponds to an element of the array. The tree is completely filled on all levels except possibly the lowest, which is filled from the left up to a point.
- Characteristics
	- most common implementation
	- operations are O(log n)
	- uses a binary tree structure
	- except that the tree is stored in an array without pointers
	- an implicit tree, children and parents inferred from the location in array
	- a binary heap with n elements has the height of log n (floor), why? ("we define the height of a node in a heap to be the number of edges on the longest simple downward path from the node to a leaf, and we defind the height of the heap to be the height of its root"
- Two kinds of binary heaps
	- max-heaps: A[PARENT(i)]>=A[i] (the largest element in a max-heap is stored at the root, and the subtree rooted at a node contains a value no larger than that contained at the node itself)
	- min-heaps: A[PARENT(i)]<=A[i] (the smallest element is at the root)
- Basic running times
	- The MAX-HEAPIFY, which runs in O(lg n) time, is the key to maintaining the max-heap property.
	- The BUILD-MAX-HEAP, which runs in linear time, produces a max-heap from an unordered input array.
	- The HEAPSORT procedure, which runs in O(nlgn) time, sorts an array in place.
	- The MAX-HEAP-INSERT, HEAP-EXTRACT-MAX, HEAP-INCREASE-KEY, and HEAP-MAXIMUM procedures, which run in O(lg n) time, allow the heap data structure to implement a priority queue.