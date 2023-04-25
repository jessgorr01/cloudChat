# Fetching the latest node image on alpine linux
FROM node:16-alpine AS development

# Declaring env
ENV NODE_ENV development

# Setting up the work directory
WORKDIR /app

# Installing dependencies
COPY package.json .

RUN npm install

# Copying all the files in our project
COPY . .

# Expose the port of your application to bind with the host port
EXPOSE 3306

# Starting our application
CMD ["npm", "start"]
