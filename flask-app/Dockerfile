FROM python:3.12-slim

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ENV FLASK_RUN_PORT=8000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
