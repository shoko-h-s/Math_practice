# 10進数から m 進数に変換（～9進数）

n = int(input("変換する値を入力："))
m = int(input("変換する進数を入力："))

# 変換後の各桁を収納するリスト（反転して入力される）
mod_list = []

while n != 0:
    # 文字列型として各桁を出力
    digit = str(n % m)
    
    mod_list.append(digit)
    n //= m

# リストを反転
answer_list = mod_list[::-1]    

print("".join(answer_list))
