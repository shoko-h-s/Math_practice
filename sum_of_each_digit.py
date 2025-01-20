# ある整数の各桁の和を求める
n = input("求める整数を入力：")

# 入力した整数を1桁ずつリスト化する
list_n = list(n[:])

# リストの要素を全てint型に直す
list_n = [int(i) for i in list_n]

print(f"各桁の和は、{sum(list_n)}")
