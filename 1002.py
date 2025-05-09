import math as m

cnt = int(input())
for index in range(cnt):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split(' '))
    dist = m.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    if dist == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
    else:
        if float(r_1) + float(r_2) == dist or float(abs(r_1 - r_2)) == dist:
            print(1)
        elif abs(r_1 - r_2) < dist and dist < r_1 + r_2:
            print(2)
        else:
            print(0)