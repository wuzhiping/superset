FROM apache/superset

RUN pip install jupyter -i https://mirrors.aliyun.com/pypi/simple/

ENV SUPERSET_SECRET_KEY some_random_base64_string

RUN superset db upgrade
RUN superset init

#ENV FLASK_APP superset
RUN superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@fab.org --password admin

RUN pip install authlib -i https://mirrors.aliyun.com/pypi/simple
RUN pip install google -i https://mirrors.aliyun.com/pypi/simple
RUN pip install --upgrade google-api-python-client -i https://mirrors.aliyun.com/pypi/simple
COPY ./pythonpath /app/pythonpath
