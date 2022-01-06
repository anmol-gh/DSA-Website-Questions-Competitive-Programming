# Link to Question -> https://projecteuler.net/problem=2
total = 0
first = 0
second = 1
third = 0
run = True

while run:
    if third >= 4_000_000:
        run = False
        break
    third = first + second
    first = second
    second = third
    if third % 2 == 0:
        print(total, third)
        total += third
print(total)
