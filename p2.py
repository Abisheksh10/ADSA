def matrix_chain_multiplication(p):
    n = len(p) - 1  
    M = [[0] * (n+1) for _ in range(n+1)]
    S = [[0] * (n+1) for _ in range(n+1)]

    for chain_length in range(2, n+1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            M[i][j] = float('inf')
            for k in range(i, j):
                cost = M[i][k] + M[k+1][j] + p[i-1] * p[k] * p[j]
                if cost < M[i][j]:
                    M[i][j] = cost
                    S[i][j] = k

    def optimization(i, j):
        if i == j:
            print(f'A{i}', end='')
        else:
            print('(', end='')
            optimization(i, S[i][j])
            optimization(S[i][j] + 1, j)
            print(')', end='')

    optimization(1, n)
    print()
    return M[1][n]

# Example usage
print("Enter the matrix dimensions in a single line:\t\tlike 10 30 5 60 20")
matrix_dimensions = list(map(int,input().split()))
min_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)
print(f'Minimum scalar multiplications: {min_scalar_multiplications}')
print("""
Initialization:

We create two matrices, M and S, each of size NxN, where N is the number of matrices in the sequence.
M[i][j] will store the minimum number of scalar multiplications needed to compute the product of matrices 
      Ai to Aj.
S[i][j] will store the value of k that minimizes M[i][j], representing the optimal split point.
Recurrence Relation:

We fill in the M matrix using a bottom-up approach, starting with subchains of length 2 and gradually 
      building up to the full chain length.

The general recurrence relation for filling in M[i][j] is:

M[i][j] = min(M[i][k] + M[k+1][j] + p[i-1] * p[k] * p[j]) for all i ≤ k < j
This formula represents the cost of parenthesizing the matrices between i and j at position k and 
      computing the cost of multiplying these parenthesized subproblems.

Reconstruction of Optimal Parenthesization:

To reconstruct the optimal way to parenthesize the matrices, we create a function that takes two indices, 
      i and j, and recursively determines the optimal split point using the S matrix.
We split the matrices at position S[i][j] and recursively call the function for the left and right 
      subchains until we reach base cases.
This process helps us build the optimal parenthesization step by step.

      
Time and Space Complexity Analysis:

Time Complexity:

Filling in the M matrix requires O(N^3) operations since there are three nested loops: one for the chain 
      length and two for the subchain indices (i and j).
Reconstructing the optimal parenthesization also takes O(N^3) time in the worst case.
Space Complexity:

We use two matrices, M and S, each of size NxN, so the space complexity is O(N^2) for storing these
       matrices.
Efficiency for Large Instances:

The dynamic programming approach is efficient for moderately large instances of the problem where N is 
      not too large.
However, it becomes impractical for very large N values due to its cubic time complexity. In such cases, 
      more advanced algorithms like Strassen's algorithm for matrix multiplication or distributed computing approaches may be used.
For most practical applications, the dynamic programming approach works well and provides the optimal 
      solution in a reasonable amount of time.
""")
