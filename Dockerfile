FROM python:3.11-slim

WORKDIR /app

# 1) requirements.txt 위치가 flaskStudy 루트라면:
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 2) minimalapp 디렉토리만 복사
COPY minimalapp ./minimalapp

# 3) 컨테이너에서 작업 디렉토리를 minimalapp으로 이동
WORKDIR /app/minimalapp

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD ["flask", "run"]
