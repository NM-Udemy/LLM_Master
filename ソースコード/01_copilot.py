import math
# 引数nが素数かどうかを判別する関数
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):  # 素数の定義から、nの平方根まで調べれば良い
        if n % i == 0:
            return False
    return True

# 1-100までの素数を表示する
for i in range(1, 101):
    if is_prime(i):
        print(i, end=' ')

# 1-100まで素数以外を表示する
for i in range(1, 101):
    if not is_prime(i):
        print(i, end=' ')