N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# self

# for _ in range(K):
#     b_max = max(B)
#     B.remove(b_max)
#
#     a_min_idx = A.index(min(A))
#     A[a_min_idx] = b_max
#
#     # print(f'A: {A}')
#     # print(f'B: {B}')
#
# print(sum(A))

# Answer
A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

    else:
        break

print(sum(A))