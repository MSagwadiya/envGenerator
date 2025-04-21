FROM python:3.12-slim as base-env
ADD . /app
WORKDIR /app

RUN pip install --target=/app -r requirements.txt
RUN chmod +x /app/main.py

CMD ["/app/main.py"]