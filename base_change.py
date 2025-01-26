# 10進数から M 進数に変換（～9進数）

n = int(input("変換する値を入力："))
m = int(input("変換する進数を入力："))

# 変換後の各桁を収納するリスト（反転して入力される）
li = []

while n != 0:
    li.append(str(n % m))
    n //= m

# リストを反転
li_rev = li[::-1]

# 各桁を結合、文字列として表示
print("".join(li_rev))
