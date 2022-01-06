def check(reports, index):
    if len(reports) == 1:
        return reports
    reports_zero = []
    reports_one = []
    for report in reports:
        if report[index] == "1":
            reports_one.append(report)
        else:
            reports_zero.append(report)
    print(len(reports_one), len(reports_zero))
    if len(reports_one) >= len(reports_zero):
        reports_zero = []
        check(reports_one, index + 1)
    else:
        reports_one = []
        check(reports_zero, index + 1)


def binaryToDecimal(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value


# Part two

reports_one = []
reports_zero = []

with open("Day 03.txt", "r") as f:
    total_reports = 0
    reports = f.read().splitlines()
    occurences = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    for report in reports:
        total_reports += 1
        for bit in range(0, len(report)):
            if report[bit] == "1":
                occurences[bit] += 1
                if bit == 0:
                    reports_one.append(report)
            elif report[bit] == "0" and bit == 1:
                reports_zero.append(report)

    gamma, epsilon = "", ""
    for i in occurences.values():
        if i > total_reports / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    # print(gamma, epsilon)
    # print(binaryToDecimal(int(gamma)) * binaryToDecimal(int(epsilon)))
    print(len(reports_one), len(reports_zero))
    if len(reports_one) >= len(reports_zero):
        reports_zero = []
        # print(reports_one)
        print('sss',check(reports_one, 1))
    else:
        reports_one = []
        # print(reports_zero)
        print('ssss',check(reports_zero, 1))
