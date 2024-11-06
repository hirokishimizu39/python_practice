# count = 0

# while count < 10:
#   print(count)
#   count += 1

age = int(input("何歳ですか？"))
casino_age = 18
game_text ="""
プレイするゲームを選択してください
1: ルーレット
2: ブラックジャック
3: ポーカー
: 
"""

if age >= casino_age:
  print("どうぞお入りください。")
  while True:
    game = int(input(game_text))
    if game == 1:
      print("あなたはルーレットを選びました")
      break
    elif game == 2:
      print("2")
      break
    elif game == 3:
      print("3")
      break
    else:
      print("1~3を選んでください。")
      continue
else:
  print("18歳未満は入れません!")