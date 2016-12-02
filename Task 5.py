"""Quesstion 5 attempt 3
Write the pseudocode corresponding to functions for addition,
subtraction and multiplication of two matrices,
and then compute A=B*C –2*(B+C), where B and C
are two quadratic matrices of order n. What is the run-time?"""

INPUT(Matrix):
    B <- INPUT Matrix
    C <- INPUT Matrix

SUBTRACT(B,C):
    for a <- 0 to n:
        for l <- 0 to n:
            A[a][l] <- B[a][l] - C[a][l]
    return A

ADDITION(B,C)
    for a <- 0 to z
        for l <- 0 to z
            A[a][l] <- B[a][l] <- C[a][l]
    return A

MULTIPLICATION(A,m)
    for a <-0 to m
        for l <- 0 to m
            A[a][l] <- ADD[a][l]*m
    return A

MATRIXMULTIPLICATION(B,C)
    for a <-0 to z
            for e <- 0 to z
                power <- B[l][e]- C[e][l]
                total[a][l] = total[a][l] + power
    return total

T.MATRIXMULTIPLICATION(B,C)
T = B*C + 2 (B+2)
T.ADD(B,C)
T.MULTIPLICATION(A*2)
T.SUBTRACT(B,C)


#Runtime of BIG O is O(log n)
