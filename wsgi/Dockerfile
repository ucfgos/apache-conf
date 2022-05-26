FROM python:3.10-slim

ARG ENV_PATH="/usr/src/venv"
WORKDIR /usr/src/app

RUN python -m venv ${ENV_PATH}
ENV PATH="${ENV_PATH}/bin:$PATH"

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y build-essential python-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y build-essential python-dev

COPY main.py .

CMD [ "uwsgi", "--socket", ":29000", "--wsgi-file", "main.py" ]