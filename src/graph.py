import json
import matplotlib.pyplot as plt

# JSON ファイルからデータを読み込み
with open("src/data.json", "r") as f:
    data = json.load(f)

ages = []
motivation = []
for entry in data.values():
    ages.append(entry["age"])
    motivation.append(entry["motivation"])

# モチベーショングラフを作成
plt.figure(figsize=(8, 4))
plt.plot(ages, motivation, marker='o', linestyle='-', color='blue', label='Motivation')
plt.title("Motivation Graph")
plt.xlabel("Age")
plt.ylabel("Motivation (%)")
plt.legend()
plt.grid(True)

# グラフをPNG形式で保存し、表示
plt.savefig("output.png")
