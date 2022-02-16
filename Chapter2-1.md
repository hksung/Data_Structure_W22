## Introduction to Algorithm _ Chapter 2-1. Insertion Sort

### Insertion Sort


```python
def insertionSort(arr):

    for i in range (1, len(arr)):

        key = arr[i]

        '''
        move elements of arr[0...i-], that are
        greater than key, to one position ahead
        of their current position
        '''

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key

# test

arr = [12, 11, 13, 4, 3, 3, 5, 34, 35,5,23]
insertionSort(arr)
print ("sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])
```

### Loop Invariant (Book: *Algorithms Unlocked*. (2013), pp.21-22)
- One common method of showing correctness uses a **loop invariant**: an assertion that we demonstrate to be true each time we start a loop iteration. For a loop invariant to help us argue correctness, we have to show three things about it.

1. Initialization: It is true before the first iteration of the loop.
2. Maintenance: If it is true before an iteration of the loop, it remains true before the next iteration.
3. Termination: The loop terminates, and when it does, the loop invariant, along with the reason that the loop terminated, gives us a useful property.

  Example: At the start of each iteration of step 1, if x is present in the array A, then it is present in the subarray (a contiguous portion of an array) from A[i] through A[n].

- Loop Invariant in the above example:
    - Iteration: Initially, i = 1 so that the subarray in the loop invariant is A[1] through A[n], which is the entire array.
    - Maintenance: Assume that at the start of an iteration for a value of i, if x is present in the array A, then it is present in the subarray from A[i] through A[n]. If we get through this iteration without returning, we know that A[i] is not x, and therfore we can say that if x is present in the array A, then it is present in the subarray from A[i+1] through A[n]. Because i is incremented before the next iteration, the loop invariant will hold before the next iteration.
    - Termination: This loop must terminate, either because the procedure returns in step 1A or i>n. We have already handled the case where the loop terminates because the procedure returns in step 1A.
    To hanle the case where the loop terminates because i>n, we rely on the contrapositive of the loop invariant. The contrapositive of the statement "if A then B" is "if not B then A." The contrapositive of a statement is true if and only if the statement is true. The contrapositive of the loop invariant is "if x is not present in the subarray from A[i] through A[n], then it is not present in the array A."

### Objects (https://wikidocs.net/20456)
<details>
<summary> 정리 </summary>
<div markdown='1'>
- Definition: any data with state (attributes or value) and defined behavior (methods).

- 객체는 어떤 속성값과 행동을 가지고 있는 데이터.
- 파이썬은 객체지향프로그래밍. 파이썬에서 모든 것은 객체이며, 객체는 각각 타입이 존재함. 객체는 타입별로 동일한 속성과 행동을 가짐.
- 객체는 클래스를 통해서 생성. 클래스는 클래스를 통해 생성할 객체들의 속성과 행동(매소드)을 정의하는 공간이며, 객체끼리 서로 같은 타입을 가진다면, 같은 속성과 행동(매소드)를 가짐.
- related functions: type, dir, help

<div>
	</details>
