import sqlite3

# データベース接続
conn = sqlite3.connect('dreams.db')
cursor = conn.cursor()

# テーブル作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS dreams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL,
    category TEXT NOT NULL,
    interpretation TEXT NOT NULL
)
''')

# 新しい初期データを追加
cursor.executemany('''
INSERT INTO dreams (keyword, category, interpretation)
VALUES (?, ?, ?)
''', [
    ('海', '自然', '感情の解放を示します'),
    ('蛇', '動物', '変化や再生を象徴します'),
    ('家', '場所', 'あなたの心の状態を表します'),
    ('星', '天体', '希望や未来の兆しを意味します'),
    ('森', '自然', '探求心や成長を示唆します'),
    ('火', '自然', '情熱やエネルギーを示します'),
    ('月', '天体', '内面的な変化や感情を象徴します'),
    ('水', '自然', '感情や流れ、生命の源を表します'),
    ('鳥', '動物', '自由や新たな可能性を意味します'),
    ('花', '自然', '美しさや短命を示します'),
    ('車', '物', '進行や移動、人生の道を表します'),
    ('橋', '場所', '障害の克服や変化を示唆します'),
    ('山', '自然', '目標達成や困難を示します'),
    ('光', '自然', '希望や指針を意味します'),
    ('影', '自然', '隠された真実や恐怖を表します'),
    ('犬', '動物', '忠誠心や友情を意味します'),
    ('猫', '動物', '独立心や気まぐれを表します'),
    ('魚', '動物', '適応力や豊かさを示します'),
    ('雪', '自然', '冷静さや純粋さを表します'),
    ('雷', '自然', '強い感情や突然の変化を示します'),
    ('空', '自然', '自由な心や無限の可能性を意味します'),
    ('煙', '自然', '過去の記憶や不確実さを示します')
])

conn.commit()
conn.close()
