FROM node:12

WORKDIR /webtaxi

COPY package*.json ./
RUN npm install --silent
CMD ["npm", "start"]

COPY . .
