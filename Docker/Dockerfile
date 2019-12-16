FROM python:3.8

COPY . /var/sources/.

WORKDIR /var/sources

RUN pip install -U pip setuptools; \
    pip install -r requirements.txt; \
    pip install .

EXPOSE 8080

CMD ["gunicorn", "--config", "gunciorn_conf.py", "app.api:instance_api()"]
