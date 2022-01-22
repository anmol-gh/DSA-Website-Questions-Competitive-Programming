nums = []
run = True

while run:
    number = input("Enter a number")
    if number == "done":
        break
    try:
        number = int(number)
        nums.append(number)
    except:
        print("Invalid input")

largest = -999999999999999999999999
smallest = 999999999999999999999999

for i in range(0, len(nums)):
    largest = max(nums[i], largest)
    smallest = min(nums[i], smallest)
print(largest, smallest)
