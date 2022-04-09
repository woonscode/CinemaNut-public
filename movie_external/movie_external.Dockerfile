FROM node:16
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY movie_external.js ./
CMD [ "node", "movie_external.js" ]