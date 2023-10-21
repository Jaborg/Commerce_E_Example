FROM apache/airflow:2.6.2-python3.11

WORKDIR /opt/airflow

ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && \
    apt-get install -y make gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow

COPY ./requirement.txt .
COPY ./Makefile .
COPY ./sql_scripts ./sql_scripts



RUN pip install --no-cache-dir -r requirement.txt
RUN make setup




