FROM python:3.9

RUN mkdir /data
RUN mkdir /output

COPY main.py .
COPY data/data.txt /data

RUN chmod 777 -R /data
RUN chmod 777 -R /output

WORKDIR /

CMD ["python", "/main.py"]