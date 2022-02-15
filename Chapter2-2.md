## Introduction to Algorithm _ Chapter 2-2. Analyzing Algorithm

- The time taken by an algorithm grows with the size of the input, so it is traditional to describe the running time of a program as a function of the size of its input. To do so, we need to define the terms 'running time' and 'size of input' more carefully.

- Input size: *the number of items in the input* (e.g., the array size *n* for sorting)

- Running time: of an algorithm on a particular input is the number of primitive operations or 'steps' executed.

<img width="502" alt="image" src="https://user-images.githubusercontent.com/84297888/149681429-a0eb5af7-9f0c-44e1-bd9b-435bb4091d23.png">

- The running time of the algorithm is the sum of running times for each statement executed; a statement that takes ci steps to execute and executes n times will contribute ci*n* to the total running time. To compute T(n), the running time of Insertion-sort on an input of *n* values, we sum the products of the cost and times columns, obtaining

<img width="498" alt="image" src="https://user-images.githubusercontent.com/84297888/149681447-c92400f0-2cb9-48e3-9884-26b4d5608d55.png">


- We can express this running times as *an+b* for constants a and b that depend on the statement costs Ci; this is thus a linear function of n.

<img width="185" alt="image" src="https://user-images.githubusercontent.com/84297888/149681473-6576d483-f603-434a-923f-0eac93a30d59.png">
<img width="524" alt="image" src="https://user-images.githubusercontent.com/84297888/149681489-fd1dd5f4-58ff-41fb-844f-5795e6475374.png">

- We can express this worse-case running times as $$an^2+bn+c$$ for constants a, b, and c that again depend on the statement costs ci; it is thus a quadratic function of n.


### Worse-case and average-case analysis

- The worse-case running time of an algorithm gives us an upper bound on the running time for any input.
- For some algorithms, the worst case occurs fairly often.
- The 'average case' is often roughly as bad as the worst case.

### Order of growth
We use some simplifying abstractions to see our analysis of the Insertion-sort procedure.
1. We ignore the actual cost of each statement, using the constant Ci to represent these costs.
2. We observe that even these constants give us more detail than we really need: we expressed the worst-case running time as $$an^2+bn+c$$ for some constants a, b, and c that depend on the statement costs ci.
3. We thus ignored not only the actual statement costs, but also the abstract costs ci.

- The rate of growth, or order of growth, of the running time: consider only the leading term of a formula (e.g., $$an^2$$)
- theta-notation
