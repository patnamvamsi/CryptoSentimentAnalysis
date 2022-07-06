FROM python:3.8

COPY . /cryptosentimentanalysis

WORKDIR /cryptosentimentanalysis

RUN pip3 install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/cryptosentimentanalysis"

EXPOSE 8004

CMD ["python","-m","uvicorn","main:app","--host=0.0.0.0","--reload","--port","8004"]


#  build an image using this command: sudo docker build -t cryptosentimentanalysis:0.1 .
#  run the image using this command: sudo docker run -p 8004:8004 --name sentimentanalysis cryptosentimentanalysis:0.1

