FROM python:3.9.16

WORKDIR /project

COPY ..

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]