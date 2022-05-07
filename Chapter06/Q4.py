N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    b_max = max(B)
    B.remove(b_max)

    a_min_idx = A.index(min(A))
    A[a_min_idx] = b_max

    # print(f'A: {A}')
    # print(f'B: {B}')

print(sum(A))