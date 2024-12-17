import sqlite3

# データベース接続
conn = sqlite3.connect('dreams.db')
cursor = conn.cursor()

# データの確認
cursor.execute('SELECT * FROM dreams')
for row in cursor.fetchall():
    print(row)

conn.close()
