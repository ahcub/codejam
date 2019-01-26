t = int(input())

for ti in range(1, t+1):
    d, n = map(int, input().split())
    max_arrival = max([(d-k)/s for k, s in [list(map(int, input().split())) for i in range(n)]])
    print('Case #{}: {:.6f}'.format(ti, d/max_arrival))
