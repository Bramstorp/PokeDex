FROM node:16.10.0

RUN npm install -g npm@8.1.3
RUN npm install -g @vue/cli@4.5.15

RUN mkdir /app && chown node:node /app

USER node

WORKDIR /app

RUN npm rebuild esbuild
