# is演算子：同じオブジェクトかどうか判定する

a = 1
b = 1
c = 3

print(id(a))
print(id(1))
print(id(b))


print(a is b)
print(a is not c)
