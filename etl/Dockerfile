# 使用 Python 3.9 輕量版
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 安裝我們需要的 Python 套件
# pandas: 處理資料
# sqlalchemy & psycopg2-binary: 連線資料庫用
# feedparser: 讀取 RSS 用
RUN pip install pandas sqlalchemy psycopg2-binary feedparser

# 把 main.py 複製進去
COPY main.py .

# 啟動時執行這行指令
CMD ["python", "main.py"]