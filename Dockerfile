FROM python:3.9

COPY main.py .

WORKDIR /

CMD ["python", "/main.py"]