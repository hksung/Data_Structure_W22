### 2.2-1

Express the function n^3/1000-100n^2-100n+3 in terms of theta-notation.

     
     [A] The highest order of n term of the function ignoring the constant coefficient is n^3. 
        So the funciton in theta-notation will be n^3.

### 2.2-2

Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element in A[1]. Then find the second smallest element of A, and exchange it with A[2]. Continue in this manner for the first n-1 elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first n-1 elements, rather than for all n elements? Give the best-case and worst-case running times of selection sort in theta-notation.


```python
# pseudocode

for i in 1 to A.length-1
    minIndex = i
    for j = i+1 to A.length
        if A[j] <A[minIndex] and j != minIndex
            minIndex = j
    swap A[i] with A[minIndex]
```


```python
# selection sort

def selectionsort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range (i+1, len(A)):
            if A[j] < A[minIndex] and j != minIndex:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]
    return (A)
# test
import random
num_failed = 0
total_tests = 100

for i in range(total_tests):
    length = random.randint(2, 50)
    lst = [random.randint(0, 100) for _ in range(length)]
    selectionsort(lst)
    
    for i in range(len(lst) -1):
        if lst[i] > lst[i+1]:
            num_failed += 1
            print(f"Test # {i<2}: List is not sorted")
            break
    if num_failed >0:
        break

if num_failed >0:
    print(f"\nFailed")
else:
    print(f"Passed {total_tests}/{total_tests} tests")

#test_return
A = [1, 3, 3, 5, 5, 3, 455, 25, 73, 55, 233]
selectionsort(A)
```

#### Loop invariant
    At the start of each iteration of the outer for loop, the subarray A[1...i-1] consists of i-1 
    smallest elements of A, sorted in increasing order.

#### Why only first N-1 elements
    The algorithm needs to run for only the first n-1 elements, rather than for all n elements 
    because the last iteration will compare A[n] with the minimum element in A[1...n-1] and swap them 
    if necessary. So, there is no need to continue the algorithm for all the way to the last element.

#### Running times
    The algorithm will take one element at a time and compare it will all the other elements. 
    In other words, each of the *n* elements will be compared with the rest of *n-1* elements. 
    So, the running times will be n^2 (theta-notation).

<details>
<summary> detail proof </summary>
<div markdown = '1'>

<img width="858" alt="image" src="https://user-images.githubusercontent.com/84297888/149683760-b7e3da98-ae3e-4de3-a0aa-f887c98e939a.png">
<div>
        </details>
    
#### 참고
- [선택 정렬](https://hyen4110.tistory.com/53)
- [삽입 정렬](https://hyen4110.tistory.com/54?category=951732)

### 2.2-3

Consider linear search again (see Exercise 2.1-3). How many elements of the in- put sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in theta-notation? Justify your answers.

    [A] On average, half the elements in array A will be checked before v is found in it. And in the worst case 
    (v is not present in A), all the elements need to be checked. In either case, the running time will be 
    proportional to n(theta-notation).

### 2.2-4

How can we modify almost any algorithm to have a good best-case running time?


    [A] We can design any algorithm to treat its best-case scenario as a special case and return a predetermined
    solution. For example, for selection sort, we can check whether the input array is already sorted and if it
    is, we can return without doing anything. We can check whether an array is sorted in linear time. 
    So, selection sort can run with a best-case running time of n(theta-notation).
        
