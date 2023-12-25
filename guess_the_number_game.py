import random

n = int(input("最小値を入力してください"))
m = int(input("最大値を入力してください"))

num = random.randint(n, m)
print("------------")
print("乱数を生成しました！")
print("------------")

count = int(input("何回以内に当てますか"))

for i in range(count):
    guess = int(input("数字を当ててください"))
    if guess == num:
        print("正解！")
        break
    print("不正解！")
    