import sqlite3
import xlwings as xw
from save_to_excel import save_to_excel  # save_to_excel.pyの関数をインポート

def search_dream(keyword):
    conn = sqlite3.connect('dreams.db')
    cursor = conn.cursor()

    # 入力されたキーワードをスペースで分割
    keywords = keyword.split()
    results = []

    # 各キーワードについて部分一致検索を実行
    for kw in keywords:
        cursor.execute('SELECT category, interpretation FROM dreams WHERE keyword LIKE ?', (f'%{kw}%',))
        result = cursor.fetchall()
        results.extend(result)

    conn.close()
    return results

# テスト
keyword = input("夢で見たキーワードを入力してください: ")
results = search_dream(keyword)

if results:
    for result in results:
        print(f"カテゴリ: {result[0]}, 占い結果: {result[1]}")
        # 検索結果をExcelファイルに保存
        save_to_excel(keyword, result)
else:
    print("該当するキーワードが見つかりません。")
