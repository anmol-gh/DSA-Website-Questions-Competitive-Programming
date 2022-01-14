# Link to Contest -> https://www.codechef.com/JAN222C

# Question 01

# for _ in range(int(input())):
#     dsa, toc, dm = map(int, input().split())
#     dsa2, toc2, dm2 = map(int, input().split())
#     total_1 = dsa + toc + dm
#     total_2 = dsa2 + toc2 + dm2
#     if total_1 > total_2:
#         print("Dragon")
#     elif total_2 > total_1:
#         print("Sloth")
#     else:
#         if dsa > dsa2:
#             print("Dragon")
#         elif dsa2 > dsa:
#             print("Sloth")
#         elif toc > toc2:
#             print("Dragon")
#         elif toc2 > toc:
#             print("Sloth")
#         else:
#             print("TIE")

# Question 02

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    counter = 0
    total = 0
    for i in range(n - 1, 0, -1):
        counter += 1
        total += a[i]
        if total >= x:
            print(counter)
            break
    if total < x:
        print(-1)
