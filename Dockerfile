FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 7860 & sleep 5 && python inference.py"]
