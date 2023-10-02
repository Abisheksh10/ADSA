def disp(l,wc,ac,bc):
    print("The sorted array is:",l)
    print("Time Complexity:\n\tWorst-Case:{}\n\tAverage-Case:{}\n\tBest-Case:{}".format(wc,ac,bc))

def Bubble(n,l):
    for i in range(n):
        for j in range(0,n-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    disp(l,"O(n^2)","O(n^2)","O(n)")

def Select(n,l):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if l[j] < l[mini]:
                mini = j
        l[i], l[mini] = l[mini], l[i]
    disp(l,"O(n^2)","O(n^2)","O(n^2)")

def Insertion(n,l):
    for i in range(1,n):
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = k
    disp(l,"O(n^2)","O(n^2)","O(n)")



s = "\033[1m"
e = "\033[0;0m"    

while True:
    
    print("\nChoose any sorting algorithm to implement:")
    print("1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort")
    i=int(input())
    print("Enter the list in a single line:")
    l=list(map(int,input().split()))
    n=len(l)
    match i:
        case 1:
            Bubble(n,l)
        case 2:
            Select(n,l)
        case 3:
            Insertion(n,l)
        case 4:
            break    
        case _:
            print("!!!Enter a valid choice!!!")
print("""
Let's compare the time complexity of Bubble Sort (which we discussed earlier) with Quick Sort, 
Merge Sort, and Python's built-in `sorted` function. We'll explain the differences and scenarios 
where one algorithm might be preferred over the other.

1. Bubble Sort:

   - Worst-case Time Complexity: O(n^2)
   - Average-case Time Complexity: O(n^2)
   - Best-case Time Complexity: O(n) (with optimizations)
   - Stability: Stable

   Preferred Scenarios:
   - Bubble Sort is rarely used in practice for large datasets because of its poor worst-case and 
      average-case time complexity. It's mainly used for educational purposes and simple sorting tasks.
   - It can be useful when you have a small dataset or when data is already partially sorted.

2. Quick Sort:

   - Worst-case Time Complexity: O(n^2) (with poor pivot choice)
   - Average-case Time Complexity: O(n log n)
   - Best-case Time Complexity: O(n log n)
   - Stability: Not stable

   Preferred Scenarios:
   - Quick Sort is a highly efficient sorting algorithm and is preferred for most scenarios.
   - It's particularly useful when you have a large dataset and want good average-case performance.
   - It's not suitable for scenarios where stable sorting is required.

3. Merge Sort:

   - Worst-case Time Complexity: O(n log n)
   - Average-case Time Complexity: O(n log n)
   - Best-case Time Complexity: O(n log n)
   - Stability: Stable

   Preferred Scenarios:
   - Merge Sort is efficient and stable, making it suitable for a wide range of scenarios.
   - It's often used when you need a guaranteed worst-case time complexity of O(n log n), which Quick Sort 
      can't always provide without additional precautions.

4. Python's `sorted` Function:

   - Time Complexity: O(n log n)
   - Stability: Stable

   Preferred Scenarios:
   - Python's `sorted` function is a built-in and highly optimized sorting algorithm, typically based on 
      an adaptive variant of Timsort (a hybrid sorting algorithm).
   - It's the preferred choice for sorting in Python for general purposes, thanks to its good performance 
      and stability.

Summary and Recommendations:

- Quick Sort is generally preferred for most scenarios due to its efficient average-case performance.
    However, it's not stable.

- Merge Sort is also efficient and stable, making it a good choice when you need a stable sort or 
      guaranteed worst-case performance.

- Bubble Sort is rarely used in practice for large datasets but may be suitable for small datasets 
      or partially ordered data.

- Python's `sorted` function is the go-to choice in Python for sorting because it's both efficient 
      and stable.

In real-world applications, you should consider the size of your dataset, the expected data distribution, 
and the need for stability when choosing a sorting algorithm. For Python developers, the built-in
`sorted` function is usually the easiest and most efficient choice for general sorting tasks.""")
