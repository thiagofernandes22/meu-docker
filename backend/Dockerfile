FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ /app

EXPOSE 80

CMD ["python", "app.py"]