import pandas as pd
import matplotlib.pyplot as plt

# 1. CSVファイルの読み込み
df = pd.read_csv('./input_csv_data.csv')

# 【重要】日本語の文字化けを防ぐ設定
# Windowsなら 'MS Gothic'、Macなら 'AppleGothic' や 'Hiragino Sans' などを指定してください
plt.rcParams['font.family'] = 'MS Gothic' 

# 2. 列名（ヘッダー）を自動取得
x_col = df.columns[0]
y_col = df.columns[1]

# 3. グラフの土台とサイズを設定
plt.figure(figsize=(8, 5))

# 4. データをプロット
plt.plot(df[x_col], df[y_col], linestyle='solid', marker='o', color='#1f77b4', linewidth=2)

# 5. ラベル・タイトルの設定と装飾
plt.xlabel(x_col, fontsize=12)
plt.ylabel(y_col, fontsize=12)
plt.title(f'{x_col} と {y_col} の推移グラフ', fontsize=14, pad=15)

# グラフの後ろに薄い補助線（グリッド）を敷いて見やすくする
plt.grid(True, linestyle='--', alpha=0.6)

# 6. 全体のレイアウトを整えて表示
plt.tight_layout()
plt.show()
