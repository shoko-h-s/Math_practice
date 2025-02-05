# 2進数を10進数に変換

# 求める数値を各桁のリストにする
n = list(input())

n_rev = n[::-1]

answer = 0

for i in range(len(n_rev)):
    d = 2 ** i * int(n_rev[i])
    answer += d
    
print(answer)
