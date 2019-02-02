t = int(input())

for ti in range(1, t+1):
    n = input()
    p = list(map(int, input().split()))
    c = [chr(65+i) for i in range(len(p))]
    exit_order = []
    senates = True
    while senates:
        senates = False
        for i, n in enumerate(p):
            if n > 0:
                senates = True
                p[i] -= 1
                exit_order.append(c[i])
    result = []
    last_el = len(exit_order)
    if len(exit_order) % 2:
        last_el -= 1
        result.append(exit_order[last_el])
    for i in range(last_el, 0, -2):
        result.append(''.join(exit_order[i-2:i]))
    print('Case #{}: {}'.format(ti, ' '.join(result)))
