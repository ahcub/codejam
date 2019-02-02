t = int(input())

for ti in range(1, t+1):
    n, k = map(int, input().split())
    prev_n = n
    remaining_n = 0
    other_n = n
    while k > 0:
        prev_n = n
        remaining_n = n % 2
        remaining_k = k % 2 if k != 1 else 0
        n = (n // 2)
        other_n = prev_n - n - 1
        k //= 2
        if remaining_k != 0:
            n = other_n
    remaining = (prev_n // 2)
    res = remaining, remaining - 1 + remaining_n if remaining > 0 else 0
    print('Case #{}: {} {}'.format(ti, remaining, remaining - 1 + remaining_n if remaining > 0 else 0))
