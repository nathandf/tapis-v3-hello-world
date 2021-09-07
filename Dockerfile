FROM python:3.9

COPY main.py .

RUN chmod 777 -R /data
RUN chmod 777 -R /output

WORKDIR /

CMD ["python", "/main.py"]