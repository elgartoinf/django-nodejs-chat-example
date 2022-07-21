FROM node:18-bullseye-slim

WORKDIR /app

COPY ./node/package.json /app

RUN npm install && npm cache clean --force

ENV PATH ./node_modules/.bin/:$PATH


