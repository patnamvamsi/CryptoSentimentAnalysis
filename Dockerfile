FROM python:3.8

COPY shared /shared
COPY CryptoSentimentAnalysis /cryptosentimentanalysis

WORKDIR /cryptosentimentanalysis

RUN pip3 install --upgrade pip \
    && pip3 install -e /shared \
    && pip3 install -r requirements.txt

ENV PYTHONPATH="/cryptosentimentanalysis"

EXPOSE 8004

CMD ["python", "-m", "uvicorn", "main:app", "--host=0.0.0.0", "--reload", "--port", "8004"]
