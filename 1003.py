cnt = int(input())

dp = [(1,0), (0,1)]
for index in range(2,41):
  z = dp[index-1][0] + dp[index-2][0]
  o = dp[index-1][1] + dp[index-2][1]
  dp.append((z,o))
for _ in range(cnt):
  inputed = int(input())
  print(f"{dp[inputed][0]} {dp[inputed][1]}")

#It's too heavy, O(2^n)
# for index in range(cnt):
#   endpoint = int(input())
#   mid = [endpoint]
#   res = []
#   while(len(mid) != 0):
#     for index in range(len(mid)):
#       ind = mid.pop(0)
#       if ind == 1 or ind == 0:
#         res.append(ind)
#         continue
#       else:
#         mid.append(ind - 1)
#         mid.append(ind - 2)
#   ret = [0,0]
#   for index in res:
#     if index == 0:
#       ret[0] += 1
#     else:
#       ret[1] += 1
#   ret_str = str(ret[0]) + " " + str(ret[1])
#   print(ret_str)