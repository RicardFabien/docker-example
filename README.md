Example of a dockerised app

Requirement: Docker

- Download the project
- In a terminal, enter the project file(you should be in the same file as this README)
- Enter the command `docker-compose build`, this command may take a while, depending on the speed of your internet connection
- Once the precedent command is done, enter the command `docker-compose up` and wait for it to finish
- Once finish, you should be able to navigate to `localhost:3000` in your browser to test the project

Project layout:
- /Backend: contains a flask server that acts as the link between the frontend and the database, with a dockerfile
- /frontend: contains a react server, with a dockerfile
- /initdb: contains initialisation files for the database
- /nginx: contains the configuration files for an nginx reverse proxy
    
