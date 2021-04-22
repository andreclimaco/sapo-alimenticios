# pull official base image
FROM node:15.14.0-alpine
USER root

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY --chown=node:node package.json ./
COPY --chown=node:node package-lock.json ./
RUN npm install -g npm@7.10.0
RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent

# add app
COPY --chown=node:node . ./

# start app
CMD ["npm", "start"]