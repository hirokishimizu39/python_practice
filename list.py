

fruits = ['apple', 'orange', 'melon', 'peach']

hetro_list = ['string', 1, 48, True, fruits]

print(hetro_list)
print(hetro_list[4][2])
print(hetro_list[4][-4])
print("hello world"[4])

fruits.append('banana')
print(fruits)

fruits.insert(0, 'grapes')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits_len = len(fruits)
print(fruits_len)
print(len("hello world"))