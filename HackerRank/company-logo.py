s = input()
dictionary = {}
answer = [
    [
        'a', 3
    ],
    [
        'b', 2
    ],
    [
        'c', 1
    ]
]
for i in s:
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)
