# N人の選手で総当たり戦を行う場合、何回の対戦が行われるかを求める
N = int(input("選手数を入力："))

# 回数は必ず整数で求められるので、小数点以下は表示しないように設定を行う
answer = int(N * (N - 1) / 2)

print(f"総対戦回数：{answer}")
