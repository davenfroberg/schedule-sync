# Use an official Node.js runtime as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Copy the rest of the application code to the working directory
COPY . .

RUN npm i -g @quasar/cli

# Install project dependencies
RUN npm install

# Expose the port on which the application will run
EXPOSE 3000

# Define the command to run the application
RUN quasar build

CMD ["quasar", "dev"]

