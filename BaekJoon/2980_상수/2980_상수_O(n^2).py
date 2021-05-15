A, B = input().split()
A, B = A[::-1], B[::-1]


for i in range(3):
    if A[i] > B[i]:
        print(A)
        break
    if A[i] < B[i]:
        print(B)
        break

