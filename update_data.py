import json
import os
from datetime import datetime

def main():
    # 現在の時刻を記録（動いているか確認しやすくするため）
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # テスト用データ（ここに後ほどHyperliquidの取得ロジックを入れます）
    data = [
        {"日付": "2025-12-30", "損益": "150.50", "勝敗": "勝ち"},
        {"日付": "2025-12-31", "損益": "-20.00", "勝敗": "負け"},
        {"日付": "2026-01-01", "損益": "85.20", "勝敗": "勝ち"},
        {"日付": "更新テスト", "損益": "0.00", "勝敗": f"最終更新: {now}"}
    ]
    
    # JSONとして保存
    with open('trading_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Successfully updated trading_data.json at {now}")

if __name__ == "__main__":
    main()
