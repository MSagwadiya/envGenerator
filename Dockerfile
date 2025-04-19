FROM python3.12-slim as base-env
ADD . /app
WORKDIR /app

RUN pip install --target=/app -r requirements.txt

CMD ["/app/main.py"]

