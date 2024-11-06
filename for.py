fruits = ['apple', 'peach', 'grapes', 'banana']
favorite_fruits = []
normal_fruits = []


for fruit in fruits:
  choice = input(f"{fruit}は好きですか? y/n" )
  if choice == 'y':
    favorite_fruits.append(fruit)
  else:
    normal_fruits.append(fruit)

print(f"favorite fruits: {favorite_fruits}")
print(f"normal_fruits: {normal_fruits}")