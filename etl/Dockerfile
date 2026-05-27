# 使用 Python 3.9 輕量版
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 把 main.py 複製進去
COPY main.py .

# 啟動時執行這行指令
CMD ["python", "main.py"]
