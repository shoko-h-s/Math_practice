# nの約数を求める
n = int(input("約数を求める正の整数を入力："))

# リスト内包表記で記述
li = [i for i in range(1, n+1) if n % i == 0]

'''
内包表記を使わない場合

li = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
'''

print(f"約数一覧：{li}")
print(f"約数の個数：{len(li)}")
print(f"約数の合計：{sum(li)}")
