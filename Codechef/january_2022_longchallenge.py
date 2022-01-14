# Link to Contest -> https://www.codechef.com/JAN221C

# Question 01

# for _ in range(int(input())):
#     t1, t2, r1, r2 = map(int, input().split())
#     print("yes") if t1 ** 2 / r1 ** 3 == t2 ** 2 / r2 ** 3 else print("no")

# Question 02

for _ in range(int(input())):
    n, d = map(int, input().split())
    if d > 21:
        answer = n
    elif d > 10:
        answer = (2 ** 10) * (3 ** (d - 10))
    else:
        answer = 2 ** d
    print(min(answer, n))

for _ in range(int(input())):
    string = input()
    is_prime = False
    s = ""
    l = []
    for i in range(len(string)):
        s = ""
        s += string[i]
        l.append(s)
        for j in range(i + 1, len(string)):
            s += string[j]
            l.append(s)
    print(l)


def check_prime(number: int) -> bool:
    pass
