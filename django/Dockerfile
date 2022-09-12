FROM python:3.10-slim

ARG APP_DIR=/usr/src/app
ARG VENV_DIR=${APP_DIR}/.venv

WORKDIR ${APP_DIR}

# Use the packages from the python environment instead of the global one
ENV PATH=${VENV_DIR}/bin:${PATH}

COPY requirements.txt .

# Add C compiler required to build wsgi
RUN apt update && apt install gcc -y && \
    # Add unprivileged user and group which will be run the application
    groupadd -r -g 1001 python && \
    useradd -r -g 1001 -u 1001 python && \
    python -m venv ${VENV_DIR} && \
    mkdir -p /var/www/app/static && \
    mkdir data && chown python:python data && \
    pip install -r requirements.txt

COPY --chown=python:python entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

USER python

CMD [ "/entrypoint.sh" ]