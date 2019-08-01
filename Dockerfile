FROM python:3.6-stretch

ADD src/ /src
WORKDIR /src

RUN pip install -r /src/requirements.txt

EXPOSE 80

CMD FLASK_APP=main.py flask run -p 80 --host=0.0.0.0
