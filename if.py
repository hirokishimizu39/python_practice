
balance = 1000
withdraw = 5000000000000
limit_withdraw = 1000000
if withdraw > limit_withdraw:
  print("you can't withdraw")
elif balance > withdraw:
  balance -= withdraw
  print(balance)
else:
  print(balance)

  