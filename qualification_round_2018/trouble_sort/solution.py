t = int(input())
for ti in range(1, t+1):
    n = input()
    v = list(map(int, input().split()))
    v1 = sorted(v[0::2])
    v2 = sorted(v[1::2])
    v[0::2] = v1
    v[1::2] = v2
    fail_index = 'OK'
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            fail_index = i
            break
    print('Case #{}: {}'.format(ti, fail_index))
