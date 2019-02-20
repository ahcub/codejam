from operator import itemgetter

t = int(input())
for ti in range(1, t+1):
    a = int(input())
    rects = a // 9
    if a % 3:
        rects += 1
    rects = min(rects, 35)
    y = 3
    missing_cells = {}
    for x in range(1, rects+1):
        x_c = 3 * x
        for xx in range(x_c-1, x_c+2):
            missing_cells[(xx, y-1)] = (x_c, y)
            missing_cells[(xx, y)] = (x_c, y)
            missing_cells[(xx, y+1)] = (x_c, y)
    prepared_cells = set()
    coordinates = None
    while coordinates != (0, 0) and coordinates != (-1, -1):
        if missing_cells:
            cell, target = missing_cells.popitem()
            print(*target)
            coordinates = tuple(map(int, input().split()))
            if coordinates != cell:
                missing_cells[cell] = target
                if coordinates in missing_cells:
                    del missing_cells[coordinates]
                    prepared_cells.add(coordinates)
            else:
                prepared_cells.add(coordinates)
        else:
            print(prepared_cells)
            break