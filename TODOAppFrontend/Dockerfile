FROM node:lts-alpine

WORKDIR /app
COPY . ./
RUN npm install
RUN ["chmod", "+x", "./start-dev-frontend.sh"]

