import json
import matplotlib.pyplot as plt

# JSON ファイルからデータを読み込み
with open("src/data.json", "r") as f:
    data = json.load(f)

ages = []
motivation = []
for entry in data.values():
    age_fraction = entry["age"] + entry.get("month", 0) / 12
    ages.append(age_fraction)
    motivation.append(entry["motivation"])

# モチベーショングラフを作成
plt.figure(figsize=(8, 4))
plt.plot(ages, motivation, marker='o', linestyle='-', color='blue', label='Motivation')
plt.axhline(50, color='red', linestyle='--', label='50%')
# y軸を50%を中心に設定
y_min = min(motivation)
y_max = max(motivation)
max_dev = max(abs(50 - y_min), abs(y_max - 50))
plt.ylim(50 - max_dev, 50 + max_dev)
plt.title("Motivation Graph (Fractional Age)")
plt.xlabel("Age")
plt.ylabel("Motivation (%)")
plt.legend()
plt.grid(True)

# グラフをPNG形式で保存し、表示
plt.savefig("output.png")
