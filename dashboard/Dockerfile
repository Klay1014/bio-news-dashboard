FROM python:3.9-slim

WORKDIR /app

# 安裝 streamlit 和資料庫相關套件
RUN pip install streamlit pandas sqlalchemy psycopg2-binary

COPY app.py .

# Streamlit 預設跑在 8501 port
# --server.address=0.0.0.0 是為了讓 Docker 外部可以連線
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]