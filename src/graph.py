import json
import matplotlib.pyplot as plt

# JSON ファイルからデータを読み込み
with open("src/data.json", "r") as f:
    data = json.load(f)
ages = data["ages"]
motivation = data["motivation"]

# モチベーショングラフを作成
plt.figure(figsize=(8, 4))
plt.plot(ages, motivation, marker='o', linestyle='-', color='blue', label='モチベーション')
plt.title("モチベーショングラフ")
plt.xlabel("年齢")
plt.ylabel("モチベーション（％）")
plt.legend()
plt.grid(True)

# グラフをPNG形式で保存し、表示
plt.savefig("output.png")
plt.show()

# コードベースの更新:
# 既存のサインとコサインのグラフをモチベーショングラフに変更。
