# フィボナッチ数列をn個目まで出力（改行区切り）
'''
最初の2数を代入しておく
3番目以降の数は、演算で求める
'''
list = [1, 1]

n = int(input())

for i in range(n):
    # 最初の2数の出力
    if (i == 0) or (i == 1):
        print(list[i])

    # 3番目以降の数の演算・出力
    else:
        num = list[-1] + list[-2]   # listの末尾の2数を合計すれば求められる
        list.append(num)   # 計算結果をlist末尾に追加する
        print(num)
