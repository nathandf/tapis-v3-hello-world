FROM python:3.9

RUN mkdir /data
RUN mkdir /output

COPY main.py .
COPY data/data.txt /data

WORKDIR /
CMD ["python", "main.py"]

