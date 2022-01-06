def total(number, bingo):
    sum = 0
    for i in bingo:
        for j in i:
            if type(j) == int:
                sum += j
    print(sum, number)
    print(sum * number)


# Part 01

with open("Day 04.txt", "r") as f:
    data = f.read().splitlines()
    numbers = list(map(int, data[0].split(",")))
    bingos = []
    bingo = []
    for i in data[1:]:
        if i == "":
            if len(bingo) == 5:
                bingos.append(bingo)
                bingo = []
        else:
            bingo.append(list(map(int, i.split())))
    del bingo
    for number in numbers:
        for bingo in bingos:
            for row in bingo:
                if number in row:
                    index = row.index(number)
                    row[index] = "x"
                    row_mark = 0
                    for i in range(0, 5):
                        if row[i] == "x":
                            row_mark += 1
                            if row_mark == 5:
                                total(number, bingo)
                                break
                    column_mark = 0
                    for i in range(0, 5):
                        if bingo[0][index] == "x":
                            column_mark += 1
                            if column_mark == 5:
                                total(number, bingo)
                                break
