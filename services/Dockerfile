FROM python:3.9.5-slim-buster

WORKDIR /usr/src/app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./project/requirements.txt /usr/app/requirements.txt
RUN pip install -r /usr/app/requirements.txt

COPY . /usr/src/app

# COPY ./project/dados.py /usr/app/dados.py
CMD ["python", "-u", "/usr/src/app/project/dados.py"]

# run entrypoint.sh
COPY ./project/entrypoint.sh /usr/app/entrypoint.sh
ENTRYPOINT ["/usr/app/entrypoint.sh"]

