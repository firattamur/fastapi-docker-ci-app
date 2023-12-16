FROM python:3.9

WORKDIR /app

COPY app/ ./app
COPY start.sh ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "start.sh"]