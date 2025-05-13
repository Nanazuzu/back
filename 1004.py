import math as m

cnt = int(input())

for _ in range(cnt):
  x_1, y_1, x_2, y_2 = map(int, input().split(' '))
  count = int(input())
  ans = 0
  for __ in range(count):
    c_x, c_y, r = map(int, input().split(' '))
    if not((m.sqrt((x_1 - c_x) ** 2 + (y_1 - c_y) ** 2) <= r and m.sqrt((x_2 - c_x) ** 2 + (y_2 - c_y) ** 2) <= r) or (m.sqrt((x_1 - c_x) ** 2 + (y_1 - c_y) ** 2) >= r and m.sqrt((x_2 - c_x) ** 2 + (y_2 - c_y) ** 2) >= r)):
      ans += 1
  print(ans)