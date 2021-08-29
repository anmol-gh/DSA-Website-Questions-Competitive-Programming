a = set(map(int, input().split()))
answer = True
for _ in range(int(input())):
    b = set(map(int, input().split()))
    if a.intersection(b) != b:
        answer = False
        break
print(answer)
