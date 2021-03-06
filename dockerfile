FROM node:16.10.0

WORKDIR /usr/app

COPY package.json .

RUN npm install --quiet

COPY . .