### Binary Search, Selection Sort, Insertion Sort, Merge Sort, and Quicksort 
(Book: *Algorithms Unlocked*. (2013), pp.28-59)

1. Binary Search (BS)
- BS has the advantage that it takes only O(lg n) times to search an n-element array.

>"Here's how you could apply binary search to finding a boook by Jonanthan Swift.
Go to the slot exactly halfway over on the shelf, find the book there,
and examine the author's name. Let's way that you've found a book by Jack
London. Not only is that not the book you're searching for, but because you
know that the books are sorted alphabetically by author, you know that all
books to the left of the book by London can't be what you're searching for.
By looking at just one book, you hve eliminated half of the books on the shelf
from consideration! (p.28)"


- In a computer, we perform binary search on an array. At any point, we are considering only a subarray, that is, the portion of the array between and including two indices; let's call them p and r. Initially, p =1 and r = n.
- We repeatedly halve the size of the subarray that we are considering until one of two things happen: we either find the value that we're searching for or the subarray is empty (that is, p becomes greater than r). The repeated halving of the subarray size is what gives rise to the O(lg n) running time.
- In the worst case: &theta;(lg n), In the best case: &theta;(1)
