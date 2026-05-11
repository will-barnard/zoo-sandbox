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

    # Install additional dependencies for emergent gameplay simulation
    RUN npm install --save some-gameplay-library

    # Copy the new script for critter interactions and evolution
    COPY simulate_critters.js .

    # Command to run both nginx and the critter simulation script
    CMD ["sh", "-c", "node simulate_critters.js & nginx -g 'daemon off;'"]
    