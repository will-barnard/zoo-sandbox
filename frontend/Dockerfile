    # Use an official Node runtime as a parent image
    FROM node:16

    # Set the working directory in the container
    WORKDIR /usr/src/app

    # Copy package.json and package-lock.json
    COPY package*.json ./

    # Install any needed packages specified in package.json
    RUN npm install

    # Bundle app source inside Docker image
    COPY . .

    # Build the application
    RUN npm run build

    # Expose the port the app runs on
    EXPOSE 8080

    # Command to run the application
    CMD ["npm", "run", "serve"]
    