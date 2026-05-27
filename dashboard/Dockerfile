FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Streamlit 預設跑在 8501 port
# --server.address=0.0.0.0 是為了讓 Docker 外部可以連線
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
