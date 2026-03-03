import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time

# 設定網頁標題
st.set_page_config(page_title="生醫新聞戰情室", layout="wide")

st.title("🧬 生醫新聞戰情室 (Bio-News Dashboard)")
st.markdown("這是由 **Python ETL** 自動抓取並存入 **PostgreSQL** 的即時資料。")

# 資料庫連線設定 (跟 ETL 一樣，host 是 'db')
DB_URI = os.getenv("DB_URI", "postgresql://user:password@db:5432/bio_news")

def load_data():
    """從資料庫撈取最新的新聞"""
    try:
        engine = create_engine(DB_URI)
        # 簡單的 SQL：撈出所有新聞，並按發布時間排序
        query = "SELECT * FROM news ORDER BY published DESC"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"無法連線到資料庫: {e}")
        return pd.DataFrame()

# 執行撈取
df = load_data()

# === 區塊 1: 數據概覽 ===
col1, col2 = st.columns(2)
with col1:
    st.metric("目前收錄新聞數", f"{len(df)} 篇")
with col2:
    st.metric("資料來源", "紐約時報 (NYT Health)")

# === 區塊 2: 顯示資料表格 ===
st.subheader("📰 最新消息列表")
if not df.empty:
    # 顯示互動式表格
    st.dataframe(
        df[['title', 'published', 'link']], 
        column_config={
            "link": st.column_config.LinkColumn("閱讀連結")
        },
        use_container_width=True
    )
else:
    st.info("目前資料庫是空的，請檢查 ETL Worker 是否有執行成功。")

# === 區塊 3: 手動重新整理按鈕 ===
if st.button('🔄 重新載入資料'):
    st.rerun()