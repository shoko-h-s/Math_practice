# nの階乗を求める
n = int(input("階乗を求める数を入力："))

# 格納用変数の準備
total = 1

# 1～nまでの値を、順に掛けていく
for i in range(n):
    total *= i+1

print(total)
