from __future__ import division
#Z tym nie działa
#A = ([-1, 2, 1],[1, -3, -2],[3, -1, -1])
#B = ([-1],[-1],[4])
#X = []

A = [[1,1,2],[2,-1,2],[4,1,4]]
B = [-1,-4,-2]
X = []

for i in range(len(A)):
    A[i].append(B[i])
    X.append(0)
size = len(A[0]) -1

for i in range(size - 1):
    if A[i][i] == 0:
        print("dzielenie przez zero")
    else:
        for j in range(i + 1, size):
            d = -A[j][i] / A[i][i]
            for k in range(i, size + 1):
                A[j][k] += d * A[i][k]

print("Po Eliminacji Współczyników: ")
print(A)

for i in range(size - 1, -1, -1):
    s = A[i][size]
    if i == (size - 1):
        X[i] = s / A[i][i]
    else:
        for j in range(size - 1, i, -1):
            s -= A[i][j] * X[j]
        if A[i][i] == 0:
            print("dzielenie przez zero")
        else:
            # print s
            X[i] = s / A[i][i]
print("Wynik ")
print(X)

