### 2.1-1

Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the array A = <31, 41, 59, 26, 41, 58>.

<details>
    <summary> answer </summary>
    <div> 
The changes of array A are like the following based on the suggested model:
        
1. A = <31, 41, 59, 26, 41, 58>
        
2. A = <31, 41, 59, 26, 41, 58>
   
3. A = <31, 41, 59, 26, 41, 58>

4. A = <26, 31, 41, 59, 41, 58>
5. A = <26, 31, 41, 41, 59, 58>
6. A = <25, 31, 41, 41, 58, 59>
        </div>
        </details>

### 2.1-2

Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.


```python
def insertionSort(arr):

    for i in range (1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key

# test

arr = [12, 11, 13, 4, 3, 3, 5, 34, 35, 5, 23]
insertionSort(arr)
print ("sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])
```



### 2.1-3

Consider the searching problem:
- Input: A sequence of n numbers A = <a1, a2, ... an> and a value v.
- Output: An index i such that v = A[i] or the special value NIL if v does not appear in A.

Q. Write pseudocode for linear search, which scans through the sequence, looking for v. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties. (The following is the python code.)


```python
def linear_search(A,v):
    for i in range(1, len(A)):
        if A[i] == v:
            return i
        return "NIL" 

#test
A = [12, 11, 13, 4, 3, 3, 5, 34, 35, 5, 23]
linear_search(A, 100)        
```


- Loop invariant: At the start of each iteration of the for loop, the subarray consists of elements that are different than v.

- Initialization: Before the first loop iteration (i=1), the subarray is the empty array, so the proof is trivial.

- Maintenance: During the each loop iteration, we compare v with A[i]. If they are the same, we return i, which is the correct result. Otherwise, we continue to the next iteration of the loop. At the end of each loop iteration, we know the subarray A[1..i] does not contain v, so the loop invariant holds true. Incrementing i for the next iteration of the for loop then preserves the loop invariant.

- Termination: The loop terminates when i > A.length = n. Since i increases by 1, we must have i = n+1 at that time. Substituting n+1, for i in the wording of the loop invariant, we have that the subarray consists of elements that are different than v. Thus, we return NTL. Observing that A[1...n], we conclude that the entire array does not have any element equal to v. Hence the algorithm is correct.

### 2.1-4

Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n+1)-element array C. State the problem formally and write pseudocode for adding the two integers.

``` 
pseudocode
ADD-BINARY(A, B)
 C = new integer[A.length + 1]
 carry = 0
 for i = 1 to A.length
 C[i] = (A[i] + B[i] + carry) % 2 // remainder
 carry = (A[i] + B[i] + carry) / 2 // quotient
 C[i + 1] = carry
 return C
```

