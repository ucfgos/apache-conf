FROM node:16-slim

WORKDIR /usr/src/node-http-server

RUN apt-get update && apt-get upgrade -y

COPY main.js .

CMD [ "node", "main.js" ]
