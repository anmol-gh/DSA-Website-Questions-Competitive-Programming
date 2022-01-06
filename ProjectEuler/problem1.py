# Link to Problem -> https://projecteuler.net/problem=1
total = 0
for i in range(0, 1000):
    if i % 3 == 0 and i % 5 == 0:
        total += i
    elif i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)
