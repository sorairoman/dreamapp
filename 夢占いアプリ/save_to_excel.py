import xlwings as xw
from datetime import datetime

def save_to_excel(keyword, result):
    # 現在の日時を取得
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Excelアプリケーションを起動し、指定されたファイルを開く
    wb = xw.Book('C:\\Users\\7d23\\Desktop\\ソフトウェア開発\\夢占いアプリ\\excel_output.xlsm')
    ws = wb.sheets['占い結果']  # シート名を指定

    # 次の空行を取得
    next_row = ws.range('A' + str(ws.cells.last_cell.row)).end('up').row + 1

    # 結果をシートに追加
    ws.range('A1').value = ["キーワード", "カテゴリ", "占い結果", "検索日時"]
    ws.range(f'A{next_row}').value = [keyword, result[0], result[1], current_time]

    # Excelファイルを保存
    wb.save()
    wb.close()
    print("結果がexcel_output.xlsmに保存されました。")
