N = int(input())

user_input = []
for _ in range(N):
    user_input.append(input())

print(' '.join(sorted(user_input, reverse=True)))