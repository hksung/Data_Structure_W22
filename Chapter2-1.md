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

### Loop Invariant
- the properties of A[1...j-1] formally as a loop variant. At the start of each iteration of the for loop of lines 1-8, the subarray A[1...j-1] consists of the elements originally in A[1...j-1], but in sorted order
- use loop invariants to help us understand why an algorithm is correct

1. initialization (i=1)
- if i=1, j=0
- arr[0] = the original element
- the original element is arranged
	(4) therefore, before the loop iteration, the loop variant is true.

2. maintenance (while repetition of the works)
- the body of the for loop works by moving A[j-1], A[j-2], A[j-3] and so on by one position to right until it finds the proper position for A[j], at which point it inserts the value of A[j].
- incrementing j for the next iteration of the for loop then preserves the loop invariant

3. termination
- the condition causing for the for loop to terminate is that j>A.length = n

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
