FROM python:3.7

COPY . /var/sources/.

WORKDIR /var/sources

RUN pip install -U pip setuptools; \
    pip install -r requirements.txt; \
    pip install .

ENV MODELS_PATH=/var/sources/src/monitoring/models
ENV DATA_PATH=/var/sources/src/monitoring/data
 
EXPOSE 8080

CMD ["gunicorn", "--config", "gunicorn.conf.py", "app.api:instance_api()"]
