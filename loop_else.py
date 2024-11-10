fruites = ['apple', 'peach', 'grapes', 'banana']

# for fruit in fruites:
#   choice = input(f"あなたが探しているフルーツは{fruit}ですか？ y/n: ")
#   if choice == "y":
#     print("見つかってよかったですね！")
#     break
#   else:
#     print("そうですか。。")
# else:
#   print("お探しのフルーツは見つかりませんでした。")


balance = 1000
game_price = 200

while balance >= game_price:
  choice = input(f"一回{game_price}円のゲームに参加しますか？（残高:{balance}円(y/n?):")
  if choice == "y":
    balance -= game_price
    print(balance)
  elif choice == "n":
    print("また遊びましょう")
    break
  else:
    print("yかnでお答えください")