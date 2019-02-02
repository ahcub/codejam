t = int(input())

for ti in range(1, t+1):
    d, p = input().split()
    d = int(d)
    total_damage = 0
    s = 1
    pp = []
    for c in p:
        if c == 'S':
            pp.append(s)
            total_damage += s
        else:
            pp.append(0)
            s *= 2
    if d < p.count('S'):
        res = 'IMPOSSIBLE'
    else:
        pp = list(reversed(pp))
        p = list(reversed(p))
        res = 0
        left_most_c = 0
        while total_damage > d:
            for i, val in enumerate(p[left_most_c:-1]):
                if val == 'S' and p[i+1] == 'C':
                    res += 1
                    dam = pp[i]
                    pp[i+1], pp[i] = dam//2, 0
                    total_damage -= dam//2
                    p[i], p[i+1] = p[i+1], p[i]
                    break

    print('Case #{}: {}'.format(ti, res))
