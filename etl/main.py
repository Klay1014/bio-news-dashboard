import pandas as pd
import feedparser
from sqlalchemy import create_engine
import time

# 1. 設定目標：紐約時報健康版 RSS
RSS_URL = "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml"

# 2. 設定倉庫位置：注意 host 是 'db' (因為在 Docker 網路內)
DB_URI = "postgresql://user:password@db:5432/bio_news"

def get_news():
    print(f"開始抓取新聞: {RSS_URL}...")
    feed = feedparser.parse(RSS_URL)
    data = []
    # 抓前 10 筆就好
    for entry in feed.entries[:10]:
        data.append({
            "title": entry.title,
            "link": entry.link,
            "published": getattr(entry, 'published', 'No Date'),
            "source": "NYT Health"
        })
    return pd.DataFrame(data)

def save_to_db(df):
    print("正在連線資料庫...")
    # 建立連線引擎
    engine = create_engine(DB_URI)
    
    # 重試機制：因為資料庫剛啟動時可能還沒準備好
    for i in range(10):
        try:
            # 寫入資料表 'news'，如果存在就附加 (append)
            df.to_sql("news", engine, if_exists='append', index=False)
            print("✅ 成功！資料已寫入 PostgreSQL 資料庫。")
            return
        except Exception as e:
            print(f"資料庫還沒醒，等待 5 秒後重試... ({e})")
            time.sleep(5)
    print("❌ 放棄，連線失敗。")

if __name__ == "__main__":
    print("ETL Worker 啟動中...")
    df = get_news()
    if not df.empty:
        print(f"抓到了 {len(df)} 筆新聞")
        save_to_db(df)
    else:
        print("沒有抓到新聞")