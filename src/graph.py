import json
import matplotlib.pyplot as plt
import numpy as np

def age_transform(x):
    """年齢を非線形にスケーリング（18歳未満を圧縮）"""
    return np.where(x < 18,
                   x * 0.25,  # 18歳未満は圧縮（0.25倍）
                   4.5 + (x - 18) * 1.3)  # 18歳以降は拡大（1.3倍）

def age_inverse(x):
    """逆変換関数"""
    return np.where(x < 4.5,
                   x / 0.25,  # 18歳未満の逆変換
                   18 + (x - 4.5) / 1.3)  # 18歳以降の逆変換

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
plt.figure(figsize=(12, 6))

# カスタムスケールでプロット
plt.plot([age_transform(x) for x in ages], motivation, 
         marker='o', linestyle='-', color='blue', label='Motivation')
plt.axhline(50, color='red', linestyle='--', label='50%')

# y軸を0-100%に設定
plt.ylim(0, 100)

# グラフの見た目を調整
plt.title("Motivation Graph (Custom Age Scale)", fontsize=12)
plt.xlabel("Age (Compressed below 18)", fontsize=10)
plt.ylabel("Motivation (%)", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# X軸の目盛りを調整（実際の年齢を表示）
major_ticks = [0, 5, 10, 15, 18, 20, 25]
plt.xticks([age_transform(x) for x in major_ticks], major_ticks)

# 18歳の位置に縦線を引く（スケール変更点の明示）
plt.axvline(age_transform(18), color='gray', linestyle=':', alpha=0.5)

plt.legend(loc='upper right')

# グラフをPNG形式で保存し、表示
plt.savefig("output.png")
