# Levenshtein Distance (Edit Distance): the minimum number of single-character edits 
# (insertions, deletions or substitutions) required to change one word into the other.

A = input()
B = input()

def editDistance(A, B):
    n = len(A)
    m = len(B)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j],
                                   dp[i - 1][j - 1])
    return dp[n][m]


print(editDistance(A, B))
