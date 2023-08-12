FROM python:slim

WORKDIR /app

COPY requirements.txt .


RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
