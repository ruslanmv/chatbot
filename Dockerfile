FROM python:3.7

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en

COPY . /

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]