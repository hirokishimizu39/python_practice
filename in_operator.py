fruits = ['apple', 'peach', 'grapes', 'banana']
print('lemon' not in fruits)
print('h' in 'hello')

your_fovorite_fruites = input("好きなグルーつはなんですか")

if your_fovorite_fruites in fruits:
  fruits.remove(your_fovorite_fruites)
  print("{}ですね、差し上げますよ".format(your_fovorite_fruites))
else:
  fruits.append(your_fovorite_fruites)
  print(fruits)