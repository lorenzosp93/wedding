# build stage
FROM node:17.8.0-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ARG ENV_MODE=staging
RUN npm run build -- --mode=${ENV_MODE}

# production stage
FROM nginx:stable-alpine as production-stage
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=build-stage /app/dist .

# Add nginx config
COPY ./nginx.conf /etc/nginx/nginx.conf

# add mime-types
COPY ./mime.types /etc/nginx/mime.types

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
