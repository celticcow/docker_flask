FROM python:3.8

COPY . /app
WORKDIR . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["svr.py"]