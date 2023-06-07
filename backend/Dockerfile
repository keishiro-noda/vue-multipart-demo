FROM python:3

USER root

RUN mkdir -p /home/guest/my-vue-app/backend
WORKDIR /home/guest/my-vue-app/backend

RUN apt-get update && \
    apt-get install apache2 -y

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# RUN pip install pyOpenSSL --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN cd /home/guest/my-vue-app/backend && \
#     alembic upgrade head