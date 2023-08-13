FROM python:slim

WORKDIR /app

COPY requirements.txt .


RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m spacy download ru_core_news_md


COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
