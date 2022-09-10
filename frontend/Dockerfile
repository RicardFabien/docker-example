FROM node:13.12.0-alpine

EXPOSE 3000
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
# Ensures the app runs the node module 
# and not any other potential executable present in the container
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g

# add app
COPY . ./

# start app
CMD ["npm", "start"]