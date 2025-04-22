# graph-py

Vibe Coding製

このプロジェクトは、JSONファイルからデータを読み込み、Matplotlibを用いてモチベーショングラフを描画するシンプルなPythonスクリプトです。

## インストール

1. Python 3.x をインストールしてください。
2. プロジェクトディレクトリに移動してください。
3. 以下のコマンドを実行して必要なパッケージをインストールします:

   ```
   pip3 install -r requirements.txt --break-system-packages
   ```

## 実行方法

以下のコマンドを実行すると、`src/data.json`に定義されたデータからグラフが描画され、`output.png`として保存されます。

```
python3 src/graph.py
```

## ファイル構成

- `src/graph.py`: グラフを描画するメインスクリプト
- `src/data.json`: グラフのデータ (年齢とモチベーション)
- `requirements.txt`: プロジェクトの依存関係
- `README.md`: このファイル
