# Link to Contest -> https://www.codechef.com/JAN221C

# Question 01

# for _ in range(int(input())):
#     t1, t2, r1, r2 = map(int, input().split())
#     print("yes") if t1 ** 2 / r1 ** 3 == t2 ** 2 / r2 ** 3 else print("no")

# Question 02

# for _ in range(int(input())):
#     n, d = map(int, input().split())
#     if d > 21:
#         answer = n
#     elif d > 10:
#         answer = (2 ** 10) * (3 ** (d - 10))
#     else:
#         answer = 2 ** d
#     print(min(answer, n))

# Question 03

for _ in range(int(input())):
    string = input()
    if "10" in string or "11" in string:
        print("Yes")
    else:
        print("No")
